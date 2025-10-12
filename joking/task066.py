def	p(g):
	M={D+y*1j:g[y][D]for	y	in	range(len(g))for	D	in	range(len(g))}
	A,C=[y	for	y	in	M	if	M[y]==3]	
	S=[(A,C-A,1),(A,A-C,1)]
	for*V,y,A,C	in	S:
		if(y	in	M)*C%8:
			if	M[y]==2:return[[(D+y*1jin	V)*3|g[y][D]for	D	in	range(len(g))]for	y	in	range(len(g))]
			S+=[V+[y-M[y]//8*A,y-M[y]//8*A+D,D,~M[y]//8*C]for	D	in	M[y]//8*[A/1j,A*1j]or[A]]