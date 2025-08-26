p=lambda m:(x:=m[:3])*(x!=[*map(list,zip(*x))])or p(m[3:])

### ovs (tied, {ovs_score} bytes)
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
