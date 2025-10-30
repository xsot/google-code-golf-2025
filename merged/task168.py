# ovs (112 bytes, gold)
import re;p=lambda i:exec(r'i[::-1]=zip(*eval(re.sub(r"0(?=(.{35})+,( [^0]).{27}\2,\2)",r"\2",str(i))));'*4)or i

### joking (115 bytes)
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(r"0(?=(.{35})+,( [^0]).{27}\2,\2)",r"\2",str(p(i,k-1))))[::-1])]

##
import re
p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(r"0, (?=(.{35})+([^0], ).{26}\2\2)",r"\2",str(p(i,k-1))))[::-1])]

### combined (117 bytes)
import re
p=lambda i,k=39:-k*i or[*zip(*eval(re.sub(r"0((.{35})+, ([^0]).{28}\3, \3)",r"\3\1",str(p(i,k-1))))[::-1])]
