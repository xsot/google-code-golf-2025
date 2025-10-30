# joking (97 bytes, gold)
p=lambda g,c=1:((f:=lambda g:[r for r in zip(*g)if c in r])(k:=f(g))==f(k[::-1]))*f(k)or p(g,c+1)

### ovs (tied, 97 bytes)
p=lambda g,c=1:(f:=lambda g:[r for r in zip(*g)if c in r])(w:=f(f(f(g))))*(w[::-1]==w)or p(g,c+1)

##
p=lambda g,c=9:c and p(g,c-1)or((w:=[g:=[r for r in zip(*g)if c in r]for _ in g])[2][::-1]in w)*g
p=lambda g,c=3,t=[]:c%3//2*t*((a:=[r for r in zip(*c%3*t or g)if c//3in r])==a[::-1])or p(g,c+1,a)  # <- this seems promising
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)

### mwi (99 bytes)
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(f(k)==f(k)[::-1])or p(g,c+1)

### combined (105 bytes)
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)
