def	p(z):
	t=min(sum(r:=z,[]),key=sum(r:=z,[]).count);o=len(r:=[r	for	r	in	zip(*r)if	t	in	r])
	f=len(r:=[r	for	r	in	zip(*r)if	t	in	r])
	for	n	in	range(22-o):
		for	m	in	range(22-f):
			for	z[m][n:n+o]in	r*0**sum(sum(r[n:n+o][1:-1])for	r	in	z[m:m+f][1:-1]):m+=1
	return	z