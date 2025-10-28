# joking (49 bytes, gold)
p=lambda i:i*0!=0and[i:=[p(x),x][x!=i]for x in i]

### combined (56 bytes)
p=lambda i:[i:=[f:=y*(x!=i or f<y)for y in x]for x in i]

### ovs (57 bytes)
p=lambda g,t=0:[g:=[t:=v^t&v*(g==r)for v in r]for r in g]
