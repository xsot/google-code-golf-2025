def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:g=E*g[::-1]or[*map(list,zip(*g))];[0for C,H in B(g,-1)for D,I in B(g,-1)for F,H in B(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in B(A)for G,I in B(H)))for G,I in B(H)for g[C+F][D+G]in[I]*(-1<D+G<23>C+F>-1)]
 return g