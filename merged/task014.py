# ovs (85 vs 70 bytes for gold)
p=lambda g:[[v for v,*c in zip(l,*g)if{*c}&t]for l in g if{*l}&(t:={*g[0]}^{*g[-1]})]
