# ovs (232 (242 unzipped) bytes, gold)
def p(g):l=range(len(g));(J,E),*B,(C,F)=[[A,D]for A in l for D in l if g[A][D]];return g[C][F-2]and[*zip(*p([*map(list,zip(*g[::-1]))]))][::-1]or[g for A in l[J+1:]for D in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]for g[A][D]in[4]][0]

### mwi (236 (253 unzipped) bytes)
def	p(g):
	l=range(len(g));(J,E),*B,(C,F)=[[A,D]for	A	in	l	for	D	in	l	if	g[A][D]]
	if	g[C][F-2]<1:
		for	A	in	l[J+1:]:
			for	D	in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]:g[A][D]=4
		return	g
	return[*zip(*p([*map(list,zip(*g[::-1]))]))][::-1]

##
def p(g,k=3):
 l=range(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*B,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*range(E+2,F-1),F+A-C-2,E-A+C+2),range(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)

### joking (237 (253 unzipped) bytes)
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

### combined (283 (327 unzipped) bytes)
def p(g,k=3,v=range):
 l=v(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*_,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*v(E+2,F-1),F+A-C-2,E-A+C+2),v(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
