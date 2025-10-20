# joking (227 (290 unzipped) bytes, gold)
def p(g):
 for y in range(32):g=[[g[y][~x]+13*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%13|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

##
def p(g):
 for y in range(#[*range(32,40,4)]##):g=[[g[y][~x]+#[*range(10,50)]##*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%#[prev_vals[-1]]##|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

### ovs (235 (267 unzipped) bytes)
def p(g):
 for S in[{0,3}]*8:g=[[g[y][~x]+10*any({*r[-2%(30-x):31-x]}-S for r in g[y+y%~y:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%10|3*({*r[:10]}<=S)*(len(w:=[r[x]for r in g if{*r[:10]}<=S])>3!=S>={*w}or 3in r[x:])for x in range(30)]for r in g]
 return g

### mwi (268 (325 unzipped) bytes)
def p(g):
 g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in range(30)]for y in range(30)]
 for y in'y'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in range(30):
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]

### combined (273 (313 unzipped) bytes)
def p(g):
 R=range(30);g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in R]for y in R]
 for _ in'_'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in R:
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]
