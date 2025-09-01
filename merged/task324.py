# mwi (289 (343 unzipped) bytes, gold)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,s in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g

### combined (291 (343 unzipped) bytes)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,_ in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g
