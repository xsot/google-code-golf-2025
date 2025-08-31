# combined (64 bytes, gold)
p=lambda i:[*zip(*[x[(j:=-x.count(0)):]+x[:j]for x in zip(*i)])]

### ovs (73 bytes)
p=lambda g,k=15:k*[0]and[[c[c.count(max(c))-k]for c in zip(*g)]]+p(g,k-1)
