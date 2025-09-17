# xsot (76 vs 70 bytes for gold)
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))

### combined (tied, 76 bytes)
import re
p=lambda i:eval(re.sub("(?<=5.{28}5, )5(?=, 5.{28}5)","2",str(i)))

### joking (77 bytes)
p=lambda i,r=[[0]*10]*10,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or i>>all(w)
