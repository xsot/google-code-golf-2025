# ovs (205 bytes, gold)
e=enumerate
def p(g):q=range(m:=min(A:={J-sum(C)//4:N for N in sum(g,g)if len(C:=[C+A*8for(A,B)in e(g)for(C,E)in e(B)if E==N])<5or(M:=N)*0for J in C})+3>>3,1-m);return[[A.get(y*8+x,M)for x in q]for y in q]

### joking (231 (253 unzipped) bytes)
def	p(g):
	A=[9*[Q:=max(P:=sum(g,[]),key=P.count)]for	A	in	g]
	for	N	in{*P}-{Q}:
		D=[(P:=A,Q:=C)for	A,g	in	enumerate(g)for	C,E	in	enumerate(g)if	E==N];F,G=D[0];B=max(P-F,Q-G)+1
		for	C,E	in	D:A[B-F-P+C*2>>1][B-G-Q+E*2>>1]=N
	return[A[:B]for	A	in	A[:B]]

##
def p(g):
 A=[#[*range(7,10)]##*[Q:=max(P:=sum(g,[]),key=P.count)]for A in g]
 for N in{*P}-{Q}:
  D=[#['[P:=A,Q:=C]','(P:=A,Q:=C)']##for A,g in enumerate(g)for C,E in enumerate(g)if E==N]#[';','\n  ']##F,G=D[0]#[';','\n  ']##B=max(P-F,Q-G)+1
  for C,E in D:A[B-#['F-P','P-F']##+C*2>>1][B-#['G-Q','Q-G']##+E*2>>1]=N
 return[A[:B]for A in A[:B]]

### mwi (242 (253 unzipped) bytes)
def	p(g):
	A=[9*[M:=max(E:=sum(g,[]),key=E.count)]for(A)in	g]
	for	N	in{*E}-{M}:
		(F,G),*B,(P,Q)=C=[[A,C]for(A,B)in	enumerate(g)for(C,E)in	enumerate(B)if	E==N];B=max(P-F,Q-G)+1
		for(J,K)in	C:A[J*2-F+B-P>>1][K*2-G+B-Q>>1]=N
	return[A[:B]for	A	in	A[:B]]

##
def p(g):
 *L,M=sorted(set(E:=sum(g,[])),key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*B,(P,Q)=C=[[A,C]for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]

### xsot (250 (262 unzipped) bytes)
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

### combined (252 (261 unzipped) bytes)
def p(g):
 D=enumerate;E=sum(g,[]);*L,M=sorted({*E},key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*_,(P,Q)=C=[[A,C]for(A,B)in D(g)for(C,E)in D(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]
