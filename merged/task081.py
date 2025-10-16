# joking (83 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or i or(8in w[:2])*(8in w[2:])

##
p=lambda i,*w:i or any(w[:2])*any(w[2:])if w[3:]else[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or i or any(w[:2])*any(w[2:])
p=lambda i,*w:i or(8in w[:2])*(8in r)if(r:=w[2:])else[*map(p,i,[i]+i,i[1:]+[i],*w)]

### xsot (95 bytes)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]

### combined (95 bytes)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]
