import base64
import git
import json
import kaggle
import os
import pandas as pd
import numpy as np
import random
import sys
import warnings
import zipfile

"""
    try running compression_search.py a bunch of times. 
    It will try random changes to improve zippability.
    If it finds any, it will add them to compression_experiments dir.
    After you have run compression_search as many times as you want, you should
    discard the change to tasks.json before running merge_and_submit.py

    NOTE: This script will break solutions that import re.
    To fix them, just go into the compression_search directory,
    find the broken task, and add "import re" back into it
"""

from C_compression import compress

# Update merged directory? [Y]es/[N]o/Leave string empty to be prompted
default_merge = ""
# Commit changes? [Y]es/[N]o/Leave string empty to be prompted
default_commit = ""
# Push to remote? [Y]es/[N]o/Leave string empty to be prompted
default_push = ""
# Submit to Kaggle? [Y]es/[N]o/Leave string empty to be prompted
default_kaggle = ""

# Configuration: Skips testing whether solutions pass. Use with caution
assume_passing = True

# Configuration: Force all solutions to be updated. Use, for example, if you have updated
# the compression function and want to run it on all files
update_all = True
# Configuration: Force selected solutions to be updated. Requires update_all = False
update_only = []

# Configuration: How many diffs to report in stats.txt
stats_size = 15

# Configuration: add player directories here
player_dirs = [
    'att',
    'joking',
    'mwi',
    'ovs',
    'xsot',
    'combined_solutions',
    'garry_moss',
    'compression_experiments',
]

warnings.filterwarnings("ignore")

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
        (line if line.endswith("\n") else line + "\n").encode("u8")
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
# gold_score[0] = min(gold_score[0], 56) # by jailctf (this was a joke)

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1-PWgStNEcAz3hGChHZ3ShS56BmB0vnAaUNF4gVUbJsw/export?format=csv")
public_score = df.loc[10:,"ox jam"].reset_index(drop=True).astype(int)

other_scores = df[10:].replace(" ", np.nan).astype("float").drop(columns=["Unnamed: 0", "ox jam"]).reset_index(drop=True)

for n in range(1, task_count + 1):
    tasks[num_to_task_name(n)]["public_gold"] = int(gold_score[n-1])
    tasks[num_to_task_name(n)]["public_best"] = int(public_score[n-1])
    tasks[num_to_task_name(n)]["gold"] = min(int(gold_score[n-1]), tasks[num_to_task_name(n)]["best"])

# Update changed tasks
changed_tasks = [diff.a_path for diff in repo.index.diff(None)
    if "/task" in diff.a_path and output_dir not in diff.a_path]

try:
    # undo `git add -N` after diff
    # https://stackoverflow.com/questions/62444728/how-to-undo-git-add-intent-to-add/62444729
    repo.git.reset("--mixed")
except:
    pass

if update_all:
    changed_tasks = list(filter(os.path.exists,
        [as_path(player, num_to_task_name(n))
            for n in range(1, task_count+1)
            for player in player_dirs]))
elif update_only:
    changed_tasks = list(filter(os.path.exists,
        [as_path(player, num_to_task_name(n))
            for n in update_only
            for player in player_dirs]))


print(f"Updating {len(changed_tasks)} changed tasks...")

failing = []
too_long = []
improved = []
total_save = 0
for i, path in enumerate(changed_tasks):
    print(f"\t{i+1}/{len(changed_tasks)}: {path}")

    player, task_name = as_dir_and_name(path)

    task_sols = tasks[task_name]["solutions"]
    with open(path, "r") as file:
        src = file.read().encode()

    preprocessed = preprocess(src)

    if not (assume_passing or test_task(task_name, preprocessed)):
        failing.append(path)
        continue

    # Ideally, we could run a single compression with
    #  rand_passes=some_big_number , pre_and_post=True
    # However, that would be waaaay slow
    #
    # it might not be too bad to try something like
    # compress(preprocessed,rand_passes=5,pre_and_post=True)
    compressed, stats = min((
        compress(preprocessed,rand_passes=50,pre_and_post=False),
        compress(preprocessed,rand_passes=50,pre_and_post=False),
        ), key=lambda x:len(x[0]))

    # Compress unless the compressed code fails
    if not (assume_passing or test_task(task_name, compressed)):
        compressed = preprocessed

    if player in task_sols and len(compressed) > task_sols[player]["size_compressed"]:
        too_long.append((path, len(compressed), task_sols[player]["size_compressed"], tasks[task_name]['best']))
        continue

    if player in task_sols and len(compressed) < task_sols[player]["size_compressed"]:
        improved.append((path, len(compressed), task_sols[player]["size_compressed"], tasks[task_name]['best']))

    # Update JSON
    tasks[task_name]["solutions"][player] = {
        "source" : base64.b64encode(src).decode('ASCII'),
        "size_uncompressed" : len(preprocessed),
        "compressed" : base64.b64encode(compressed).decode('ASCII'),
        "size_compressed" : len(compressed),
        **stats
    }

    # Update best
    improvement = tasks[task_name]["best"] - len(compressed)
    if improvement > 0:
        tasks[task_name]["best"] = len(compressed)
        total_save += improvement
        with open(as_path("compression_experiments", task_name), "wb") as c_file:
            comp_src = b""
            exec(compressed.replace(b"exec", b"comp_src="))
            c_file.write(comp_src)

        # Update gold
        if len(compressed) < tasks[task_name]["gold"]:
            tasks[task_name]["gold"] = len(compressed)

if any(improved):
    print(f"{len(improved)} TASK{'S' * (len(improved) != 1)} IMPROVED:")
    for path, current, prev, best in improved:
        print(f"\t{path} - current: {current}, prev: {prev}, prev_best: {best}")

# Exit if there are problems with any changed solutions
if any(failing) or any(too_long):
    if any(failing):
        print(f"{len(failing)} TASK{'S' * (len(failing) != 1)} FAILING:")
        for path in failing:
            print("\t" + path)
    if any(too_long):
        print(f"{len(too_long)} TASK{'S' * (len(too_long) != 1)} WORSE THAN PREVIOUS:")
        for path, current, prev, best in too_long:
            print(f"\t{path} - current: {current}, prev: {prev}, best: {best}")

# Update tasks.json
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# Show change data
total_score = max_size * task_count - sum(task_data['best'] for task_data in tasks.values())

print(f"Saved {total_save} bytes")
print(f"Score: {total_score}")