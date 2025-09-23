def p(g):
 G=g[-5:]
 for s in range(20):G=[x for x in zip(*G)if{*x}-{b:=0,4}];g=[[*x]for x in zip(*g)if b|(b:=b^(4in x))]
 for s in range(20):
  for y in range(20):
   for x in range(20):
    if all(g[Y][X]in[0,4-4*(len(G)*s>Y-y>-1<X-x<len(G[0])*s)or G[(Y-y)//s][(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))):[0for Y in range(len(G)*s)for X in range(len(G[0])*s)for g[Y+y][X+x]in[G[Y//s][X//s]]];return g