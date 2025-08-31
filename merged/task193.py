# xsot (98 vs 85 bytes for gold)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))

##
import re
p=lambda m,i=1:-i*m or p([*zip(*eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {m} ")))],i-1)

### combined (tied, 98 bytes)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
