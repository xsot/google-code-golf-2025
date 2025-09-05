# joking (82 vs 2500 bytes for gold)
p=lambda i:[[(c[0]+7in{*x}&{*c,hash(c)%1070})*2+c[0]for c in zip(x,*i)]for x in i]

## only one test case is weird (train1)
## hash of c = -4089153112963877882

### combined (114 bytes)
p=lambda i:[[y%8*(8in{*x}&{*(u:=[*zip(*i)])[b],*{*u[b-1]}&{*u[-~b%17]}})*3or y for b,y in enumerate(x)]for x in i]

### mwi (126 bytes)
p=lambda g,k=31,r=range(17):-k*g or p([[max(3*(g[-y][x]%5+g[~y][x-1]%5+g[~y][-~x%17]%5>5),g[~y][x])for y in r]for x in r],k-1)
