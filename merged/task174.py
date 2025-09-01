# mwi (99 vs 97 bytes for gold)
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(f(k)==f(k)[::-1])or p(g,c+1)

### ovs (105 bytes)
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)

### combined (105 bytes)
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)
