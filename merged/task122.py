# ovs (71 bytes, gold)
p=lambda a:'3, 0'in'%s'%max(a)and[*map(p,a)]or a[:len(a)^1][-2:]+a[:-2]

### mwi (79 bytes)
p=lambda a:7in map(sum,a)and a[-2-len(a)%2:][:2]+a[:-2]or[*zip(*p([*zip(*a)]))]

### att (82 bytes)
p=lambda a:7in map(sum,a)and a[-2:][::(-1)**len(a)]+a[:-2]or[*zip(*p([*zip(*a)]))]

### combined (94 bytes)
p=lambda i:sum(map(max,i))<8and[[x[0]%2*3,x[1]%2*3,*x[:-2]]for x in i]or[*zip(*p([*zip(*i)]))]
