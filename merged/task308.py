# mwi (249 (266 unzipped) vs 252 bytes for gold)
def p(g):
 *L,M=sorted(set(E:=sum(g,[])),key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*B,(P,Q)=C=[[A,C]for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]

### xsot (252 (262 unzipped) bytes)
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

### combined (254 (261 unzipped) bytes)
def p(g):
 D=enumerate;E=sum(g,[]);*L,M=sorted({*E},key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*_,(P,Q)=C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]
