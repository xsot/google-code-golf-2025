p=lambda g,s=[0]:s*-1*-1or[*map(p,g,(s+g)[1:3+len(s)//12]*10)]

##
p=lambda g,x=1:[(g[x:=x^1][1:3+(l:=len(g))//12]*9)[:l]for _ in g]
p=lambda g,x=1:[(g[x:=x^1][1:3+len(g)//12]*9)[:len(g)]for _ in g]