# mwi (132 vs 127 bytes for gold)
import re;p=lambda i:[i:=eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0,",r"\1\2\4\3,0,\2+",str([*zip(*i[::-1])])))for _ in i][7]

### joking (133 bytes)
import re;p=lambda i,k=7:-k*i or p(eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0,",r"\1\2\4\3,0,\2+",str([*zip(*i[::-1])]))),k-1)

##
import re;p=lambda i,k=7:-k*i or p(eval(re.sub("(?<=([^0]).{37}([^0]), )0(, 0.{31})0, 0, 0",r"\1\3\2,0,\1",str([*zip(*i[::-1])]))),k-1)
import re;p=lambda i,k=7:-k*i or p(eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0, 0",r"\1\2\4\3,0,\2",str([*zip(*i[::-1])]))),k-1)

### ovs (169 bytes)
E=enumerate
p=lambda g:[[v or max({*zip(b'\0',[v]+sorted(f:=sum(g,[]),key=f.count))}&{((I//12-i)**2+(I%12-j)**2,V)for I,V in E(f)})[1]for j,v in E(r)]for i,r in E(g)]

### combined (169 bytes)
E=enumerate
p=lambda g:[[v or max({*zip(b'\0',[v]+sorted(f:=sum(g,[]),key=f.count))}&{((I//12-i)**2+(I%12-j)**2,V)for I,V in E(f)})[1]for j,v in E(r)]for i,r in E(g)]
