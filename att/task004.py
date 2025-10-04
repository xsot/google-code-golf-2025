import re
p=lambda i:eval(re.sub(r"((.)(, \2)*), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))

##
import re;p=lambda i:eval(re.sub(r"((.)(, \2)*), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))
import re;p=lambda i:eval(re.sub(r"(((.), )\2*)0,?(?=.*\3.*].*\3)",r"0,\1",str(i)))
p=lambda a:[[b.pop(sum([-1,~b[::-1].index(m:=max(b))][:~sum(c)//~m]))]+b for b,c in zip(a,a[1:]+a)]
p=lambda a:[[b.pop(sum([-1,bytes(b).rfind(m:=max(b))][:~sum(c)//~m]))]+b for b,c in zip(a,a[1:]+a)]