# att (185 bytes, gold)
def p(a,n=3):
	for i,b in enumerate(a):
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):i-~d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
