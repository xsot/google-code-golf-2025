# ovs (96 vs 95 bytes for gold)
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
