def	p(r):
	f,l=max((len({*str(e:=[f[o:o+3]for	f	in	r[f:f+3]])}),e)for	f	in	range(len(r))for	o	in	range(len(r[-1])))
	for	e	in	range(len(r[-1])):
		for	f	in	range(len(r)-e*3):
			for	o	in	range(len(r[-1])-e*3):
				for	a	in	range(len(r[-1])):
					for	a	in	range(e*3*all(r[f+a][o+n]==l[a//e][n//e]or	r[f+a][o+n]==r[-1][-1]!=l[a//e][n//e]==max({*l[1]}-{r[-1][-1]})for	a	in	range(e*3)for	n	in	range(e*3))):
						for	n	in	range(e*3):r[f+a][o+n]=l[a//e][n//e]
					l=*zip(*l[::-1]),
	return	r