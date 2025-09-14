# ovs (260 (313 unzipped) vs 259 bytes for gold)
def p(g):s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count);b=[b,B][any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g)];[0for y,r in enumerate(eval(str(g)))for x,c in enumerate(r)for z,s in enumerate(g)for Y in(-z,z)for X in(-z,z)if c in{k,K}!=len(g)>Y+y>-1<X+x<len(g[0])for g[Y+y][X+x]in[[K,k][g[Y+y][X+x]in(b,k)]]];return g

### mwi (288 (343 unzipped) bytes)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,s in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g

### combined (289 (343 unzipped) bytes)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,_ in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g
