# ovs (46 bytes, gold)
p=lambda i:[[i[6][[y]<x]for y in x]for x in i]

### combined (52 bytes)
p=lambda i:[[i[-y>>8][x==i[6]]for y in x]for x in i]

### att (57 bytes)
p=lambda a:[[(d:=a[-1][0])*(0<c!=d)for c in b]for b in a]
