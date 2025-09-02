def p(g):
 e=enumerate;w=[(y,x,s)for y,r in e(g[:-2])for x,c in e(r[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0;u=[[y[0]for y in zip(x,*g)if any(y)]for x in g if any(x)]
 for y,x,s in w[::-1]:
  for p in'p in':
   for Y,R in e(u):
    for X,p in e(R):
     for n,j in e(s*all(((u*2)[n+Y]*2)[m+X]==2*(2!=r)for n,j in e(s)for m,r in e(j))):u[n+Y][X:X+3]=j;s=[]
   s=*zip(*s[::-1]),
 return u