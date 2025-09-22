# ovs (92 bytes, gold)
p=lambda i,k=-3:i*k or[i:=[r.pop()|4*(k==2)|7*((k:=K)==1)for K in i]for*r,in zip(*p(i,k+1))]

##

import re
p=lambda i:[i:=eval(re.sub('0(?=.{31}(2)|.{28}(1))',r'6^\1\2',str([*zip(*i[::-1])])))for _ in i][3]

E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]

### joking (104 bytes)
import re;p=lambda i:[i:=eval(re.sub("0(?=.{28,30}( 2|1))",r"\1^6",str([*zip(*i[::-1])])))for _ in i][7]

##
p=eval(f"lambda i:[i:=[[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7{'for %s in range(9)]'*3%(*'ba_',)}[3]")

## experiments with using true/false
p=lambda i:[i:=[[s!=2and~-len(str(s))|y|(s==1)*7for y,s in zip(x,[0,*x])]for x in zip(*i[::-1])]for _ in i][7]
p=lambda i:[i:=[[y==1or s!=2and y|6-len(str(s))^5for y,s in zip(x,[0,*x])]for x in zip(*i[::-1])]for _ in i][7]

### mwi (106 bytes)
p=lambda i,r=range(9):[i:=[[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r]for _ in i][3]

### combined (107 bytes)
p=lambda i,k=3,r=range(9):-k*i or p([[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r],k-1)

### att (111 bytes)
p=eval('lambda a:[[(b:=sum(a,()))[4]or(1in b[1::2])*7|4*(2in b[::2])'+'for*a,in map(zip,a[8:]+a,a,a[1:]+a)]'*2)
