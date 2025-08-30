# joking+mwi (269 (316 unzipped) vs 254 bytes for gold)
def p(g):
 D=enumerate;E=sum(g,[]);*L,M=sorted({*E},key=E.count);A=[[M]*len(A)for A in g]
 for N in L:
  C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];F,*_,P=sorted(A for(A,B)in C);G,*_,Q=sorted(B for(A,B)in C);B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=g[J][K]
 return[A[:B]for A in A[:B]]
