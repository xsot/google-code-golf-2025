# ovs (92 vs 79 bytes for gold)
import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.*],)","*[9]*len([\\1]),",str(m)))

### xsot (93 bytes)
import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.{30})","*[9]*len([\\1]),",str(m)))

### combined (94 bytes)
import re
p=lambda i:eval(re.sub("(?<=.{30}2, )([0, ]+)(?=2.{30})","*[9]*len([\\1]),",str(i)))
