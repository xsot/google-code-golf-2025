import re
p=lambda m,i=1:-i*m or p([*map(list,zip(*eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {m} "))))],i-1)