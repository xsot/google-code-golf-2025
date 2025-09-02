# combined (56 vs 50 bytes for gold)
p=lambda i:[i:=[f:=y*(x!=i or f<y)for y in x]for x in i]

### ovs (57 bytes)
p=lambda g,t=0:[g:=[t:=v^t&v*(g==r)for v in r]for r in g]
