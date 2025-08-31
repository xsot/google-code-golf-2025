# joking+mwi (127 vs 97 bytes for gold)
import re;p=lambda i:[eval(re.sub(r"((\d)(, \2)*)",r"*map(int.__mul__,x[h.index(1):],[\1])",str(h:=[*map(max,*i)])))for x in i]

### ovs (132 bytes)
E=enumerate
p=lambda g:[[sum(c for c in(1,2,4)if(g*2)[i+(F:=sum(g,[]).index)(c)//10-F(1)//10][j]==c)for j,_ in E(r)]for i,r in E(g)]
