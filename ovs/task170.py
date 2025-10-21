def p(g):[g and(y:=h,x:=r)for h,g in enumerate(g)for r,g in enumerate(g)];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and g for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

## 204 without compression:
exec(f"def p(g):A=len(bytes(f:=sum(g,[])).rstrip(b'\\0'))-1;N=len(g[0]);s=3-0**f[A-3];*h,={'filter(any,zip(*'*2}g[:A//N-s]))));return[[g*(h>0)"+"for h,g in zip(h[::len(h)//s-1],g[A%sN-s:])]"*2%('%','//'))
