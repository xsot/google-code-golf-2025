def	p(r):
	for	i	in	range(4):t=[*map(min,r)].index(0);e=[*map(min,r)].count(0);r=[*map(list,zip(*r))][::-1];n=[*map(min,r)].index(0);[0for	i	in	range(4)for	o	in	range(e)for	s	in	range(e)for	r[n-1+r[n][t]//-9*~i-e*i-o][t-1+r[n][t]//-9*~i-e*i-s]in	r[n-1+r[n][t]//8][t-1+r[n][t]%8:][:1>r[n+o][t+s]<=n-1+r[n][t]//-9*~i-e*i-o|t-1+r[n][t]//-9*~i-e*i-s]]
	return	r