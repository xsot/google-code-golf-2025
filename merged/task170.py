# compression_experiments (194 (236 unzipped) vs 180 bytes for gold)
def p(r):[(o:=i,f:=e)for i,r in enumerate(r)for e,r in enumerate(r)if r];n=0**r[o-3][f]-4;e=*filter(max,zip(*filter(max,zip(*r[:o-3])))),;return[[e and(r)for e,r in zip(e[::~len(e)//n],r[n-~f:])]for e,r in zip(e[::~len(e)//n],r[n-~o:])]

### joking (197 (236 unzipped) bytes)
# zip fiddling
def p(g):[(y:=r,x:=h)for r,g in enumerate(g)for h,g in enumerate(g)if g];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and(g)for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

## zips about the same
def p(g):[g and(y:=r,x:=h)for r,g in enumerate(g)for h,g in enumerate(g)];s=0**g[y-3][x]-3;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and(g)for h,g in zip(h[::~len(h)//~-s],g[s+x:])]for h,g in zip(h[::~len(h)//~-s],g[s+y:])]


##
def p(g):[#['g and','']##(#['y:=r,x:=h','x:=h,y:=r']##)for r,g in enumerate(g)for h,g in enumerate(g)#['if g'*(prev_vals[0]=='')]##];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and#[' g ','(g)']##for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

### ovs (197 (237 unzipped) bytes)
def p(g):[g and(y:=h,x:=r)for h,g in enumerate(g)for r,g in enumerate(g)];s=0**g[y-3][x]-4;h=*filter(max,zip(*filter(max,zip(*g[:y-3])))),;return[[h and g for h,g in zip(h[::~len(h)//s],g[s-~x:])]for h,g in zip(h[::~len(h)//s],g[s-~y:])]

## 204 without compression:
exec(f"def p(g):A=len(bytes(f:=sum(g,[])).rstrip(b'\\0'))-1;N=len(g[0]);s=3-0**f[A-3];*h,={'filter(any,zip(*'*2}g[:A//N-s]))));return[[g*(h>0)"+"for h,g in zip(h[::len(h)//s-1],g[A%sN-s:])]"*2%('%','//'))

### mwi (212 (246 unzipped) bytes)
def	p(g):y,x=max((y+1,x+1)for	y,g	in	enumerate(g)for	x,c	in	enumerate(g)if	c);s=4-0**g[y-1][x-4];v=-~len(h:=[*filter(max,zip(*filter(max,zip(*g[:y-s]))))])//s;return[[h[Y*v][X*v]and	g	for	X,g	in	enumerate(g[x-s:x])]for	Y,g	in	enumerate(g[y-s:y])]

##
def p(g):e=enumerate;y,x=max((y+1,x+1)for y,r in e(g)for x,c in e(r)if c);s=4-0**g[y-1][x-4];v=-~len(h:=[*filter(max,zip(*filter(max,zip(*g[:y-s]))))])//s;return[[h[Y*v][X*v]and C for X,C in e(R[x-s:x])]for Y,R in e(g[y-s:y])]

## a good bit longer, but almost tied due to compressing a lot better
def p(g):e=enumerate;I,J=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c]);s=3-0**g[I][J-3];y,*_,Y=[y for y,x in t if y<I-s or x<J-s];v=(Y+1-y)//(s+1);return[[g[y+v*n][min(x for y,x in t if y<I-s or x<J-s)+v*m]and c for m,c in e(r[J-s:J+1])]for n,r in e(g[I-s:I+1])]
def p(g):I,J=max(t:=[(y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c]);s=3-0**g[I][J-3];y,*_,Y=[y for y,r in enumerate(g)for x,c in enumerate(r)if c>0<I-s>y];v=(Y+2-y)//-~s;return[[g[y+v*n][min(x for y,r in enumerate(g)for x,c in enumerate(r)if c>0<I-s>y)+v*m]and c for m,c in enumerate(r[J-s:J+1])]for n,r in enumerate(g[I-s:I+1])]

### combined (242 (279 unzipped) bytes)
def p(g):
 e=enumerate;I,J=i,j=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c])
 while g[i-1][j-1]:i-=1;j-=1
 x=min(x for y,x in t if y<i or x<j);y,*_,Y=[y for y,x in t if y<i or x<j];s=(Y+1-y)//(I+1-i);return[[g[y+s*n][x+s*m]and c for m,c in e(r[j:J+1])]for n,r in e(g[i:I+1])]
