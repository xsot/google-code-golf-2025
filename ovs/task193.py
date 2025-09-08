import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
