def	p(t):
	f={r+d*1j:t[d][r]for	d	in	range(len(t))for	r	in	range(len(t))}
	n,e=[d	for	d	in	f	if	f[d]==3]
	i=[(n,e-n,1),(n,n-e,1)]
	for*o,d,n,e	in	i:
		if(d	in	f)*e%8:
			if	f[d]==2:return[[(r+d*1jin	o)*3|t[d][r]for	r	in	range(len(t))]for	d	in	range(len(t))]
			i+=[o+[d-f[d]//8*n,d-f[d]//8*n+r,r,~f[d]//8*e]for	r	in	f[d]//8*[n/1j,n*1j]or[n]]