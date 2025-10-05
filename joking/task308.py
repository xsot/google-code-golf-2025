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