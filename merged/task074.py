# ovs (158 vs 91 bytes for gold)
def p(g):g=[[x%9for x in r]+[0,0]for r in g]+[[0]*32]*2;return[[*map(max,*sum([[x,x[:1:-1]]for x in k],[]))]for k in zip(g,g[:1:-1],[*zip(*g)][::-1],zip(*g))]
