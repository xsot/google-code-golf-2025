def	p(a):
	r=[[*e]for	e	in	zip(*a)if	1in	e]
	r=[[*e]for	e	in	zip(*r)if	1in	e]
	for	e	in	0,1,0,1,0,1,0,1:a=e*a[::-1]or[[*e]for	e	in	zip(*a)];[1for	t,e	in	enumerate(a)for	z,e	in	enumerate(a)for	i,e	in	enumerate(all(a[t+i-1][z+n-1]==e&-2if	0<z+n<24>t+i>0else	e<4for	i,e	in	enumerate(r)for	n,e	in	enumerate(e))*r)for	n,e	in	enumerate(e)if	0<z+n<24>t+i>0for	a[t+i-1][z+n-1]in[e]]
	return	a