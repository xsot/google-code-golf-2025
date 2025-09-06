# att (93 vs 87 bytes for gold)
p=lambda a:[*map(f:=lambda*b,i=-1:[b[i:=i+1]or sum({*b[i:]}&{*b[:i]})for _ in b],*map(f,*a))]

### combined (99 bytes)
p=lambda i,*n:[[y or max({*x[b:],0}&{*x[:b],0})for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
