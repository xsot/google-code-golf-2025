import os
import shutil


def comp(path):
    new_lines = []
    for line in open(path):
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

for i in range(1, 401):
    fname = f"task{i:03}.py"

    # Collect all solutions for this task
    solutions = []

    for player_name, player_dir in players:
        path = os.path.join(player_dir, fname)
        if os.path.exists(path):
            code = comp(path)
            score = len(code.encode('utf-8'))
            solutions.append((score, player_name, path, code))

    # Skip if no solutions found
    if not solutions:
        continue

    # Sort by score (shortest first), then by player name for tie-breaking
    solutions.sort(key=lambda x: (x[0], x[1]))

    output_path = os.path.join(output_dir, fname)

    if len(solutions) == 1:
        # Only one solution exists, just copy it
        _, _, source_path, _ = solutions[0]
        shutil.copy(source_path, output_path)
    else:
        # Multiple solutions exist, merge them
        lines = []

        # Add the best solution first
        best_score, best_player, best_path, _ = solutions[0]
        with open(best_path) as f:
            lines.extend(f.readlines())

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

print("Merging complete!")
