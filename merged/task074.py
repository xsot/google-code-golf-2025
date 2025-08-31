# ovs (103 vs 82 bytes for gold)
p=lambda i,k=2,r=range(30):-k*i or p([[min(i[a][b],i[b][a],i[1-b^-~b>>b][a])for b in r]for a in r],k-1)

### combined (tied, 103 bytes)
p=lambda i,k=2,r=range(30):-k*i or p([[min(i[a][b],i[b][a],i[1-b^-~b>>b][a])for b in r]for a in r],k-1)
