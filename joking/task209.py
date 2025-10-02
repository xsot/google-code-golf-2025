def p(g):
 G=g[-5:]
 for s in range(1,53):G=[[*s]for s in zip(*G)if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s in range(1,53):
  for y in range(1,53):
   for x in range(1,53):
    if[0for Y in range(len(G)*s*all(g[Y][X]in[0,((G+[[]]*53)[(Y-y)//s]+[4]*53)[(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))))for X in range(len(G[0])*s)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g


## faster for +2b
def p(g):
 G=g[-5:]
 for s in g*4:G=[[*s]for s in zip(*G)if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s in range(1,20):
  for y in range(1,20):
   for x in range(1,20):
    if[0for Y in range(len(G)*s*all(g[Y][X]in[0,((G+[[]]*20)[(Y-y)//s]+[4]*20)[(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))))for X in range(len(G[0])*s)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g