import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(f'(?<={(b:=max(sum(a,[]),key=bool))}, )([^0{b}])(.*{b}.{{34}})0',r'0\2\1',str(p(a,n+1)[::-1]))))]