def	p(o):
	for*i,in[[]]*8:
		o=[i[::-1]for*i,in	zip(*o)]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				if	m:
					n={(r,e)}
					for	t	in*i,:
						if{(r-1,e),(r,e-1),(r-1,e+1),(r-1,e-1)}&t:i.remove(t);n|=t
					i+=[n]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				for	t	in*i,:
					for	n,f	in	t:
						if{(n-e,f-~r),(n-~e,f-r)}&t:o[n-e][f-r]|=len({*str([i[f:f+2]for*i,in	o[n:n+2]])})//8*o[n][f]
	return	o