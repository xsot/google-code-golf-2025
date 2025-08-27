p=lambda a:2*[2*[d or any(c)*8for*c,d in zip(*a,b)]for b in a]

### ovs (tied, 62 bytes)
p=lambda g:[2*[v or 8*any(c)for*c,v in zip(*g,r)]for r in g]*2

### xsot (67 bytes)
p=lambda m:[2*[c or any(d)*8for c,d in zip(r,zip(*m))]for r in m]*2

##
p=lambda m:[2*[r[c]or any([*zip(*m)][c])*8for c in range(len(r))]for r in m]*2

def p(m):
 n=len(m)
 for i in range(n*n):m[r][c]=m[r:=i//n][c:=i%n]or(sum([*zip(*m)][c])>0)*8
 return[l*2for l in m]*2
