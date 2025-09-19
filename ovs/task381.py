p=lambda i,a=8:[[-s+(s:=s+y)or(a%9>0<s<sum(x))*9for y in x]for x in i if[s:=0,a:=a+1]]

##

p=lambda i:i[:1]+[[-s+(s:=s+y)or(0<s<sum(x))*9for y in x]for x in i[1:9]if[s:=0]]+i[9:]

import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.*],)","*[9]*len([\\1]),",str(m)))
