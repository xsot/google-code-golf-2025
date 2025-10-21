p=lambda g,c=1:(f:=lambda g:[r for r in zip(*g)if c in r])(w:=f(f(f(g))))*(w[::-1]==w)or p(g,c+1)

##
p=lambda g,c=9:c and p(g,c-1)or((w:=[g:=[r for r in zip(*g)if c in r]for _ in g])[2][::-1]in w)*g
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)
