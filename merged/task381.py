# ovs (86 vs 79 bytes for gold)
p=lambda i,a=8:[[-s+(s:=s+y)or(a%9>0<s<sum(x))*9for y in x]for x in i if[s:=0,a:=a+1]]

##

p=lambda i:i[:1]+[[-s+(s:=s+y)or(0<s<sum(x))*9for y in x]for x in i[1:9]if[s:=0]]+i[9:]

import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.*],)","*[9]*len([\\1]),",str(m)))

### joking (91 bytes)
p=lambda i,E=enumerate:[[y or(a%9>0<2in{*x[b:]}&{*x[:b]})*9for b,y in E(x)]for a,x in E(i)]

##
p=lambda i,r=range(10):[[(x:=i[a])[b]or(a%9>0<2in{*x[b:]}&{*x[:b]})*9for b in r]for a in r]
p=lambda i:i[:1]+[[x[b]or(2in{*x[b:]}&{*x[:b]})*9for b in range(10)]for x in i[1:-1]]+i[-1:]
p=lambda i:i[:1]+[(b:=0)or[y|((b:=b|x.pop(0))>y<2in x)*9for y in[*x]]for x in i[1:-1]]+i[-1:]

### xsot (93 bytes)
import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.{30})","*[9]*len([\\1]),",str(m)))

### combined (94 bytes)
import re
p=lambda i:eval(re.sub("(?<=.{30}2, )([0, ]+)(?=2.{30})","*[9]*len([\\1]),",str(i)))
