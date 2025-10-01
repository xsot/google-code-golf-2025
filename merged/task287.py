# att (55 bytes, gold)
p=lambda*a:sum({*a[3:]}-{4})or[*map(p,*a+a,a[0][::-1])]

##
p=lambda*a:a[2:]and max({*a}-{4})or[*map(p,*a,a[0][::-1])]
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]

### joking (63 bytes)
p=lambda i,*w:i*0!=0and[*map(p,i,i[::-1],*w)]or max({i,*w}-{4})

### combined (63 bytes)
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]

### ovs (123 bytes)
M=lambda x:(x[:8],x[::-1])
p=lambda g:sum(M([sum(M([max({*v}-{4})for v in zip(*M(r),*M(R))]),[])for r,R in zip(*M(g))]),[])
