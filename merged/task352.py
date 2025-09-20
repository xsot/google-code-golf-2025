# joking (84 bytes, gold)
p=lambda i:[*eval("map(lambda*x,t=0:[max(0<t<3,t:=y)for y in x][::-1],*"*4+"i))))")]

##
p=lambda*i:i[0]*0!=0and[*map(p,*sum([[x,x[1:]+x[-1:],x[:1]+x]for x in i],[]))]or i[0]or 2in i

### att (86 bytes)
p=lambda i,k=3:-k*i or[*map(lambda*x,t=0:[max(0<t<3,t:=y)for y in x],*p(i,k-1)[::-1])]

### combined (90 bytes)
p=lambda i,k=3:-k*i or[[y or 6>>t&9for y,t in zip(x,[0,*x])]for x in zip(*p(i,k-1)[::-1])]

### xsot (114 bytes)
import re
p=lambda m,i=3:-i*m or p([*zip(*eval(re.sub(r"0(?=..2|.{%d}2)"%(len(m[0]*3)+4),'1',str(m)))[::-1])],i-1)

###
import re
p=lambda m,i=1:-i*m or p(eval(re.sub(r"0(?=..2|(...){,2}.{%d}2)|(?<=2..)0"%(len(m[0]*3)-2),'1',str(m)))[::-1],i-1)
