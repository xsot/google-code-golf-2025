new_lines = []
for line in open(0):
    if line.startswith('#'):
        break
    line = line.rstrip()
    if line:
        new_lines.append(line)
print(end='\n'.join(new_lines))