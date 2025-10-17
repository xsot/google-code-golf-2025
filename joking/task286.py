p=lambda i,k=39:-k*i or[[t:=y or sum({*sum(t%8*i,[])}-{t,8})for y in[8]+x][:0:-1]for*x,in zip(*p(i,k-1))]

## faster version
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or t%8and sum({*sum(i,[])}-{t,0,8})for y in x],*p(i,k-1)[::-1])]
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or([0,*{*sum(i,[])}-{y,t,8}]*2)[3]for y in x],*p(i,k-1)[::-1])]