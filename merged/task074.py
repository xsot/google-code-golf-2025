# joking+mwi (106 vs 82 bytes for gold)
p=lambda i,k=2,r=range(30):-k*i or p([[min(i[a][b],i[b][a],(i+i[1::-1])[~b][a])for b in r]for a in r],k-1)

### ovs (158 bytes)
def p(g):g=[[x%9for x in r]+[0,0]for r in g]+[[0]*32]*2;return[[*map(max,*sum([[x,x[:1:-1]]for x in k],[]))]for k in zip(g,g[:1:-1],[*zip(*g)][::-1],zip(*g))]
