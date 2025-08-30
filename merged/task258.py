# att (61 bytes, gold)
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))

### joking+mwi (tied, 61 bytes)
import re;p=lambda i:eval(re.sub("1, 0(?=, 1)","1,2",str(i)))

### xsot (62 bytes)
import re
p=lambda m:eval(re.sub("1, 0(?=, 1)","1, 2",str(m)))

### ovs (67 bytes)
p=lambda g:[[v|a+b&2for a,b,v in zip([0]+r,r[1:]+[0],r)]for r in g]
