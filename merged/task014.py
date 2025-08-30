# joking+mwi (76 vs 70 bytes for gold)
p=lambda i:[[y[0]for y in zip(x,*i)if len({*y})>2]for x in i if len({*x})>2]

### ovs (85 bytes)
p=lambda g:[[v for v,*c in zip(l,*g)if{*c}&t]for l in g if{*l}&(t:={*g[0]}^{*g[-1]})]
