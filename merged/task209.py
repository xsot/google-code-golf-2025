# joking (249 (387 unzipped) bytes, gold)
def p(g):
 G=g
 for s in G*4:G=[[*s]for s in zip(*G[-5:])if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s,r in enumerate(g):
  if[1for y,r in enumerate(g)for x,r in enumerate(s*r)for Y,r in enumerate(s*G*all(g in[0,((G+32*[[]])[(Y-y)//s]+32*[4])[(X-x)//s]]for Y,g in enumerate(g)for X,g in enumerate(g)))for X,r in enumerate(s*r)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g


## experimenting with more specific zip replacing
def p(g):
 G=g
 for s in G*4:G=[[*s]for s in zip(*G[#['~4','-5']#:])if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s,r in enumerate(g):
  if[#range(7)#for y,r in enumerate(g)for x,r in enumerate(s*r)for Y,r in enumerate(s*all(g in[0,((G+#range(20,60)#*[[]])[(Y-y)//s]+#[prev_vals[-1]]#*[4])[(X-x)//s]]for Y,g in enumerate(g)for X,g in enumerate(g))*G)for X,r in enumerate(s*r)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g

## parser
totals = {}
h = {}

def zip_replace(src,target,prev_vals = []):
 if "#" in src:
    z = re.search(r"#([^#]+)#", src)[1]
    a = 0
    if z not in totals: totals[z] = {}
    for t in eval(z):
        l = zip_replace(re.sub(r"#[^#]+#", str(t), src, 1), target, prev_vals + [t])
        a += l
        if t not in totals[z]: totals[z][t] = 0
        totals[z][t] += l
    return a
 else:
    zipped_src = compress_with_zlib(src.encode())
    if len(zipped_src) <= target:
        if len(zipped_src) not in h:
         print(len(zipped_src))
         h[len(zipped_src)] = src
         print(src)
        return 1
    return 0

### xsot (274 (417 unzipped) bytes)
def p(g):
 G=g[-5:]
 for s in range(20):G=[x for x in zip(*G)if{*x}-{b:=0,4}];g=[[*x]for x in zip(*g)if b|(b:=b^(4in x))]
 for s in range(20):
  for y in range(20):
   for x in range(20):
    if all(g[Y][X]in[0,4-4*(len(G)*s>Y-y>-1<X-x<len(G[0])*s)or G[(Y-y)//s][(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))):[0for Y in range(len(G)*s)for X in range(len(G[0])*s)for g[Y+y][X+x]in[G[Y//s][X//s]]];return g

### mwi (289 (429 unzipped) bytes)
def p(g):
 G=g[-5:]
 for s in[()]*4:G=[x for x in zip(*G[::-1])if{*x}-{0,4}];g=[[*x]for x in zip(*g[::-1])if 4in(s:=s+x)]
 for s in[2,3,4]:
  for y in range(20):
   for x in range(20):
    if all(g[Y][X]in[0,4-4*(y<=Y<y+len(G)*s>0<x<=X<x+len(G[0])*s)or G[(Y-y)//s][(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))):
     for Y in range(len(G)*s):
      for X in range(len(G[0])*s):g[Y+y][X+x]=G[Y//s][X//s]
     return g

### combined (297 (406 unzipped) bytes)
def p(g):
 R=range;G=g[-5:]
 for s in[()]*4:G=[x for x in zip(*G[::-1])if{*x}-{0,4}];g=[[*x]for x in zip(*g[::-1])if 4in(s:=s+x)]
 for s in[2,3,4]:
  H,W=len(G)*s,len(G[0])*s
  for y in R(20):
   for x in R(20):
    if all(g[Y][X]in[0,4-4*(y<=Y<y+H>0<x<=X<x+W)or G[(Y-y)//s][(X-x)//s]]for Y in R(len(g))for X in R(len(g[0]))):
     for Y in R(H):
      for X in R(W):g[Y+y][X+x]=G[Y//s][X//s]
     return g
