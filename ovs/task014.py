p=lambda i,*I:[w for*w,r in zip(*I or p(zip(*i),*i),i)if len({*r})>2]

##

p=lambda g:[[v for v,*c in zip(l,*g)if{*c}&t]for l in g if{*l}&(t:={*g[0]}^{*g[-1]})]
