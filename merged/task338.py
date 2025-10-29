# xsot (65 vs 64 bytes for gold)
p=lambda i:[(t:=0)or[(i:=t**y==i)*3>>(t:=y)for y in x]for x in i]

##
p=lambda i,s=0:[(t:=1)*[(s:=t<y-s&6)*3>>(t:=y)for y in x]for x in i]

### joking (69 bytes)
p=lambda i,s=0:[(t:=0)or[(s:=t<y-s&6)*3>>(t:=y)for y in x]for x in i]

## regex solution
import re;p=lambda i:eval(re.sub("(2, (., )?\\2*2)","*[3>>x for x in[\\1]]",str(i)))
p=lambda i,s=0:[[~y%~(s:=y*t!=4and s^y)%4for y,t in zip(x,[0]+x)]for x in i]
p=lambda i,s=0:[(t:=1)*[~y%~(s:=t*(t:=y)!=4and s^y)%4for y in x]for x in i]
p=lambda i,s=0:[(t:=1)*[~y%~(s:=(y&t|s)^(t:=y))%4for y in x]for x in i]
p=lambda i,s=0:[[~y%~(s:=y-s>>t&2)%4for y,t in zip(x,[0]+x)]for x in i]

### att (104 bytes)
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]

### combined (104 bytes)
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]
