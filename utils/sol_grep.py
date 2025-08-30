import re
for n in range(1,401):
 path = "submission_passing_\\task%03d.py"%n
 with open(path, "r") as file:
  src = file.read()
 if re.search(r"set",src):print(n,src)