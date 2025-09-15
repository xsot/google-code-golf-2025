# ovs (102 vs 93 bytes for gold)
import re;p=lambda i:eval(re.sub("(?<!1, )1,([^1]+)1(?!, 1)",r"1,*[(s:=len([\1]))%2*5+2]*s,1",str(i)))

##

def p(g):
 for r in g:
  I=0
  for i,c in enumerate(r):
   if c<1==r[i-1]!=(r+[0])[i-2]:I^=1;j=i
   if I>c:r[i]=2|r[j:].index(1)%2*5
 return g

### combined (108 bytes)
import re;p=lambda i:eval(re.sub(r"(?<!1, )1, ((0, )+)1(?!, 1)",r"1,*[len([\1])%2*5+2]*len([\1]),1",str(i)))
