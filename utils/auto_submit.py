# Commit all improved solutions? Y[es]/[No]/Leave string empty to be prompted
default_commit = ""
# Push to remote? Y[es]/[No]/Leave string empty to be prompted
default_push = ""
# Calculate score with zlib compression? [Y]es/[No]/Leave string empty to be prompted
default_compress = ""
# Submit to Kaggle? [Y]es/[No]/Leave string empty to be prompted
default_kaggle = ""

submission_dir = "combined_solutions"


import git, json, importlib, kaggle, zlib, zipfile, os, shutil, random, sys, os, re
import warnings
warnings.filterwarnings("ignore")

repo = git.Repo('.')
last_commit = repo.head.commit

too_long = []
failing = []
passing = []
total_save = 0
sys.path.insert(0, os.path.abspath('./'))

def test_task(task_name):
 test_filename = f'google-code-golf-2025\\{task_name}.json'
 with open(test_filename) as test_file:
  test_data = json.load(test_file)
  try:
   s = importlib.import_module(f'{submission_dir}.{task_name}')
   importlib.reload(s)
  except:
   return
  if hasattr(s,'p'):
   submission = s.p
   for name in test_data:
    for test_case in test_data[name]:
     try:
      repr = lambda i:json.dumps(eval(str(i).replace("False","0").replace("True","1").replace(".0","")))
      if not repr(submission(test_case['input'])) == repr(test_case['output']):
       return False
     except KeyboardInterrupt as e:
      print('break')
      return
     except:
      return False
    return True

for diff in repo.index.diff(None):
 path = diff.a_path
 task_name = path[-10:-3]
 if "/task" not in path: continue
 if "alt" in path:
  passing += [path[-14:-3]]
 old_src = repo.git.show(f"{last_commit.hexsha}:{path}")
 with open(path , "r") as file:
  new_src = file.read()
 if len(new_src) > len(old_src):
  too_long += [task_name]
  continue
 if not test_task(task_name):
  failing += [task_name]
  continue
 passing += [task_name]
 total_save += len(old_src) - len(new_src)

if failing:
 print(f"{len(failing)} SOLUTION{'S'*(len(failing)!=1)} FAILED:", failing)
if too_long:
 print(f"{len(too_long)} SOLUTION{'S'*(len(too_long)!=1)} ARE WORST THAN CURRENT BEST:", too_long)
print(f"{len(passing)} improved solution{'s'*(len(passing)!=1)}, saving {total_save}b")

def promptYN(prompt, default = ""):
 response = default or input(prompt)[0].upper()
 while response not in "YN":
  response = input("Improper input, try Y or N")[0].upper()
 return response == "Y"
if passing and promptYN("Commit all improved solutions? [Y]es/[N]o", default_commit):
 for task in passing:
  repo.git.add(f"{submission_dir}/{task}.py")
 repo.git.commit([f'-m Saved {total_save}b on: {passing}'])

if promptYN("Push improved solutions to remote? [Y]es/[N]o", default_push):
 repo.remote(name='origin').push()

if promptYN("Calculate score with zlib compression?", default_compress):
 def zip_src(src, window):
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
 
 def sub_vars(src):
 
  # all letters except lowercase p
  var_names = b"abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  var_regex = br"(?<!\\)\b[%b]\b(?!['\"])" % var_names

  vars_prev = sorted(set(re.findall(var_regex,src)))
  varless = re.sub(var_regex,b"_", src)
  rest = set(re.findall(br"[%b]" % var_names, varless))

  # TODO: Optimize sorting method, could probably save 10-30 bytes
  trans = dict(zip(vars_prev,sorted(sorted(rest), key=varless.count)[::-1] + sorted(set(bytes([v]) for v in var_names) - rest)))

  return re.sub(var_regex, lambda c:trans[c.group()], src)
 
 score = 1_000_000
 temp_dir = "submission_temp"
 os.makedirs(temp_dir, exist_ok=True)

 for task_num in range(1, 401):
  task_name = f"task{task_num:03d}.py"
  path_in  = f"{submission_dir}/{task_name}"
  
  with open(path_in, "rb") as task_in:
   task_src = bytes([b for b in task_in.read() if b != 13])
  
  task_src = sub_vars(task_src)

  zipped_src = zip_src(task_src, -9)
  if len(zipped_src) < len(task_src):
   for pre in [b"",b"\n", b"\r",b"\f",b"\n\f",b"\r\f"] + [bytes([c,ne]) for c in b"\t\n\f\r 0123456789#" for ne in b"\n\r"]:
    for post in [b"",b" ",b"\t",b"\n",b"\r",b"\f",b"#",b";",b"\t ",b" \t",b"\np"] + [b"#"+bytes([n]) for n in range(32,127)]:
     if len(pre+post) > 3: continue
     for window in (-9, -15):
      z_src = zip_src(pre+task_src+post, window)
      if len(z_src)<len(zipped_src):zipped_src = z_src

  improvement = len(task_src) - len(zipped_src)

  if improvement > 0:
   task_src = zipped_src

  score -= len(task_src)
  with open(f"{temp_dir}/{task_name}", "wb") as file:
   file.write(task_src)

 with zipfile.ZipFile(f"submission.zip", "w") as zipf:
  for task_num in range(1, 401):
   task_name = f"task{task_num:03d}.py"
   src_path = f"{temp_dir}/{task_name}."
   if os.path.exists(src_path):
    zipf.write(src_path, arcname=task_name)
 try:
  shutil.rmtree(temp_dir)
 except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror))

 print("Score:", score)
 if promptYN("Submit to Kaggle? [Y]es/[No]", default_kaggle):
  kaggle.api.authenticate()
  kaggle.api.competition_submit("submission.zip", f"Est. Score: {score} " + "".join([random.choice("⬛🟦🟥🟩🟨⬜🟪🟧🟫")for _ in[0]*9]), "google-code-golf-2025")

 os.remove("submission.zip")
