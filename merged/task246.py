# joking (126 vs 105 bytes for gold)
# almost identical to 335
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k+2in x)*8for y in x],*i)],k-1)

### combined (131 bytes)
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k+2in x)*8for b,y in enumerate(x)]for x in zip(*i)],k-1)

### att (137 bytes)
def p(a,n=0,b=0):
	for c in a:d=b;b^=sum(c)%8*4&8;c[j]=c[j:=sum(a,c).index(3-n)%len(c)]or d|b
	*d,=map(list,zip(*a));return n*d or p(d,1)
