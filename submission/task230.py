import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=.{%d}0, 5.{%d}5)"%((len(m)*3+1,)*2),"3421"[i],str(p(m,i-1)[::-1]))))]