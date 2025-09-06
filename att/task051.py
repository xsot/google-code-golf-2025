import re
p=lambda a,n=-63:n*a or[*zip(*eval(re.sub(r'0, ([^0])((, (?!0|\1).)+[0, ]*)0',r'0,\1\2\1',str(p(a,n+1)))))][::-1]