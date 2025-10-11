p=lambda i,n=0,Z=zip:[*Z(*[[y%~y&max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]

##
p=lambda i,n=0,Z=zip:[*Z(*[[y and max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]
p=lambda n,*i:[[y%~y&max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for x,p,q in zip(i,((),)+i,i[1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0]or[*zip(*p(0,*zip(*n),[5]))]
p=lambda n,*i:[[y%~y&max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for x,p,q in zip(i[1:],i,i[2:])if any(x)or[n:=n-[*p,5].index(5)+q.index(5)]*0]or[*zip(*p(0,i,*zip(*n),[5]))]