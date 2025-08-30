# combined (108 vs 96 bytes for gold)
import re;p=lambda i:eval(re.sub(r"(?<!1, )1, ((0, )+)1(?!, 1)",r"1,*[len([\1])%2*5+2]*len([\1]),1",str(i)))

### ovs (142 bytes)
def p(g):
 for r in g:
  I=0
  for i,c in enumerate(r):
   if c<1==r[i-1]!=(r+[0])[i-2]:I^=1;j=i
   if I>c:r[i]=2|r[j:].index(1)%2*5
 return g
