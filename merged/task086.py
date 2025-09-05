# joking (172 bytes, gold)

p=lambda i,k=7,s=0:-k*i or[[k<7and(-((s:=(y>0)*min(s-1,-1)or~-max(-s,s,1))>1)or y)or(z:=[*{}.fromkeys(sum(i,[]))])[y and~(y!=z[1])]for y in x]for x in zip(*p(i,k-1)[::-1])]

##alt
p=lambda i,k=7,s=0:-k*i or p([[k and(-((s:=(y>0)*min(s-1,-1)or~-max(-s,s,1))>1)or y)or(z:=[*{}.fromkeys(sum(i,[]))])[y and~(y!=z[2])]for y in x]for x in zip(*i[::-1])],k-1)

### xsot (248 bytes)
import re
p=lambda i,k=3:-k*[[(y!=0)*max({*(g:=sum(i,i[0]))}-{y or min(g,key=g.count),''})for y in x]for x in i]or p(eval(re.sub(r"(([^0]), ((?!\2)(\d, )(\4\2, 0|\2)|\2, \2(, \2, 0)?), (0|''))",f"*[x or''for x in[\\1]]",str([*zip(*i[::-1])]))),k-1)

### combined (251 bytes)
import re
p=lambda i,k=3:-k*[[(y!=0)*max({*(g:=sum(i,i[0]))}-{y or min(g,key=g.count),''})for y in x]for x in i]or p(eval(re.sub(r"(([1-9]), ((?!\2)(\d), (\4, \2, 0|\2)|\2, \2(, \2, 0)?), (0|''))",f"*[x or''for x in[\\1]]",str([*zip(*i[::-1])]))),k-1)
