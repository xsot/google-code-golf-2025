def p(g):y,x=max((y+1,x+1)for y,g in enumerate(g)for x,c in enumerate(g)if c);s=4-0**g[y-1][x-4];v=-~len(h:=[*filter(max,zip(*filter(max,zip(*g[:y-s]))))])//s;return[[h[Y*v][X*v]and g for X,g in enumerate(g[x-s:x])]for Y,g in enumerate(g[y-s:y])]

## 223 without compression:
def p(g):e=enumerate;y,x=max((y+1,x+1)for y,r in e(g)for x,c in e(r)if c);s=4-0**g[y-1][x-4];v=-~len(h:=[*eval('filter(max,zip(*'*2+'g[:y-s]))))')])//s;return[[h[Y*v][X*v]and C for X,C in e(R[x-s:x])]for Y,R in e(g[y-s:y])]
