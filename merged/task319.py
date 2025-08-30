# combined (392 vs 199 bytes for gold)
E=enumerate
def p(g):
 f=sum(g,[]);*r,b=sorted({*f},key=f.count);W,H=len(g[0]),len(g);T={C:{(i,j)for i,r in E(g)for j,v in E(r)if C==v}for C in r}
 for c in r:
  for l in r:
   if T[c]in({(i*2+q+a,j*2+Q+A)for i,j in T[l]for a in(0,1)for A in(0,1)if H>i*2+q+a>-1<j*2+Q+A<W}for q in range(-H*2,H*2)for Q in range(-W*2,W*2)):return[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]

### ovs (tied, 392 bytes)
E=enumerate
def p(g):
 f=sum(g,[]);*r,b=sorted({*f},key=f.count);W,H=len(g[0]),len(g);T={C:{(i,j)for i,r in E(g)for j,v in E(r)if C==v}for C in r}
 for c in r:
  for l in r:
   if T[c]in({(i*2+q+a,j*2+Q+A)for i,j in T[l]for a in(0,1)for A in(0,1)if H>i*2+q+a>-1<j*2+Q+A<W}for q in range(-H*2,H*2)for Q in range(-W*2,W*2)):return[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]
