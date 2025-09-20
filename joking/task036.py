# this is clearly not the right approach lol
p=lambda i,n=2,*t:t*(~n%2*6>len(t))or p(i,n+1,*[x for x in zip(*n%2*t or i)if n//2in x])

##
p=lambda i,n=1:(len(l:=(f:=lambda g:[x for x in zip(*g)if n in x])(f(i)))<6)*l or p(i,n+1)