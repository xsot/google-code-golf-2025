import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'([^0])((, (?!\1|0).).*0\3.{28})0',r'0\2\1',str(p(a,n+1)[::-1]))))]