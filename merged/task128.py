# ovs (73 vs 64 bytes for gold)
p=lambda g,k=15:k*[0]and[[c[c.count(max(c))-k]for c in zip(*g)]]+p(g,k-1)
