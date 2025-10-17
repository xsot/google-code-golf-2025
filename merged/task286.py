# joking (105 bytes, gold)
p=lambda i,k=39:-k*i or[[t:=y or sum({*sum(t%8*i,[])}-{t,8})for y in[8]+x][:0:-1]for*x,in zip(*p(i,k-1))]

## faster version
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or t%8and sum({*sum(i,[])}-{t,0,8})for y in x],*p(i,k-1)[::-1])]
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or([0,*{*sum(i,[])}-{y,t,8}]*2)[3]for y in x],*p(i,k-1)[::-1])]

### ovs (107 bytes)
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or sum({*sum(t%8*i,[])}-{t,8})for y in x],*p(i,k-1)[::-1])]

### combined (121 bytes)
p=lambda i,k=139:-k*i or[[z[1]or([0,*{*z,8}^{*sum(i,[])}]*2)[3]for z in zip([0,*x],x,[*x[1:],0])]for x in zip(*p(i,k-1))]

### xsot (134 bytes)
import re
p=lambda m,i=291:-i*m or p([*zip(*eval(re.sub("0(?=, ([^08]))",lambda x:s.strip(", 08[]()"+x[1])[0],s:=str(m))))][::-1],i-1)
