# zip fiddling
def	p(g):
	A=[9*[m:=max(sum(g,[]),key=sum(g,[]).count)]for	A	in	g]
	for	N	in{*sum(g,[])}-{m}:
		(F,G),*B,(P,Q)=D=[[A,C]for(A,g)in	enumerate(g)for(C,E)in	enumerate(g)if	E==N];B=max(P-F,Q-G)+1
		for(C,E)in	D:A[B-F-P+C*2>>1][B-G-Q+E*2>>1]=N
	return[A[:B]for	A	in	A[:B]]