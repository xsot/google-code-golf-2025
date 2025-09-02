# combined (251 vs 208 bytes for gold)
import re
p=lambda i,k=3:-k*[[(y!=0)*max({*(g:=sum(i,i[0]))}-{y or min(g,key=g.count),''})for y in x]for x in i]or p(eval(re.sub(r"(([1-9]), ((?!\2)(\d), (\4, \2, 0|\2)|\2, \2(, \2, 0)?), (0|''))",f"*[x or''for x in[\\1]]",str([*zip(*i[::-1])]))),k-1)
