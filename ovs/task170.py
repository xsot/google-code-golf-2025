def p(g):y,x=max((h,r)for h,g in enumerate(g)for r,g in enumerate(g)if g);s=4-0**g[y][x-3];v=-~len(h:=[*filter(max,zip(*filter(max,zip(*g[:y+1-s]))))])//s;return[[h and g for h,g in zip(h[::v],g[-s-~x:])]for h,g in zip(h[::v],g[-s-~y:])]

## 223 without compression:
def p(g):e=enumerate;y,x=max((y+1,x+1)for y,r in e(g)for x,c in e(r)if c);s=4-0**g[y-1][x-4];v=-~len(h:=[*eval('filter(max,zip(*'*2+'g[:y-s]))))')])//s;return[[h[Y*v][X*v]and C for X,C in e(R[x-s:x])]for Y,R in e(g[y-s:y])]
