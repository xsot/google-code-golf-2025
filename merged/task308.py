# xsot (252 (262 unzipped) vs 254 bytes for gold)
def p(g):
 D=enumerate;*L,M=sorted(set(E:=sum(g,[])),key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*_,(P,Q)=C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]

##
# this is shorter before zip
def p(g):
 D=enumerate;E=sum(g,[]);*L,M=sorted({*E},key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*_,(P,Q)=C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]

### joking+mwi (261 bytes)
def p(g):
 D=enumerate;E=sum(g,[]);*L,M=sorted({*E},key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*_,(P,Q)=C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]
