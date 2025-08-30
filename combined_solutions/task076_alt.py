def p(g):
 C=[];e=enumerate
 for A,r in e(g):
  for B,F in e(r):
   G={(A,B)}
   for D in[*C]:
    if F*any((A+l//3-1,B+l%3-1)in D for l in range(9)):C.remove(D);G|=D
   C+=[G]*F
 for D in[[{(A,B,g[A][B])for(A,B)in A},{(A,B,g[A][B])for(A,B)in A if g[A][B]%2<1}]for A in C if any(g[A][B]==3for(A,B)in A)]:
  for K in'_'*4:
   g=[*zip(*g[::-1])]
   for L in'__':
    A=len(g:=[*map(list,g[::-1])])
    for B in range(-A,A):
     for C in range(-A,A):
      if all(A>E+B>=0<=F+C<len(g[0])>G==g[E+B][F+C]for(E,F,G)in D[1]):
       for(E,F,G)in[*D[0],*D[1]]:g[E+B][F+C]=G
 return g