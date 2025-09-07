# mwi (110 vs 109 bytes for gold)
p=lambda g,*G:sum([[[2,*r,2]]*(any({*r}-{2})*str(g).count('2')//12or{*r}=={2})for*r,in zip(*G or p(g,*g))],[])

### ovs (112 bytes)
p=lambda g,*G:sum([[[2,*r,2]]*({*r}=={2}or({*r}-{2}!={0})*str(g).count('2')//12)for*r,in zip(*G or p(g,*g))],[])

### combined (185 bytes)
def p(i,e=enumerate):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{2},{1,*range(3,10)}]];s=len(l)//3;return[[y or m[~-a//s][~-b//s]for b,y in e(x)]for a,x in e(l)]
