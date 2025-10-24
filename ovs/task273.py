p=lambda a,*A,d=0:[[c^(2%-~c|(d:=2&d-c%3))for c in b]for b in zip(*A or p(a,*a))]

##
p=lambda g,q=0:g and[max(g[:1]+[[2&(q:=q^v)>>v+g.count(r)for v in r]for r in g])]+p(g[1:])
