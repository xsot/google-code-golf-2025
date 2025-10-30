# att (68 bytes, gold)
p=lambda i,*I:[w for*w,r in zip(*I or p(zip(*i),*i),i)if[*{*r}][2:]]

### ovs (69 bytes)
p=lambda i,*I:[w for*w,r in zip(*I or p(zip(*i),*i),i)if len({*r})>2]

##

p=lambda g:[[v for v,*c in zip(l,*g)if{*c}&t]for l in g if{*l}&(t:={*g[0]}^{*g[-1]})]

### combined (76 bytes)
p=lambda i:[[y[0]for y in zip(x,*i)if len({*y})>2]for x in i if len({*x})>2]
