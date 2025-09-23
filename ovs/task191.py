def p(g):
 A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in 0,1,0,1,0,1,0,1,:g=E*g[::-1]or[c for*c,in zip(*g)];[0for C,H in enumerate(g,-1)for D,I in enumerate(g,-1)for F,H in enumerate(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in enumerate(A)for G,I in enumerate(H)))for G,I in enumerate(H)for g[C+F][D+G]in[I]*(-1<D+G<23>C+F>-1)]
# for E in[0,1]*4:g=E*g[::-1]or[c for*c,in zip(*g)];[0for C,H in enumerate(g,-1)for D,I in enumerate(g,-1)for F,H in enumerate(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in enumerate(A)for G,I in enumerate(H)))for G,I in enumerate(H)if-1<D+G<23>C+F>-1for g[C+F][D+G]in[I]]
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
