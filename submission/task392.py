def p(g):
 e=enumerate;C=max(sum(g,[]));o=2+(f"{C}, 0, 0, {C}"in str(g))
 for k,_ in e(g):g=[[c or any(any(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])*[C,5][k%o<o-1]for x,c in e(r)]for y,r in e(g)]
 return g