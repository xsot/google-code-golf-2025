import re
import zlib
import functools

PREFIXES = [b"",b"\n", b"\r",b"\f",b"\n\f",b"\r\f"] + [bytes([c,ne]) for c in b"\t\n\f\r 0123456789#" for ne in b"\n\r"]
POSTFIXES = [b"",b" ",b"\t",b"\n",b"\r",b"\f",b"#",b";",b"\t ",b" \t",b"\np"] + [b"#"+bytes([n]) for n in range(32,127)]

@functools.lru_cache(maxsize=2048)
def compress(task_src: bytes) -> bytes:
    task_src_2 = sub_vars(task_src)
    zipped_src = zip_src(task_src_2, -9)

    if len(zipped_src) > len(task_src) + 10:
        return task_src

    for pre in PREFIXES:
        for post in POSTFIXES:
            if len(pre+post) > 3: continue
            for window in (-9, -15):
                z_src = zip_src(pre+task_src_2+post, window)
                if len(z_src)<len(zipped_src):zipped_src = z_src

    return min(zipped_src, task_src, key=len)

def zip_src(src: bytes, window: int) -> bytes:
    compression_level = 9 # Max Compression

    # Save on import re
    header = b"#coding:L1\nimport zlib"
    if src[:10]==b"import re\n":
        header+=b",re"
        src=src[10:]
    # We prefer that compressed source not end in a quotation mark
    while (compressed := zlib.compress(src, compression_level, window))[-1] == ord('"'): src += b"#"

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

    delim = b'"""'

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

def sub_vars(src: bytes) -> bytes:
    # all letters except lowercase p
    var_names = b"abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    var_regex = br"(?<!\\)\b[%b]\b(?!['\"])" % var_names

    vars_prev = sorted(set(re.findall(var_regex,src)))
    varless = re.sub(var_regex,b"_", src)
    rest = set(re.findall(br"[%b]" % var_names, varless))

    # TODO: Optimize sorting method, could probably save 10-30 bytes
    trans = dict(zip(vars_prev,sorted(sorted(rest), key=varless.count)[::-1] + sorted(set(bytes([v]) for v in var_names) - rest)))

    return re.sub(var_regex, lambda c:trans[c.group()], src)
