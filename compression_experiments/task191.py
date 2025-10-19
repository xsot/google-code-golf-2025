def	p(n):
	e=[[*l]for	l	in	zip(*n)if	1in	l]
	e=[[*l]for	l	in	zip(*e)if	1in	l]
	for	l	in	0,1,0,1,0,1,0,1:n=l*n[::-1]or[[*l]for	l	in	zip(*n)];[1for	r,l	in	enumerate(n)for	z,l	in	enumerate(n)for	i,l	in	enumerate(all(n[r+i-1][z+f-1]==l&-2if	0<z+f<24>r+i>0else	l<4for	i,l	in	enumerate(e)for	f,l	in	enumerate(l))*e)for	f,l	in	enumerate(l)if	0<z+f<24>r+i>0for	n[r+i-1][z+f-1]in[l]]
	return	n