# att (105 vs 104 bytes for gold)
p=lambda a,n=3,d=0:-n*a or p([[b.pop()|4*(n|2in b)*(d:=d^sum(c)&2)for c in a[::-1]]for*b,in zip(*a)],n-1)

### mwi (109 bytes)
p=lambda a,n=3,d=0:-n*a or p([[b.pop()or(n|2in b)*d*4for c in a[::-1]if[d:=d^sum(c)&2]]for*b,in zip(*a)],n-1)

### joking (126 bytes)
# almost identical to 335
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k+2in x)*8for y in x],*i)],k-1)

### combined (131 bytes)
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k+2in x)*8for b,y in enumerate(x)]for x in zip(*i)],k-1)
