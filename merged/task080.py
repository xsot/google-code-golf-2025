# combined (465 vs 283 bytes for gold)
def p(g):
 e=enumerate;t=[-1,0],[1,0],[0,-1],[0,1];E=[A+1for A,B in e(g)if len({*B})==1][0];c=[A[::E]for A in g[::E]];J=lambda A,B:len(c)>A>-1<B<len(c[0])
 for A,B in e(c):
  for C,y in e(B):
   if sum(0<y*c[A+H][C+I]for H,I in t if J(A+H,C+I))>3:
    for K,B in e(c):
     for L,R in e(B):
      for H,I in t+([-1,-1],[-1,1],[1,-1],[1,1]):
       if(R==y)*J(A+H,C+I)*J(K+H,L+I):c[K+H][L+I]=c[A+H][C+I]
    return[[y or c[A//E][C//E]for C,y in e(B)]for A,B in e(g)]
