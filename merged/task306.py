# joking+mwi (81 vs 74 bytes for gold)
p=lambda i,k=7:-k*i or[[*x[:10],*map(max,x,x[10:])]for x in zip(*p(i,k-1))][::-1]

### att (82 bytes)
p=lambda a:[*map(f:=lambda*b:[max(b[i%10::10])for i in range(len(b))],*map(f,*a))]

### ovs (126 bytes)
E=enumerate
p=lambda g:[[max(sum([r[j%s::s]for r in g[i%s::s]],[]))for j,_ in E(r)]for i,r in E(g)for s,q in E(g,1)if q[0]==4]
