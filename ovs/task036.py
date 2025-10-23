p=lambda i,n=2,*t:t*(t==t[n%2:5])or p(i,n+1,*[x for x in zip(*n%2*t or i)if n//2in x])

##
p=lambda i,n=1,w=0,*t:t*(t==t[w:5])or p(i,n+w,w^1,*[x for x in zip(*w*t or i)if n in x])
p=lambda i,k=99,*r:-k*i or p([*zip(*i[~(a:={*sum(i,w:=i[-1]),*r}>{*w,*r})::-1])],k-1,*r,*a*w)
p=lambda g:min([(h:=lambda g,k=-99:k*g or h([*zip(*g[C not in g[0]:][::-1])],k+1))(g)for C in{*sum(g,[])}],key=len)
