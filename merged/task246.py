# combined (131 vs 126 bytes for gold)
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k+2in x)*8for b,y in enumerate(x)]for x in zip(*i)],k-1)

### att (137 bytes)
def p(a,n=0,b=0):
	for c in a:d=b;b^=sum(c)%8*4&8;c[j]=c[j:=sum(a,c).index(3-n)%len(c)]or d|b
	*d,=map(list,zip(*a));return n*d or p(d,1)
