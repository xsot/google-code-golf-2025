# xsot (114 vs 84 bytes for gold)
import re
p=lambda m,i=3:-i*m or p([*zip(*eval(re.sub(r"0(?=..2|.{%d}2)"%(len(m[0]*3)+4),'1',str(m)))[::-1])],i-1)

###
import re
p=lambda m,i=1:-i*m or p(eval(re.sub(r"0(?=..2|(...){,2}.{%d}2)|(?<=2..)0"%(len(m[0]*3)-2),'1',str(m)))[::-1],i-1)
