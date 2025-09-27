p=lambda i,*n:n[-n.count(0):]+n or[*zip(*map(p,i,*i))][:15]

##

p=lambda g,k=15:k*[0]and[[c[c.count(max(c))-k]for c in zip(*g)]]+p(g,k-1)
