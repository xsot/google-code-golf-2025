# joking (62 vs 61 bytes for gold)
p=lambda g,s=[0]:s*-1*-1or[*map(p,g,(s+g)[1:3+len(s)//12]*10)]

##
p=lambda g,x=1:[(g[x:=x^1][1:3+(l:=len(g))//12]*9)[:l]for _ in g]
p=lambda g,x=1:[(g[x:=x^1][1:3+len(g)//12]*9)[:len(g)]for _ in g]

### ovs (64 bytes)
p=lambda g,x=1:[(g[x:=x^1][1:3+l//12]*9)[:l]for l in map(len,g)]

##

p=lambda g,o=2:g*-1*-1or[*map(p,g[o>2:o]*10,[3+len(g)//12]*len(g))]

### combined (65 bytes)
p=lambda g,x=1:[(g[x:=x^1][1:len({*g[0]})]*9)[:len(g)]for _ in g]
