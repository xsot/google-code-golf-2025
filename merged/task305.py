# joking (62 vs 57 bytes for gold)
p=lambda g,y=0:[(sorted({*x}-{0})*9)[y:(y:=y+1)+15]for x in g]

## recursive alts
p=lambda i,s=0:i*-1and s%i+1or[p(max(i),s+n)for n in range(16)]
p=lambda i,s=0:[p(max(i),s+n)for n in range(i*-1or 16)]or s%i+1

##bunch of experiments
p=lambda g:[([*range(1,1+max(g[0]))]*9)[y:y+16]for y in range(16)]
p=lambda g,r=range(16):[([*r[1:1+max(g[0])]]*9)[y:y+16]for y in r]
p=lambda g,y=0:g and[(sorted({*g.pop()}-{0})*9)[y:y+16]]+p(g,y+1)
p=lambda g,r=range(16):[[1+(y+x)%max(g[0])for x in r]for y in r]
p=lambda g,y=-1:[*zip(*[(sorted({*x}-{0})*9)[(y:=y+1):31]for x in g])]
p=lambda g:[*zip(*[(sorted({*g[0]}-{0})*9)[y:31]for y in range(16)])]
p=lambda g,r=range(16):[([*r[1:1+max(g[0])]]*9)[y:y+16]for y in r]
p=lambda g:[[1+x%max(g[0])for x in range(y,y+16)]for y in range(16)]

### combined (tied, 62 bytes)
p=lambda g:[(sorted({*g[0]}-{0})*9)[y:y+16]for y in range(16)]

### ovs (74 bytes)
p=lambda g:[[max(r[j%(n:=len({*r}-{0}))::n])for j in range(16)]for r in g]
