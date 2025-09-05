# att (64 vs 2500 bytes for gold)
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]

### ovs (tied, 64 bytes)
p=lambda g:[[v+2-2*any(r)*any(c)for*c,v in zip(*g,r)]for r in g]

### combined (tied, 64 bytes)
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]

### xsot (75 bytes)
p=lambda m,i=1:-i*m or p([*zip(*[r*(sum(r)>4)or[2]*len(r)for r in m])],i-1)
