# att (58 bytes, gold)
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])

### xsot (tied, 58 bytes)
p=lambda m:(x:=m[:3])*(x!=[*map(list,zip(*x))])or p(m[3:])
