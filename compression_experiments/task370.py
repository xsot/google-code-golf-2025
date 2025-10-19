def	p(a):
	for	f	in	range(4):m=[*map(min,a)].index(0);i=[*map(min,a)].count(0);a=[*map(list,zip(*a))][::-1];u=[*map(min,a)].index(0);[0for	f	in	range(4)for	d	in	range(i)for	n	in	range(i)for	a[u-1+a[u][m]//-9*~f-i*f-d][m-1+a[u][m]//-9*~f-i*f-n]in	a[u-1+a[u][m]//8][m-1+a[u][m]%8:][:1>a[u+d][m+n]<=u-1+a[u][m]//-9*~f-i*f-d|m-1+a[u][m]//-9*~f-i*f-n]]
	return	a