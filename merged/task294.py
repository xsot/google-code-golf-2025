# joking (70 bytes, gold)
import re;p=lambda m:eval(re.sub('(?<=5.{34})5(?=.{34}5)','2',str(m)))

## recursive version
p=lambda i,r=[[0]*10]*10,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or i>>all(w)

### xsot (76 bytes)
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))

### combined (76 bytes)
import re
p=lambda i:eval(re.sub("(?<=5.{28}5, )5(?=, 5.{28}5)","2",str(i)))
