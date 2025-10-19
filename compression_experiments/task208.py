def	p(t):
	u=min(sum(n:=t,[]),key=sum(n:=t,[]).count);r=len(n:=[n	for	n	in	zip(*n)if	u	in	n])
	i=len(n:=[n	for	n	in	zip(*n)if	u	in	n])
	for	e	in	range(22-r):
		for	o	in	range(22-i):
			for	t[o][e:e+r]in	n*0**sum(sum(n[e:e+r][1:-1])for	n	in	t[o:o+i][1:-1]):o+=1
	return	t