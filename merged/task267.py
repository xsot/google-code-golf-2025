# combined (52 vs 2500 bytes for gold)
p=lambda i:[[i[-y>>8][x==i[6]]for y in x]for x in i]

### att (57 bytes)
p=lambda a:[[(d:=a[-1][0])*(0<c!=d)for c in b]for b in a]

### ovs (59 bytes)
p=lambda g:[[sum({*[g[-1][0]]*v}-{v})for v in r]for r in g]
