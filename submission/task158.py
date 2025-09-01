def p(g):
 o=g[0][-1];s,t=max((len({*sum(a:=[R[x:x+3]for R in g[y:y+3]],[])}),a)for y in range(len(g))for x in range(len(g[0])))
 for s in(1,2,3):
  for y in range(len(g)+1-3*s):
   for x in range(len(g[0])+1-3*s):
    for z in'range'*2:
     t=(t,[*zip(*t)])[z<'r'][::-1]
     for Y in range(s*3*all((a:=g[y+Y][x+X])==(b:=t[Y//s][X//s])or(a==o)*(b==max({*t[1]}-{o}))for Y in range(s*3) for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g