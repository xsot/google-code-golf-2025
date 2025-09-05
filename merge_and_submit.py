import base64
import git
import json
import kaggle
import os
import pandas as pd
import random
import sys
import zipfile

from utils.compression import compress

# Update merged directory? [Y]es/[N]o/Leave string empty to be prompted
default_merge = ""
# Commit changes? [Y]es/[N]o/Leave string empty to be prompted
default_commit = ""
# Push to remote? [Y]es/[N]o/Leave string empty to be prompted
default_push = ""
# Submit to Kaggle? [Y]es/[N]o/Leave string empty to be prompted
default_kaggle = ""

# Configuration: Skips testing whether solutions pass. Use with caution
assume_passing = False

# Configuration: Update all solutions. Use, for example, if you have updated
# the compression function and want to run it on all files
update_all = False

# Configuration: add player directories here
player_dirs = [
    'att',
    'joking',
    'mwi',
    'ovs',
    'xsot',
    'combined_solutions',
]

output_dir = "merged"

task_count = 400
max_size = 2500

num_to_task_name = lambda n: f"task{n:03d}"

as_path = lambda dir, name, extension = "py": dir + "/" + name + "." + extension

as_dir_and_name = lambda path: (path.split("/")[0], path.split("/")[1][:-3])

def preprocess(source):
    # Allows preprocess to work on str objects as well as bytes objects
    match_type = lambda s: s if type(source) == str else s.encode()

    new_lines = []
    for line in source.replace(match_type("\r\n"), match_type("\n")).split(match_type("\n")):
        if match_type("nomerge") in line:
            return None
        if line.startswith(match_type('##')):
            break
        if line.startswith(match_type('#')):
            continue
        line = line.rstrip()
        if line:
            new_lines.append(line)
    return match_type('\n').join(new_lines)

def promptYN(prompt, default = ""):
    """ Get a yes or no answer from input """
    response = default or (input(prompt+" ")+" ")[0].upper()
    while response not in "YN":
        response = (input("Improper input, try Y or N ")+" ")[0].upper()
    return response == "Y"

def test_task(task_name, src, subsets=('train', 'test', 'arc-gen')):
    test_filename = f'inputs/{task_name}.json'
    with open(test_filename) as test_file:
        test_data = json.load(test_file)
    try:
        s = dict()
        exec(src, s)
        submission = s['p']
    except:
        print("Load fail")
        return False
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

def writelines_with_newline(file, lines):
    file.writelines(
        line if line.endswith("\n") else line + "\n"
        for line in lines
    )

# Init path & git repo
sys.path.insert(0, os.path.abspath('./'))

repo = git.Repo(".")
last_commit = repo.head.commit

# Track changed (or newly created) files
try:
   repo.git.add("-N", ["*/task*.py"])
except:
   pass

# Read in data from tasks.json, or rebuild it if its not there
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    # Error if json is formatted incorrectly
    assert(len(tasks) == task_count)
    assert(all(task_data["solutions"] and task_data["gold"] and task_data["best"] for task_data in tasks.values()))
except:
    if promptYN("tasks.json is missing or unreadable. Try rebuilding it?"):
        tasks = {num_to_task_name(n): {"gold": max_size, "best": max_size, "solutions": dict()}
            for n in range(1,task_count+1)}
        # if we couldn't read tasks.json, consider all existing tasks changed
        update_all = True
    else:
        exit()

# Update golds
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=1427788625&single=true&output=csv")
gold_score = df.loc[7:,"BEST"].reset_index(drop=True).astype(int)

for n in range(1, task_count + 1):
    tasks[num_to_task_name(n)]["gold"] = int(gold_score[n-1])

# Update changed tasks
changed_tasks = [diff.a_path for diff in repo.index.diff(None)
    if "/task" in diff.a_path and output_dir not in diff.a_path]

if update_all:
    changed_tasks = list(filter(os.path.exists,
        [as_path(player, num_to_task_name(n))
            for n in range(1, task_count+1)
            for player in player_dirs]))


print(f"Updating {len(changed_tasks)} changed tasks...")

failing = []
too_long = []
passing = []
total_save = 0
for i, path in enumerate(changed_tasks):
    print(f"\t{i}/{len(changed_tasks)}: {path}")

    player, task_name = as_dir_and_name(path)

    task_sols = tasks[task_name]["solutions"]
    with open(path, "r") as file:
        src = file.read().encode()

    preprocessed = preprocess(src)

    if not (assume_passing or test_task(task_name, preprocessed)):
        failing.append(path)
        continue

    # Compress unless the compressed code fails
    compressed = compress(preprocessed)
    if not (assume_passing or test_task(task_name, compressed)):
        compressed = preprocessed

    if player in task_sols and len(compressed) > task_sols[player]["size_compressed"]:
        too_long.append((path, len(compressed), task_sols[player]["size_compressed"]))
        continue

    passing.append(path)

    # Update JSON
    tasks[task_name]["solutions"][player] = {
        "source" : base64.b64encode(src).decode('ASCII'),
        "size_uncompressed" : len(preprocessed),
        "compressed" : base64.b64encode(compressed).decode('ASCII'),
        "size_compressed" : len(compressed)
    }

    # Update best
    improvement = tasks[task_name]["best"] - len(compressed)
    if improvement > 0:
        tasks[task_name]["best"] = len(compressed)
        total_save += improvement

# Exit if there are problems with any changed solutions
if any(failing) or any(too_long):
    if any(failing):
        print(f"{len(failing)} TASK{'S' * (len(failing) != 1)} FAILING:")
        for path in failing:
            print("\t" + path)
    if any(too_long):
        print(f"{len(too_long)} TASK{'S' * (len(too_long) != 1)} WORSE THAN PREVIOUS:")
        for path, current, best in too_long:
            print(f"\t{path} - current: {current}, best: {best}")
    print("ABORTING MERGE")
    exit()

# Update tasks.json
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# Show change data
total_score = max_size * task_count - sum(task_data['best'] for task_data in tasks.values())

print(f"Saved {total_save} bytes")
print(f"Score: {total_score}")

# Update merged files
if not promptYN("Update merged directory? [Y]es/[N]o", default_merge):
    exit()

print("Merging...")

all_tasks_lines = []

task_ids = [s.strip() for s in open("task_ids.txt")]

for i in range(1, task_count + 1):
    task_name = num_to_task_name(i)
    task_data = tasks[task_name]
    solutions = task_data["solutions"]
    gold = task_data["gold"]
    best_score = task_data["best"]

    # Sort by zipped score (shortest first), score, then by player name for tie-breaking (combined last)
    ordered = sorted(solutions, key =
        lambda name: (
            solutions[name]["size_compressed"],
            solutions[name]["size_uncompressed"],
            name == "combined_solutions",
            name
        ))

    lines = []

    for idx, player in enumerate(ordered):
        solution = solutions[player]
        score = solution["size_compressed"]
        unzipped_score = solution["size_uncompressed"]
        code = base64.b64decode(solution["source"]).decode()
        is_best = idx == 0

        prefix = "tied, " * (score == best_score and not is_best)
        postfix = "bytes" if not is_best else "bytes, gold" if score==gold else f"vs {gold} bytes for gold"
        hashes = "#" if is_best else "###"

        score_string = f"{prefix}{score}{f' ({unzipped_score} unzipped)' * (unzipped_score != score)} {postfix}"

        if is_best:
            all_tasks_lines.append(f"# task {i}: {score_string}, https://arcprize.org/play?task={task_ids[i-1]}\n" + preprocess(code))
        else:
            lines.append("")

        lines.append(f"{hashes} {player.replace('combined_solutions', 'combined')} ({score_string})")
        lines.append(code)

        with open(as_path(output_dir, task_name), "w") as file:
            writelines_with_newline(file, lines)

with open(as_path(output_dir, "all_tasks"), "w") as file:
    writelines_with_newline(file, all_tasks_lines)

with open(as_path(output_dir, "scores", "txt"), "w") as file:
    for task in tasks.values():
        print(task["best"], file=file)

# Commit changes
if promptYN("Commit changes? [Y]es/[N]o", default_commit):
    repo.git.add("*/task*.py")
    repo.git.add("merged/*")
    repo.git.add("tasks.json")
    repo.git.commit([f'-m +{total_save}={total_score}/{1_000_000 - sum(gold_score)}'])

# Push
if promptYN("Push improved solutions to remote? [Y]es/[N]o", default_push):
    repo.remote(name='origin').push()

# Submit
if promptYN("Submit to Kaggle? [Y]es/[No]", default_kaggle):
    temp_path = "_temp.py"
    with zipfile.ZipFile(f"submission.zip", "w") as zipf:
        for task_num in range(1, task_count + 1):
            task_name = num_to_task_name(task_num)
            task_source = base64.b64decode(min(tasks[task_name]["solutions"].values(),
                key=lambda s:s["size_compressed"])["compressed"])
            with open(temp_path, "wb") as temp_file:
                temp_file.write(task_source)
                zipf.write(temp_path, arcname=task_name)
    kaggle.api.authenticate()
    kaggle.api.competition_submit("submission.zip", f"Est. Score: {total_score} " + "".join([random.choice("⬛🟦🟥🟩🟨⬜🟪🟧🟫")for _ in[0]*9]), "google-code-golf-2025")
