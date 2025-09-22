p=lambda i,k=-2:[i:=[r.pop()|4*(k==2)|7*((k:=K)==1)for K in i]for*r,in zip(*i*k or p(i,k+1))]

##

import re
p=lambda i:[i:=eval(re.sub('0(?=.{31}(2)|.{28}(1))',r'6^\1\2',str([*zip(*i[::-1])])))for _ in i][3]

E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]
