# att (65 vs 61 bytes for gold)
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]

### ovs (tied, 65 bytes)
p=lambda g:[[v or 2*any(c)*any(r)for*c,v in zip(*g,r)]for r in g]
