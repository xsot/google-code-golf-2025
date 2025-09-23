# zip fiddling
def p(g):
 t,t=max((len({*str(s:=[z[x:x+3]for z in g[y:y+3]])}),s)for y in range(len(g))for x in range(len(g[1])))
 for s in range(len(g[1])):
  for y in range(len(g)-s*3):
   for x in range(len(g[1])-s*3):
    for z in range(len(g[1])):
     t=*zip(*t[::-1]),
     for Y in range(s*3*all(g[y+Y][x+X]==t[Y//s][X//s]or g[y+Y][x+X]==g[1][-1]!=t[Y//s][X//s]==max({*t[1]}-{g[1][-1]})for Y in range(s*3)for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g