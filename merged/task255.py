# ovs (244 (276 unzipped) vs 243 bytes for gold)
def p(g):
 for S in[{0,3}]*8:g=[[r[~x]+10*any({*s[-2%(30-x):31-x]}-S for s in g[y+y%~y:y+2])for y,r in enumerate(g)]for x,_ in enumerate(g)];g=[[v%10|3*({*r[:10]}<=S)*(len(w:=[r[x]for r in g if{*r[:10]}<=S])>3!=S>={*w}or 3in r[x:])for x,v in enumerate(r)]for r in g]
 return g

### mwi (269 (325 unzipped) bytes)
def p(g):
 g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in range(30)]for y in range(30)]
 for y in'y'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in range(30):
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]

### combined (274 (313 unzipped) bytes)
def p(g):
 R=range(30);g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in R]for y in R]
 for _ in'_'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in R:
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]
