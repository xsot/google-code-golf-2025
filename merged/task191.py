# ovs (255 (327 unzipped) vs 251 bytes for gold)
def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:g=E*g[::-1]or[*map(list,zip(*g))];[0for C,H in B(g,-1)for D,I in B(g,-1)for F,H in B(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in B(A)for G,I in B(H)))for G,I in B(H)for g[C+F][D+G]in[I]*(-1<D+G<23>C+F>-1)]
 return g

## better golf, 274/302:
E=enumerate
def p(g):
 Z,m,M=[{j+i*1jfor i,r in E(g)for j,v in E(r)if C==v}for C in(0,1,4)]
 for I in range(8):
  for i in M:
   Y,*_=t={y for y in M if{y+1,y-1j,y-1}<m|M};W,N=[{i+1j**I*(y-Y-I//4*2*(y-Y).real)for y in e}for e in(t,m)]
   for y in N&Z:g[int(y.imag)][int(y.real)]|=W<=M!=N-M==N
 return g

### mwi (265 (356 unzipped) bytes)
def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:
  g=E*g[::-1]or[*map(list,zip(*g))]
  for C in range(-9,30):
   for D in range(-9,30):
    for(F,H)in B(A*all(g[C+F][D+G]==I//2*2if-1<D+G<23>C+F>-1else I<4for(F,H)in B(A)for(G,I)in B(H))):
     for(G,I)in B(H):
      if-1<D+G<23>C+F>-1:g[C+F][D+G]=I
 return g

### combined (267 (359 unzipped) bytes)
def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:
  g=E*g[::-1]or[*map(list,zip(*g))]
  for C in range(-9,30):
   for D in range(-9,30):
    for(F,H)in B(A*all(g[C+F][D+G]==I//2*2if 23>D+G>-1<C+F<23 else I<4for(F,H)in B(A)for(G,I)in B(H))):
     for(G,I)in B(H):
      if 23>D+G>-1<C+F<23:g[C+F][D+G]=I
 return g
