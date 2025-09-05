# combined (86 vs 80 bytes for gold)
import re
p=lambda i:eval(re.sub(r"(([^0])(, .)+), 0(?=.*\2.*\].*\2)",r"0,\1",str(i)))

### ovs (110 bytes)
p=lambda g,s=0:g and[[[v,j][{*g[0]}<={*sum(g[min(2,s:=s+(v>0)):],[])}]for j,v in zip([0]+g[0],g[0])]]+p(g[1:])
