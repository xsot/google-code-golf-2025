# att (51 vs 49 bytes for gold)
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]

### ovs (tied, 51 bytes)
p=lambda g:[[l.pop(0)*b*2for b in l[4:]]for l in g]

### xsot (tied, 51 bytes)
p=lambda m:[[c*r.pop(4)*2for c in r[:3]]for r in m]

### combined (tied, 51 bytes)
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
