def p(a,n=0,b=0):
	for c in a:d=b;b^=sum(c)%8*4&8;c[j]=c[j:=sum(a,c).index(3-n)%len(c)]or d|b
	*d,=map(list,zip(*a));return n*d or p(d,1)