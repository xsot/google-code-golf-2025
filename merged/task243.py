# att (79 bytes, gold)
p=lambda a,n=-79:a*n or[*zip(*eval(str(p(a,n+1)[::-1]).replace('1, 0','1,1')))]

### combined (tied, 79 bytes)
p=lambda i,k=79:-k*i or[*zip(*eval(str(p(i,k-1)[::-1]).replace("1, 0","1,1")))]

### ovs (89 bytes)
p=lambda g:[g:=[[v<q<2or(q:=v)for v in r]for*r,in zip(*g)if[q:=2]][::-1]for _ in g*4][-1]

### xsot (99 bytes)
import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)","1",'%len(m*3)*98+f'"{m}"'+')[::-1]'*98))
##
import re
p=lambda m:eval(eval('(m:=re.sub("0(?=..1|..{%d}1)","1",str(m))[::-1]),'%len(m*3)*98)[-1])
import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)","1",'%len(m*3)*98+f'"{m}"'+')[::-1]'*98))
import re
p=lambda m:eval(eval('re.sub("0(?=..1|..{%d}1)"%len(m*3),"1",'*98+f'"{m}"'+')[::-1]'*98))
import re
p=lambda m:eval(eval('(s:="%r")'%m+'and(s:=re.sub("0(?=..1|..{%d}1)"%len(m*3),"1",s)[::-1])'*98))
