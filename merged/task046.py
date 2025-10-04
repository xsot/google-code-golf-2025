# joking (169 vs 168 bytes for gold)
p=lambda i,n=0,Z=zip:[*Z(*[[y%~y&max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]

##
p=lambda i,n=0,Z=zip:[*Z(*[[y and max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]

### combined (176 bytes)
p=lambda i,n=0:[*zip(*[[y and max({*p,*x,*q}-{5})for y in x[n%3:]+x[:n%3]]for*x,p,q in zip(*i,[[],*zip(*i)],[*zip(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]
