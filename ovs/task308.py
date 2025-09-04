def p(g):
 A=[9*[M:=max(E:=sum(g,[]),key=E.count)]for(A)in g]
 for N in{*E}-{M}:
  (F,G),*B,(P,Q)=C=[[A,C]for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==N];B=max(P-F,Q-G)+1
  for(J,K)in C:A[J*2-F+B-P>>1][K*2-G+B-Q>>1]=N
 return[A[:B]for A in A[:B]]
