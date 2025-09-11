# joking (238 (253 unzipped) vs 239 bytes for gold)
def p(g):
 l=range(len(g));(J,E),*B,(C,F)=[[A,D]for A in l for D in l if g[A][D]]
 if g[C][F-2]<1:
  for A in l[J+1:]:
   for D in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]:g[A][D]=4
  return g
 return[*zip(*p([*map(list,zip(*g[::-1]))]))][::-1]


## shorter unzipped (247)
def p(g):
 l=range(len(g));(J,E),*B,(C,F)=[[A,D]for A in l for D in l if g[A][D]];r=*map(list,g),
 for A in l[J+1:]:
  for D in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]:r[A][D]=4
 return(g[C][F-2]<1)*r or[*zip(*p([*zip(*g[::-1])]))][::-1]

def p(g):
 l=range(len(g));(J,E),*B,(C,F)=[[A,D]for A in l for D in l if g[A][D]];z=g[C][F-2]<1
 for A in l[J+1:]:
  for D in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]:g[A][D]+=z*4
 return z*g or[*zip(*p([*map(list,zip(*g[::-1]))]))][::-1]

### mwi (282 (331 unzipped) bytes)
def p(g,k=3):
 l=range(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*B,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*range(E+2,F-1),F+A-C-2,E-A+C+2),range(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### combined (284 (327 unzipped) bytes)
def p(g,k=3,v=range):
 l=v(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*_,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*v(E+2,F-1),F+A-C-2,E-A+C+2),v(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### ovs (287 (341 unzipped) bytes)
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
