# ovs (191 vs 156 bytes for gold)
def p(g):f=sum(g,[]);C=[sum(R[i%11&~3:][:4].count(0)for R in g[i//11&~3:][:4])for i in range(121)];return[[v*(v==5)or(C[i]==min(C))*max({*f}-{5})for i,v in r]for r in zip(*[enumerate(f)]*11)]
