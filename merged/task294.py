# xsot (76 vs 2500 bytes for gold)
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))

### combined (tied, 76 bytes)
import re
p=lambda i:eval(re.sub("(?<=5.{28}5, )5(?=, 5.{28}5)","2",str(i)))
