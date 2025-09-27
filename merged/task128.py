# ovs (59 bytes, gold)
p=lambda i,*n:n[-n.count(0):]+n or[*zip(*map(p,i,*i))][:15]

##

p=lambda g,k=15:k*[0]and[[c[c.count(max(c))-k]for c in zip(*g)]]+p(g,k-1)

### joking (62 bytes)
p=lambda i,*n:n[(j:=-n.count(0)):]+n[:j]or[*zip(*map(p,i,*i))]

### combined (64 bytes)
p=lambda i:[*zip(*[x[(j:=-x.count(0)):]+x[:j]for x in zip(*i)])]
