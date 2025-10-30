p=lambda a,n=91:-n*a or p([[[min(b+c,key=c.count)for*c,in a],A:=b][n>0]for*b,in zip(*a)][any(b'%c'%x*6in bytes(A)for x in A)-2::-1],n-1)

##
p=lambda g:max([[min(w:=r+c,key=w.count)for*c,in zip(*S)]for r in S]for A in range(len(g.pop(0))-6)if(s:=lambda w:len({*sum([r[A:A+6]for r in g[:6]],w[:6])})<=2)for S in[[[v for v,*c in zip(r,*g)if s(c)]for r in g if s(r[A:])]])or p(g)
