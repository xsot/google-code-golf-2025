import re
p=lambda m,i=3:-i*m or p([*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(m))))][::-1],i-1)