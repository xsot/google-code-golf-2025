# ovs (96 vs 93 bytes for gold)
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]

##
p=lambda g,k=3,P=[0]:-k*g or[P:=((P>r)*[k]*(P.count(P[0])+k-2)+r)[:len(r)]for r in p(g,k-2)][::-1]
def p(g):i=g.index(m:=max(g));return[[*map(max,(i+sum(m)//2)*[3>>((i:=i-1)<0)]+g[0],r)]for r in g]

### combined (tied, 96 bytes)
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
