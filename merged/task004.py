# ovs (73 bytes, gold)
import re;p=lambda i:eval(re.sub(r"(.),(?=.*\1.*0, \1)",r"0,\1|",str(i)))

##
p=lambda g,s=0:g and[[[v,j][{*g[0]}<={*sum(g[min(2,s:=s+(v>0)):],[])}]for j,v in zip([0]+g[0],g[0])]]+p(g[1:])

### att (83 bytes)
import re
p=lambda i:eval(re.sub(r"((.)(, \2)*), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))

##
import re;p=lambda i:eval(re.sub(r"((.)(, \2)*), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))
import re;p=lambda i:eval(re.sub(r"(((.), )\2*)0,?(?=.*\3.*].*\3)",r"0,\1",str(i)))
p=lambda a:[[b.pop(sum([-1,~b[::-1].index(m:=max(b))][:~sum(c)//~m]))]+b for b,c in zip(a,a[1:]+a)]
p=lambda a:[[b.pop(sum([-1,bytes(b).rfind(m:=max(b))][:~sum(c)//~m]))]+b for b,c in zip(a,a[1:]+a)]

### joking (83 bytes)
import re
p=lambda i:eval(re.sub(r"(([1-9]).*?), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))

### combined (86 bytes)
import re
p=lambda i:eval(re.sub(r"(([^0])(, .)+), 0(?=.*\2.*\].*\2)",r"0,\1",str(i)))
