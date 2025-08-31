# combined (121 vs 109 bytes for gold)
p=lambda i,k=139:-k*i or[[z[1]or([0,*{*z,8}^{*sum(i,[])}]*2)[3]for z in zip([0,*x],x,[*x[1:],0])]for x in zip(*p(i,k-1))]

### xsot (134 bytes)
import re
p=lambda m,i=291:-i*m or p([*zip(*eval(re.sub("0(?=, ([^08]))",lambda x:s.strip(", 08[]()"+x[1])[0],s:=str(m))))][::-1],i-1)
