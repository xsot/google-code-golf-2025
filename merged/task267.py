# att (57 vs 46 bytes for gold)
p=lambda a:[[(d:=a[-1][0])*(0<c!=d)for c in b]for b in a]

### ovs (59 bytes)
p=lambda g:[[sum({*[g[-1][0]]*v}-{v})for v in r]for r in g]
