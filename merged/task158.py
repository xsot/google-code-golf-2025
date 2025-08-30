# combined (441 vs 306 bytes for gold)
def p(g):
 o=g[0][-1];e=enumerate;_,t=max((len({*sum(a:=[R[x:x+3]for R in g[y:y+3]],[])}),a)for y,r in e(g)for x,c in e(r))
 for s in[1,2,3]:
  for y,r in e(g[:1-3*s]):
   for x,c in e(r[:1-3*s]):
    for z in'range'*2:
     t=[t,[*zip(*t)]][z<'r'][::-1];R=range(s*3)
     if all((a:=g[y+Y][x+X])==(b:=t[Y//s][X//s])or(a==o)*(b==max({*t[1]}-{o}))for Y in R for X in R):
      for Y in R:
       for X in R:g[y+Y][x+X]=t[Y//s][X//s]
 return g
