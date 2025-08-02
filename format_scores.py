prev = 0
for line in open(0):
  score, task = line.split();
  task = int(task[4:7])
  for _ in range(task-prev-1): print()
  print(score)
  prev = task