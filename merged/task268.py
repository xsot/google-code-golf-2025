E=enumerate
def p(g):
 for _ in[G:=[*g]]*4:
  for v in g,G:v[:]=map(list,zip(*v[::-1]))
  for i,r in E(G):
   for j,v in E(r):
    for D in(-1,1,0)*(v<max(r)<sum(r[j:])&sum(r[:j])):
     for J in[j,j-1,j+1,j][[i<G.index(max(G)),4>>4*r[j+D]][D]or 3:]:
      I=i-(D^J==j)
      while-1<(I:=I+1)<len(g)>(J:=J+D)>-1<G[I][J]<1:g[I][J]=4
 return g