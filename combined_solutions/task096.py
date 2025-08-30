def p(g):
 r=sum(g,W:=[]);*u,b=sorted({*r},key=r.count)
 for z in u:
  w=[[b,z][c==z]for c in max(g+[*zip(*g)],key=lambda r:r.count(z))]
  for _ in g:w=w[w.index(z):][::-1]
  if(w+[b]).index(b)<(w[::-1]+[b]).index(b):w=w[::-1]
  while w!=w[::-1]or len(w)==2:w+=[z]
  W=sorted(W+[w],key=len)[::-1]
 w=[[b]*len(W[0])]*len(W[0])
 for n,q in enumerate(W):
  for _ in g:w=[*map(list,zip(*w[::-1]))];w[n][n:-n]=q
 return w