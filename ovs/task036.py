p=lambda i,k=99,*r:-k*i or p([*zip(*i[~(a:={*sum(i,w:=i[-1]),*r}>{*w,*r})::-1])],k-1,*r,*a*w)

##
p=lambda g:min([(h:=lambda g,k=-99:k*g or h([*zip(*g[C not in g[0]:][::-1])],k+1))(g)for C in{*sum(g,[])}],key=len)
