def p(g):[g and(y:=h,x:=r)for h,g in enumerate(g)for r,g in enumerate(g)];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and g for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

## 211 without compression:
exec(f"def p(g):f=sum(g,[]);s=0;A=[s:=s+y for y in f].index(s);N=len(g[0]);s=3-0**f[A-3];v=~len(h:=[*{'filter(max,zip(*'*2}g[:A//N-s]))))])//~s;return[[g*(h>0)"+"for h,g in zip(h[::v],g[A%sN-s:])]"*2%('%','//'))
