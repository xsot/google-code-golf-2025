def	p(e):
	*f,n={o*66+l:(e)for	o,e	in	enumerate(e)for	l,e	in	enumerate(e)if	e},
	for	o	in	n:
		u={o}
		for	t	in*f,:
			if{o-66,o-1}&t:f.remove(t);u|=t
		f+=u,
	for	t	in*f,:
		for	o	in	t:
			for	u	in	t:
				i=t
				for	i	in	1//len([r	for	r	in	i	if	n[o]==n[r]])*f:
					for	a	in	t-{u}:
						for	r	in([r	for	r	in	i	if	n[o]==n[r]==n[u]]):r+=(len([r	for	r	in	i	if	n[o]==n[r]==n[u]])^6)%6*(a-u);e[r//66][r%66],={n[r]for	r	in	i}-{n[o]}
	return	e