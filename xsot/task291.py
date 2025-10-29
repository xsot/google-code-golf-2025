p=lambda m,k=1:[*{r.count(k)for r in m},[k]][3:]or p(m,k+1)

##
import re
p=lambda m:[[int(re.findall(r"([^0]), 0[^]]*\1",str(m))[0])]]
##
import re
p=lambda m:[[int(re.search(r"([^0])(?=, 0[^]]*\1)",str(m))[0])]]