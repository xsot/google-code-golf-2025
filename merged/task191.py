# combined (359 vs 251 bytes for gold)
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
