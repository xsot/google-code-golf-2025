# ovs (86 bytes, gold)
p=lambda a:[*map(f:=lambda*b,i=0:[v|(i:=i^b.count(v)*v-v)>>v*9for v in b],*map(f,*a))]

### att (93 bytes)
p=lambda a:[*map(f:=lambda*b,i=-1:[b[i:=i+1]or sum({*b[i:]}&{*b[:i]})for _ in b],*map(f,*a))]

### joking (93 bytes)
p=lambda a,*b,i=-1:[b[i:=i+1]or sum({*b[i:]}&{*b[:i]})for _ in b]or[*map(p,a,*map(p,a*3,*a))]

### combined (99 bytes)
p=lambda i,*n:[[y or max({*x[b:],0}&{*x[:b],0})for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
