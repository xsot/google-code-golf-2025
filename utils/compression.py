import ast
import deflate
import re
import zlib
import zopfli.zlib
import functools

PREFIXES = [b"",b"\n", b"\r",b"\f",b"\n\f",b"\r\f"] + [bytes([c,ne]) for c in b"\t\n\f\r 0123456789#" for ne in b"\n\r"]
POSTFIXES = [b"",b" ",b"\t",b"\n",b"\r",b"\f",b"#",b";",b"\t ",b" \t",b"\np"] + [b"#"+bytes([n]) for n in range(32,127)]

@functools.lru_cache(maxsize=2048)
def compress(task_src: bytes) -> bytes:

    for task_src_2 in (sub_vars(task_src), task_src):

        # if adding a new compression method, try to keep these in order of
        # fastest to slowest
        task_src = min(task_src, compress_with_zlib(task_src, task_src_2), key=len)
        task_src = min(task_src, compress_with_libdeflate(task_src, task_src_2), key=len)
        task_src = min(task_src, compress_with_zopfli(task_src, task_src_2), key=len)
    
    return task_src

def compress_with_zlib(task_src: bytes, task_src_2: bytes) -> bytes:
    zipped_src = zip_src(task_src_2, method="zlib", window=-9)

    if len(zipped_src) > len(task_src) + 10:
        return task_src

    for pre in PREFIXES:
        for post in POSTFIXES:
            if len(pre+post) > 3: continue
            for window in (-9, -15):
                z_src = zip_src(pre+task_src_2+post, method="zlib", window=window)
                if len(z_src)<len(zipped_src):zipped_src = z_src

    return zipped_src

def compress_with_zopfli(task_src: bytes, task_src_2: bytes) -> bytes:
    zipped_src = zip_src(task_src_2, method="zopfli")
    if len(zipped_src) > len(task_src) + 10:
        return task_src
    for pre in PREFIXES:
        for post in POSTFIXES:
            if len(pre+post) > 3: continue
            z_src = zip_src(pre+task_src_2+post, method="zopfli")
            if len(z_src)<len(zipped_src):zipped_src = z_src
    return zipped_src


def compress_with_libdeflate(task_src: bytes, task_src_2: bytes) -> bytes:
    # libdeflate hardcodes a window of 32768
    # https://github.com/ebiggers/libdeflate/blob/master/lib/zlib_compress.c
    zipped_src = zip_src(task_src_2, method="libdeflate", window=-15)
    if len(zipped_src) > len(task_src) + 10:
        return task_src
    for pre in PREFIXES:
        for post in POSTFIXES:
            if len(pre+post) > 3: continue
            z_src = zip_src(pre+task_src_2+post, method="libdeflate", window=-15)
            if len(z_src)<len(zipped_src):zipped_src = z_src
    return zipped_src

def zip_src(src: bytes, method: str, window: int = None) -> bytes:
    # Save on import re
    header = b"#coding:L1\nimport zlib"
    if src[:10]==b"import re\n":
        header+=b",re"
        src=src[10:]
    if method == "zopfli":
        iterations = 20 # this is enough to get us the best scores as of now
        compressed = zopfli.zlib.compress(src, numiterations=iterations, blocksplitting=False)
        window = -(((compressed[0] >> 4) & 0x0F) + 8)
        compressed = compressed[2:-4]
    elif method == "libdeflate":
        compression_level = 12 # Max Compression
        # the python wrapper adds a header a footer
        # it's always worth it to strip them and specify the window length in the decoder
        compressed = deflate.zlib_compress(src, compression_level)[2:-4]
    elif method == "zlib":
        compression_level = 9 # Max Compression
        compressed = zlib.compress(src, compression_level, window)
    else:
        raise ValueError(f"Unknown method {method}")

    def sanitize(b_in):
        """Clean up problematic bytes in compressed b-string"""
        b_out = bytearray()
        for ch,ch1 in zip(b_in,b_in[1:]+b"'"):
            if   ch==0  : b_out+=b"\\x00" if ch1 in b"01234567" else b"\\0"
            elif ch==13 : b_out+=b"\\r"
            elif ch==92 and ch1 in b"\\\n\"\'01234567NUabfnrtvxu": b_out+=b"\\\\"
            else:         b_out.append(ch)
        return b_out

    compressed = sanitize(compressed)

    delim = b'"""' if compressed[-1:] != b'"' else b"'''"

    newlines = compressed.count(ord("\n"))
    single = compressed.count(ord("'")) + newlines
    double = compressed.count(ord('"')) + newlines
    if 4 > single < double:
        delim = b"'"
        compressed = compressed.replace(b"'", b"\\'").replace(b"\n", b"\\n")
    elif 4 > double < single:
        delim = b'"'
        compressed = compressed.replace(b'"', b'\\"').replace(b"\n", b"\\n")

    return header+b"\nexec(zlib.decompress(bytes(" + \
        delim + compressed + delim + \
        b',"L1")'+(b',%d'%window if window<15 else b'')+b'))'

def sub_vars(src: bytes, alphabet:bytes = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz") -> bytes:
    
    if set(alphabet) != set(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz"):
        raise ValueError("alphabet must be an ordering of all letters except lowercase p")
    
    vars_prev = get_vars(src, alphabet)

    if len(vars_prev) == 0:
        return src
    varless = re.sub(br"(?<!\\)\b[%b]\b(?!['\"])" % alphabet,b"_", src)
    rest = set(re.findall(br"[%b]" % alphabet, varless))

    # first try replacing variables with letters that already exist in the source,
    # most common first
    vars_new_1 = sorted(sorted(rest), key=varless.count)[::-1]

    # then use the rest of the letters. bruteforcing different orderings
    # may yield byte saves
    vars_new_2 = sorted(set(bytes([v]) for v in alphabet) - rest)

    vars_new = vars_new_1 + vars_new_2
    trans = dict(zip(vars_prev, vars_new))

    return re.sub(br"(?<!\\)\b[%b]\b(?!['\"])" % b"".join(vars_prev), lambda c:trans[c.group()], src)

def get_vars(src: bytes, alphabet: bytes):
    tree = ast.parse(src)

    identifiers = set()

    for i in ast.walk(tree):
        if isinstance(i, ast.arg):
           identifiers.add(i.arg.encode())
        if isinstance(i, ast.Name):
            identifiers.add(i.id.encode())
        if isinstance(i, ast.FunctionDef):
            identifiers.add(i.name.encode())

    return sorted(i for i in identifiers if len(i)==1 and i in alphabet)