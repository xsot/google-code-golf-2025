# joking+mwi (58 bytes, gold)
p=lambda i:(r:=i[:3])*([*map(list,zip(*r))]!=r)or p(i[3:])

### ovs (tied, 58 bytes)
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])

### xsot (tied, 58 bytes)
p=lambda m:(x:=m[:3])*(x!=[*map(list,zip(*x))])or p(m[3:])
