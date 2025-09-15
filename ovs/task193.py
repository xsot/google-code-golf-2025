p=lambda m,*a:[[b*any(a)for*a,b in zip([0]+r,r[1:]+[0],r)]for*r,in zip(*a or p(m,*m))]

##

import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
