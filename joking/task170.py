# zip fiddling
def p(g):[(y:=r,x:=h)for r,g in enumerate(g)for h,g in enumerate(g)if g];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and(g)for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

## zips about the same
def p(g):[g and(y:=r,x:=h)for r,g in enumerate(g)for h,g in enumerate(g)];s=0**g[y-3][x]-3;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and(g)for h,g in zip(h[::~len(h)//~-s],g[s+x:])]for h,g in zip(h[::~len(h)//~-s],g[s+y:])]


##
def p(g):[#['g and','']##(#['y:=r,x:=h','x:=h,y:=r']##)for r,g in enumerate(g)for h,g in enumerate(g)#['if g'*(prev_vals[0]=='')]##];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and#[' g ','(g)']##for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]