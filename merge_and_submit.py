import git, json, importlib, zipfile, os, shutil, random, sys, os
import warnings

import pandas as pd

from utils.compression import compress

# Commit changes? [Y]es/[N]o/Leave string empty to be prompted
default_commit = ""
# Push to remote? [Y]es/[N]o/Leave string empty to be prompted
default_push = ""
# Calculate score with zlib compression? [Y]es/[N]o/Leave string empty to be prompted
default_compress = ""
# Submit to Kaggle? [Y]es/[N]o/Leave string empty to be prompted
default_kaggle = ""

# Configuration: add player directories here
players = [
    ('xsot', 'xsot/'),
    ('ovs', 'ovs/'),
    ('att', 'att/'),
    ('joking', 'joking/'),
    ('mwi', 'mwi/'),
    ('combined', 'combined_solutions/')
]

# Output directory
output_dir = 'merged/'

submission_dir = "submission"

def promptYN(prompt, default = ""):
    response = default or (input(prompt+" ")+" ")[0].upper()
    while response not in "YN":
        response = (input("Improper input, try Y or N")+" ")[0].upper()
    return response == "Y"


#################
# STEP 1: merge #
#################


def preprocess(source):
    new_lines = []
    for line in source.replace("\r\n", "\n").split("\n"):
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
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=1427788625&single=true&output=csv")
    gold_score = df.loc[7:,"BEST"].reset_index(drop=True).astype(int)
except:
    gold_score = ['???'] * 400

task_ids = [s.strip() for s in open("task_ids.txt")]

single_file_view = []
scores = []

for i in range(1, 401):
    fname = f"task{i:03}.py"

    # Collect all solutions for this task
    solutions = []

    for player_name, player_dir in players:
        path = os.path.join(player_dir, fname)
        if os.path.exists(path):
            code = preprocess(open(path).read())
            if not code:
                continue
            zipped_code = compress(code.encode())
            zipped_score = len(zipped_code)
            score = len(code)
            solutions.append((zipped_score, score, player_name, path, zipped_code, code))

    # Skip if no solutions found
    if not solutions:
        scores.append(99999)

    # Sort by zipped score (shortest first), score, then by player name for tie-breaking (combined last)
    solutions.sort(key=lambda x: (x[0], x[1], x[2] == 'combined', x[2]))

    output_path = os.path.join(output_dir, fname)

    # Multiple solutions exist, merge them
    lines = []

    # Add the best solution first
    zipped_score, score, best_player, best_path, _, code = solutions[0]
    with open(best_path) as f:
        z = f" ({score} unzipped)" * (zipped_score != score)
        if zipped_score == gold_score[i-1]:
            score_string = f"{zipped_score}{z} bytes, gold"
        else:
            score_string = f"{zipped_score}{z} vs {gold_score[i-1]} bytes for gold"
        # append the raw source file (it will be cleaned up again in step 2)
        lines.append(f"# {best_player} ({score_string})")
        lines.extend(f.readlines())
        single_file_view.append(f"# task {i}: {score_string}, https://arcprize.org/play?task={task_ids[i-1]}\n" + code)
    best_score = zipped_score
    scores.append(best_score)

    # Add other solutions with comments
    for zipped_score, score, player_name, path, _, _ in solutions[1:]:
        z = f" ({score} unzipped)" * (zipped_score != score)
        if score == best_score:
            lines.extend(["", f"### {player_name} (tied, {zipped_score}{z} bytes)"])
        else:
            lines.extend(["", f"### {player_name} ({zipped_score}{z} bytes)"])

        with open(path) as f:
            lines.extend(f.readlines())

    # Write merged file
    with open(output_path, 'w') as f:
        writelines_with_newline(f, lines)

with open(f"{output_dir}/all_tasks.py", 'w') as f:
    writelines_with_newline(f, single_file_view)

with open(f"{output_dir}/scores.txt", 'w') as f:
    for score in scores:
        print(score, file=f)

print("Merging complete!")

####################################
# STEP 2: Copy raw into submission #
####################################

for n in range(1,401):
    name = f"task{n:03d}.py"
    with open(output_dir + name, "r") as file:
        src = file.read()
    src = preprocess(src)
    #with open(f"{submission_dir}/{name}", "r") as file:
    #    l = len(file.read())
    if 1:#l > len(src):
        with open(f"{submission_dir}/{name}", "w") as file:
            file.write(src)

#######################
# STEP 3: auto_submit #
#######################


warnings.filterwarnings("ignore")

repo = git.Repo('.')
last_commit = repo.head.commit

too_long = []
failing = []
passing = []
merges = []
total_save = 0
sys.path.insert(0, os.path.abspath('./'))


def test_task(task_name, dir, subsets=('train', 'test', 'arc-gen')):
    test_filename = f'inputs/{task_name}.json'
    with open(test_filename) as test_file:
        test_data = json.load(test_file)
    try:
        s = importlib.import_module(f'{dir}.{task_name}')
        importlib.reload(s)
    except:
        # python file not found
        return False
    if hasattr(s,'p'):
        submission = s.p
        for subset in subsets:
            for test_case in test_data[subset]:
                try:
                    repr = lambda i:json.dumps(eval(str(i).replace("False","0").replace("True","1").replace(".0","")))
                    if not repr(submission(test_case['input'])) == repr(test_case['output']):
                        # incorrect result
                        return False
                except KeyboardInterrupt as e:
                    # user interrupt
                    print('break')
                    return False
                except:
                    # error caused by solution
                    return False
        # passed all tests
        return True

# Add untracked tasks if any exist
try: 
   repo.git.add("-N", ["*/task*.py"])
except:
   pass

for diff in repo.index.diff(None):
 path = diff.a_path
 if output_dir in path:
  merges += [path]
  continue
 if "task" not in path:
  continue
 dir, task_name = path.split("/")
 task_name = task_name[:-3]
 try:
  repo.git.ls_tree(f"{last_commit.hexsha}", path)
  old_src = compress(preprocess(repo.git.show(f"{last_commit.hexsha}:{path}")).encode())
 except git.exc.GitCommandError as e:
  old_src = b"#" * 2500
 with open(path , "r") as file:
  new_src = compress(preprocess(file.read()).encode())
 save =  len(old_src) - len(new_src)
 if save < 0:
  too_long += [path]
  continue
 if not test_task(task_name, dir):
  failing += [path]
  continue
 passing += [path]
 if dir == submission_dir: total_save += save

if failing:
 print(f"{len(failing)} SOLUTION{'S'*(len(failing)!=1)} FAILED:", failing)
 exit()
if too_long:
 print(f"{len(too_long)} SOLUTION{'S'*(len(too_long)!=1)} ARE LONGER THAN PREVIOUS:", too_long)
print(f"{len(passing)} improved solution{'s'*(len(passing)!=1)}, saving {total_save}b")

if (passing or merges) and promptYN("Commit changes? [Y]es/[N]o", default_commit):
 if passing:
  for path in passing:
   repo.git.add(path)
  repo.git.commit([f'-m Saved {total_save}b on: {passing}'])
 if merges:
  for path in merges:
   repo.git.add(path)
  repo.git.commit([f'-m auto-merged'])


if promptYN("Push improved solutions to remote? [Y]es/[N]o", default_push):
 repo.remote(name='origin').push()

if promptYN("Calculate score with zlib compression?", default_compress):
 score = 1_000_000
 temp_dir = "submission_temp"
 os.makedirs(temp_dir, exist_ok=True)

 for task_num in range(1, 401):
  task_name = f"task{task_num:03d}.py"
  path_in  = f"{submission_dir}/{task_name}"
  with open(path_in) as task_in:
   task_src = preprocess(task_in.read()).encode()

   zipped_src = compress(task_src)
   improvement = len(task_src) - len(zipped_src)

   if improvement > 0:
    # make sure zipped program still passes
    # TODO: in the merge phase, we could have passed over a longer, but correct
    # zipped program that is shorter than this program unzipped
    with open(f"{temp_dir}/{task_name}", "wb") as file:
     file.write(zipped_src)
    if test_task(task_name[:-3], temp_dir, subsets=('train',)):
     task_src = zipped_src
   with open(f"{temp_dir}/{task_name}", "wb") as file:
    file.write(task_src)
   score -= len(task_src)

 with zipfile.ZipFile(f"submission.zip", "w") as zipf:
  for task_num in range(1, 401):
   task_name = f"task{task_num:03d}.py"
   src_path = f"{temp_dir}/{task_name}"
   if os.path.exists(src_path):
    zipf.write(src_path, arcname=task_name)
 try:
  shutil.rmtree(temp_dir)
 except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror))

 print("Score:", score)
 if promptYN("Submit to Kaggle? [Y]es/[No]", default_kaggle):
  import kaggle
  kaggle.api.authenticate()
  kaggle.api.competition_submit("submission.zip", f"Est. Score: {score} " + "".join([random.choice("⬛🟦🟥🟩🟨⬜🟪🟧🟫")for _ in[0]*9]), "google-code-golf-2025")
