# compression_experiments (227 (384 unzipped) vs 221 bytes for gold)
def	p(a):
	r=[[*e]for	e	in	zip(*a)if	1in	e]
	r=[[*e]for	e	in	zip(*r)if	1in	e]
	for	e	in	0,1,0,1,0,1,0,1:a=e*a[::-1]or[[*e]for	e	in	zip(*a)];[1for	t,e	in	enumerate(a)for	z,e	in	enumerate(a)for	i,e	in	enumerate(all(a[t+i-1][z+n-1]==e&-2if	0<z+n<24>t+i>0else	e<4for	i,e	in	enumerate(r)for	n,e	in	enumerate(e))*r)for	n,e	in	enumerate(e)if	0<z+n<24>t+i>0for	a[t+i-1][z+n-1]in[e]]
	return	a

### joking (230 (384 unzipped) bytes)
def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in 0,1,0,1,0,1,0,1:g=H*g[::-1]or[[*H]for H in zip(*g)];[1for C,H in enumerate(g)for D,H in enumerate(g)for F,H in enumerate(all(g[C+F-1][D+G-1]==H&-2if 0<D+G<24>C+F>0else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if 0<D+G<24>C+F>0for g[C+F-1][D+G-1]in[H]]
 return g

##
def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in#['[0,1]*4','[0,1]*8',' 0,1,0,1,0,1,0,1']##:g=H*g[::-1]or[[*H]for H in zip(*g)];[#[*range(10)]##for C,H in enumerate(g)for D,H in enumerate(g)for F,H in enumerate(all(g[C+F-1][D+G-1]==H&-2if 0<D+G<24>C+F>0else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if 0<D+G<24>C+F>0for g[C+F-1][D+G-1]in[H]]
 return g

### ovs (248 (364 unzipped) bytes)
def p(g):
 A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:g=E*g[::-1]or[[*c]for c in zip(*g)];[0for C,H in enumerate(g,-1)for D,I in enumerate(g,-1)for F,H in enumerate(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in enumerate(A)for G,I in enumerate(H)))for G,I in enumerate(H)if-1<D+G<23>C+F>-1for g[C+F][D+G]in[I]]
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

### combined (265 (359 unzipped) bytes)
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
