def p(g):
 e=enumerate;C=[]
 for c in[[[c for c in r[:x+1]]for r in g[:y+1]]for y,r in e(g)for x,c in e(r)if c==r[x-1]==g[y-1][x]>0]:
  for _ in'--':
   c=[*zip(*c)]
   while any(c[-1][-1]^r[-1]for r in c):c=c[1:]
  C+=[[sum(a:=[c for r in c[1:-1]for c in r[1:-1]]),[[c and max([*a,0])for c in r]for r in c]]]
 return max(C)[1]