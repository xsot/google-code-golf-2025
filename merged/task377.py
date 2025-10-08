# joking (55 bytes, gold)
p=lambda g,*a:[g:=y for*y,in zip(*a or p(g,*g))if g!=y]

### xsot (57 bytes)
# ovs + att
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]

##
p=lambda m,i=1:-i*m or p([*zip(*m[:1]+[y for x,y in zip(m,m[1:])if x!=y])],i-1)

### combined (57 bytes)
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]

### ovs (62 bytes)
p=lambda g,k=-1:g*k or p([y for*y,in zip(*g)if g!=(g:=y)],k+1)
##
p=lambda a,*w:a*-1*-1or[p(b[0],*a)for b in zip(a,*w)if w!=(w:=b)]
