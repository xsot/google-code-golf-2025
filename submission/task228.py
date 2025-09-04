import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'0(.{34}([^0]).*)(.)(?=, \2.*0, \2)',r'\3\1 0',str(p(a,n+1)[::-1]))))]