p=lambda i,s=0:[[~y%~(s:=y-s>>t&2)%4for y,t in zip(x,[0]+x)]for x in i]

## regex solution
import re;p=lambda i:eval(re.sub("(2, (., )?\\2*2)","*[3>>x for x in[\\1]]",str(i)))
p=lambda i,s=0:[[~y%~(s:=y*t!=4and s^y)%4for y,t in zip(x,[0]+x)]for x in i]
p=lambda i,s=0:[(t:=1)*[~y%~(s:=t*(t:=y)!=4and s^y)%4for y in x]for x in i]
p=lambda i,s=0:[(t:=1)*[~y%~(s:=(y&t|s)^(t:=y))%4for y in x]for x in i]