p=lambda i,s=9:[[-s+(s:=s+y)or(1<s<sum(x))*9for y in x]*(s:=1)for x in i[:9]]+i[9:]

##
import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.{30})","*[9]*len([\\1]),",str(m)))