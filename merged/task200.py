# joking (84 bytes, gold)
p=lambda g,r=5:[([0]*g[9].index(c:=max(g[9]))+[c,r,c,r:=any(x)*5]*3)[:10]for x in g]

##
p=lambda g:[[c:=0,n:=0]and[(c:=c|b)and[a//9*5,c,5*0**a,c][n:=-~n%4]for b in g[9]]for a in range(10)]
p=lambda g,P=[0]*9:[*zip(*([P*2]*g[9].index(c:=max(g[9]))+[C:=[c]*10,[5]+P,C,P+[5]]*9)[:10])]

### ovs (86 bytes)
p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,i%7,c,i%6]*3)[:10]for i in b'6********M']

##

p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]

### combined (110 bytes)
p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]
