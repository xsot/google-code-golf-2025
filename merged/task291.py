# xsot (59 bytes, gold)
p=lambda m,k=1:[*{r.count(k)for r in m},[k]][3:]or p(m,k+1)

##
import re
p=lambda m:[[int(re.findall(r"([^0]), 0[^]]*\1",str(m))[0])]]
##
import re
p=lambda m:[[int(re.search(r"([^0])(?=, 0[^]]*\1)",str(m))[0])]]

### combined (62 bytes)
p=lambda i,n=1:len({x.count(n)for x in i})//3*[[n]]or p(i,n+1)

### att (69 bytes)
p=lambda a:max([[c]]for c in sum(a,a)if[*{b.count(c)for b in a}][2:])
