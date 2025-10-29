def	p(n):
	*f,e={u*66+o:(n)for	u,n	in	enumerate(n)for	o,n	in	enumerate(n)if	n},
	for	u	in	e:
		t={u}
		for	m	in*f,:
			if{u-66,u-1}&m:f.remove(m);t|=m
		f+=t,
	for	m	in*f,:
		for	u	in	m:
			for	t	in	m:
				r=m
				for	r	in	1//len([a	for	a	in	r	if	e[u]==e[a]])*f:
					for	i	in	m-{t}:
						for	a	in([a	for	a	in	r	if	e[u]==e[a]==e[t]]):a+=(len([a	for	a	in	r	if	e[u]==e[a]==e[t]])^6)%6*(i-t);n[a//66][a%66],={e[a]for	a	in	r}-{e[u]}
	return	n