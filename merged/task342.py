# joking (112 vs 110 bytes for gold)
import re;p=lambda i,k=3:-k*i or p(eval(re.sub("([1-9])((.{32})+?[0, ]+)8",r"0\2\1",str([*zip(*i)][::-1]))),k-1)

### combined (119 bytes)
p=lambda i,s=-1:[[y==8and[g for g in[*map(max,*i[:a]),*map(max,*i[a:])]if g%8][s:=s+1]for y in i[a]]for a in range(10)]
