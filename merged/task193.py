# ovs (77 bytes, gold)
*r,p='0'*25,lambda i,*w:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(w.count(i)>1)*i

##

import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))

### joking (78 bytes)
p=lambda i,*w,r=['0'*25]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(w.count(i)>1)*i

##
p=lambda i,r=[[0]*25]*25,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or(sum(w)>i)*i

### xsot (98 bytes)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))

##
import re
p=lambda m,i=1:-i*m or p([*zip(*eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {m} ")))],i-1)

### combined (98 bytes)
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
