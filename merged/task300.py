p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))if max(range(1,10),key=sum(a,a).count)in b]

### ovs (130 bytes)
p=lambda g:max(c*(sum(map(bool,sum(a:=[[c*(c==q)for*v,q in zip(*g,r)if c in v]for r in g if c in r],[]))),a)for c in sum(g,[]))[1]
