# joking (55 bytes, gold)
# same as 106
p=lambda i,s=[],k=3:-k*i or p([*zip(*i+s)],i[::-1],k-1)

### ovs (68 bytes)
p=lambda g,a=-3:-a*g and[r:=g[a]+sum(g,[])[a::-3],*p(g,a+1),r[::-1]]

### combined (74 bytes)
p=lambda g:(t:=[a+b for*b,a in zip(*g[::-1],g)])+[e[::-1]for e in t[::-1]]

### xsot (92 bytes)
def p(M,m=[[0]*6]*6):
 for i in[0,1,2]*9:m[i][:3]=M[i];*m,=map(list,zip(*m[::-1]))
 return m
