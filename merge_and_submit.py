# Commit changes? Y[es]/[No]/Leave string empty to be prompted
default_commit = ""
# Push to remote? Y[es]/[No]/Leave string empty to be prompted
default_push = ""
# Calculate score with zlib compression? [Y]es/[No]/Leave string empty to be prompted
default_compress = ""
# Submit to Kaggle? [Y]es/[No]/Leave string empty to be prompted
default_kaggle = ""

# Configuration: add player directories here
players = [
    ('xsot', 'xsot/'),
    ('ovs', 'ovs/'),
    ('att', 'att/'),
    ('combined', 'combined_solutions/')
]

# Output directory
output_dir = 'merged/'

submission_dir = "combined_solutions"


#################
# STEP 1: merge #
#################

import os
import shutil


def comp(path):
    new_lines = []
    for line in open(path):
        if "nomerge" in line:
            return None
        if line.startswith('##'):
            break
        if line.startswith('#'):
            continue
        line = line.rstrip()
        if line:
            new_lines.append(line)
    return '\n'.join(new_lines)


def writelines_with_newline(file, lines):
    file.writelines(
        line if line.endswith("\n") else line + "\n"
        for line in lines
    )


try:
    import pandas as pd
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=1427788625&single=true&output=csv")
    gold_score = df.loc[7:,"BEST"].reset_index(drop=True).astype(int)
except:
    gold_score = ['???'] * 400

task_ids = [s.strip() for s in open("task_ids.txt")]

single_file_view = []

for i in range(1, 401):
    fname = f"task{i:03}.py"

    # Collect all solutions for this task
    solutions = []

    for player_name, player_dir in players:
        path = os.path.join(player_dir, fname)
        if os.path.exists(path):
            code = comp(path)
            if not code:
                continue
            score = len(code.encode('utf-8'))
            solutions.append((score, player_name, path, code))

    # Skip if no solutions found
    if not solutions:
        continue

    # Sort by score (shortest first), then by player name for tie-breaking
    solutions.sort(key=lambda x: (x[0], x[1]))

    output_path = os.path.join(output_dir, fname)

    # Multiple solutions exist, merge them
    lines = []

    # Add the best solution first
    best_score, best_player, best_path, code = solutions[0]
    with open(best_path) as f:
        if best_score == gold_score[i-1]:
            score_string = f"{best_score} bytes, gold"
        else:
            score_string = f"{best_score} vs {gold_score[i-1]} bytes for gold"
        # append the raw source file (it will be cleaned up again by pack.sh)
        lines.append(f"# {best_player} ({score_string})")
        lines.extend(f.readlines())
        single_file_view.append(f"# task {i}: {score_string}, https://arcprize.org/play?task={task_ids[i-1]}:\n" + code)

    # Add other solutions with comments
    for score, player_name, path, _ in solutions[1:]:
        if score == best_score:
            lines.extend(["", f"### {player_name} (tied, {score} bytes)"])
        else:
            lines.extend(["", f"### {player_name} ({score} bytes)"])

        with open(path) as f:
            lines.extend(f.readlines())

    # Write merged file
    with open(output_path, 'w') as f:
        writelines_with_newline(f, lines)

    with open(f"{output_dir}/all_tasks.py", 'w') as f:
        writelines_with_newline(f, single_file_view)

print("Merging complete!")

############################################
# STEP 2: Copy raw into combined_solutions #
############################################

import re
for n in range(1,401):
 name = f"task{n:03d}.py"
 with open(f"merged/{name}", "r") as file:
    src = file.read()
 src =  re.sub(r"#.*\n", "",re.sub(r"\s*##[\s\S]*", "", src))
 with open(f"combined_solutions/{name}", "r") as file:
    l = len(file.read())
 if l > len(src):
    with open(f"combined_solutions/{name}", "w") as file:
        file.write(src)

#######################
# STEP 3: auto_submit #
#######################


import git, json, importlib, kaggle, zlib, zipfile, os, shutil, random, sys, os, re
import warnings
warnings.filterwarnings("ignore")

repo = git.Repo('.')
last_commit = repo.head.commit

too_long = []
failing = []
passing = []
merges = []
total_save = 0
sys.path.insert(0, os.path.abspath('./'))

def test_task(task_name):
 test_filename = f'inputs/{task_name}.json'
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
 if "merge/" in path:
  merges += [path]
  continue
 if "combined_solutions/task" not in path: 
  continue
 if "alt" in path:
  passing += [path[-14:-3]]
 old_src = bytes(repo.git.show(f"{last_commit.hexsha}:{path}"),"u8")
 with open(path , "r") as file:
  new_src = bytes(file.read(),"u8")
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

if (passing or merges) and promptYN("Commit changes? [Y]es/[N]o", default_commit):
 if passing:
  for task in passing:
   repo.git.add(f"{submission_dir}/{task}.py")
  repo.git.commit([f'-m Saved {total_save}b on: {passing}'])
 if merges:
  for path in merges:
   repo.git.add(path)
  repo.git.commit([f'-m auto-merged'])


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
