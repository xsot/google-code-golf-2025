# joking (88 vs 75 bytes for gold)
# this is clearly not the right approach lol
p=lambda i,n=2,*t:t*(~n%2*6>len(t))or p(i,n+1,*[x for x in zip(*n%2*t or i)if n//2in x])

##
p=lambda i,n=1:(len(l:=(f:=lambda g:[x for x in zip(*g)if n in x])(f(i)))<6)*l or p(i,n+1)

### ovs (93 bytes)
p=lambda i,k=99,*r:-k*i or p([*zip(*i[~(a:={*sum(i,w:=i[-1]),*r}>{*w,*r})::-1])],k-1,*r,*a*w)

##
p=lambda g:min([(h:=lambda g,k=-99:k*g or h([*zip(*g[C not in g[0]:][::-1])],k+1))(g)for C in{*sum(g,[])}],key=len)

### mwi (98 bytes)
p=lambda i:max(l for n in range(10)if len(l:=(f:=lambda g:[x for x in zip(*g)if n in x])(f(i)))<6)

### combined (106 bytes)
p=lambda i:[l for n in{*sum(i,[])}if len(l:=[[y[0]for y in zip(x,*i)if n in y]for x in i if n in x])<6][0]
