# joking (77 bytes, gold)
p=lambda i,*c:[*map(min,i,[9,9]+i[::-1],c)]or[i:=[*map(p,i,*i)]for _ in i][2]

##
p=lambda i,k=2:-k*i or p([[*map(min,a,[9,9]+a[::-1],c)]for*c,a in zip(*i,i)],k-1)
p=lambda i,k=2:-k*i or p([[*map(min,a,b,c)]for a,b,*c in zip(i,i[:2]+i[::-1],*i)],k-1)

### mwi (80 bytes)
p=lambda i:[i:=[[*map(min,a,[9,9]+a[::-1],c)]for*c,a in zip(*i,i)]for _ in i][2]

### ovs (103 bytes)
p=lambda i,k=2,r=range(30):-k*i or p([[min(i[a][b],i[b][a],i[1-b^-~b>>b][a])for b in r]for a in r],k-1)

### combined (103 bytes)
p=lambda i,k=2,r=range(30):-k*i or p([[min(i[a][b],i[b][a],i[1-b^-~b>>b][a])for b in r]for a in r],k-1)
