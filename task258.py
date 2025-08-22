import re
p=lambda m:eval(re.sub("1, 0(?=, 1)","1, 2",str(m)))