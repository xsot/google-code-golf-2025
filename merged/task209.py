# xsot (274 (417 unzipped) vs 273 bytes for gold)
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
