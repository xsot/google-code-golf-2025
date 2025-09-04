import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'([^0]), (?!\1|0)(.)(.*\1.{34})0',r'\1,0\3\2',str(p(a,n+1)[::-1]))))]