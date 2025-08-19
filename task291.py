import re
p=lambda m:[[int(re.findall(r"([^0]), 0[^]]*\1",str(m))[0])]]
##
import re
p=lambda m:[[int(re.search(r"([^0])(?=, 0[^]]*\1)",str(m))[0])]]