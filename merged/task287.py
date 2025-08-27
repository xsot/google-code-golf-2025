p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]

### ovs (123 bytes)
M=lambda x:(x[:8],x[::-1])
p=lambda g:sum(M([sum(M([max({*v}-{4})for v in zip(*M(r),*M(R))]),[])for r,R in zip(*M(g))]),[])
