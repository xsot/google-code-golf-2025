# ovs (86 vs 81 bytes for gold)
p=lambda m,*a:[[b*any(a)for*a,b in zip([0]+r,r[1:]+[0],r)]for*r,in zip(*a or p(m,*m))]

##

import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))

### xsot (98 bytes)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))

##
import re
p=lambda m,i=1:-i*m or p([*zip(*eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {m} ")))],i-1)

### combined (98 bytes)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
