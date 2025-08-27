p=lambda a:max([[c]]for c in sum(a,a)if[*{b.count(c)for b in a}][2:])

### xsot (71 bytes)
import re
p=lambda m:[[int(re.findall(r"([^0]), 0[^]]*\1",str(m))[0])]]
##
import re
p=lambda m:[[int(re.search(r"([^0])(?=, 0[^]]*\1)",str(m))[0])]]
