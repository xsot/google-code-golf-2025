# att (57 vs 54 bytes for gold)
p=lambda a:a[:-1]+[[4*(sum(c)<2*max(c))for c in zip(*a)]]

### ovs (58 bytes)
p=lambda g:g[:-1]+[[1//r.count(max(r))*4for r in zip(*g)]]
