# joking+mwi (286 (327 unzipped) vs 250 bytes for gold)
def p(g,k=3,v=range):
 l=v(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*_,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*v(E+2,F-1),F+A-C-2,E-A+C+2),v(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### ovs (341 bytes)
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
