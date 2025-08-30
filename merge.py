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


# Configuration: add player directories here
players = [
    ('xsot', 'xsot/'),
    ('ovs', 'ovs/'),
    ('att', 'att/')
]

# Output directory
output_dir = 'merged/'

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
