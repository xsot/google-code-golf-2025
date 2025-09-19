# att (63 vs 56 bytes for gold)
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]

### joking (tied, 63 bytes)
p=lambda i,*w:i*0!=0and[*map(p,i,i[::-1],*w)]or max({i,*w}-{4})

### combined (tied, 63 bytes)
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]

### ovs (123 bytes)
M=lambda x:(x[:8],x[::-1])
p=lambda g:sum(M([sum(M([max({*v}-{4})for v in zip(*M(r),*M(R))]),[])for r,R in zip(*M(g))]),[])
