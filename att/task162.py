import re
p=lambda i:eval(eval('re.sub("0, 0, 0(.{55})?"*3,"*(1,)*3\%d"*3%(1,2,3),'*2+f'"{i}"))'))