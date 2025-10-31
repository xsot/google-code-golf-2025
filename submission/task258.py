import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))