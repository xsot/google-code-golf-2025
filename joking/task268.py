# 224
def p(g):J,E=[(C:=A,F:=D)for A in range(len(g))for D in range(len(g))if g[A][D]][0];return g[C][F-2]and[*zip(*p([[*A]for A in zip(*g[::-1])]))][::-1]or[g for A in range(J+1,len(g))for D in({*range(E+2,F-1),C-A+E+2,F-2+A-C}&{*range(len(g))},range(E+1,F))[A<C]for g[A][D]in[4]][0]

##
def p(g):J,E=[#['[C:=A,F:=D]','(C:=A,F:=D)']##for A in range(len(g))for D in range(len(g))if g[A][D]][0];return g[C][F-2]and[*zip(*p([[*A]for A in zip(*g[::-1])]))][::-1]or[g for A in range(J+1,len(g))for D in({*range(E+2,F-1),C-A+E+2,F-2+A-C}&{*range(len(g))},range(E+1,F))[A<C]for g[A][D]in[4]][0]

##
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