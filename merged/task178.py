# att (49 bytes, gold)
p=lambda a:a*-1*-1or[p(b)for b in a if a!=(a:=b)]

### xsot (57 bytes)
# ovs + att
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]

##
p=lambda m,i=1:-i*m or p([*zip(*m[:1]+[y for x,y in zip(m,m[1:])if x!=y])],i-1)

### ovs (62 bytes)
p=lambda g,k=-1:k*g or p([r for*r,in zip(*g)if g!=(g:=r)],k+1)
