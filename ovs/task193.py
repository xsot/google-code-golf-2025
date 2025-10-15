*r,p='0'*25,lambda i,*w:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(w.count(i)>1)*i

##

import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
