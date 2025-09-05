# xsot (95 vs 2500 bytes for gold)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]

### combined (tied, 95 bytes)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]
