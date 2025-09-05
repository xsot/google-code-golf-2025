# mwi (238 (270 unzipped) vs 2500 bytes for gold)
def p(g):e=enumerate;I,J=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c]);s=3-0**g[I][J-3];x=min(x for y,x in t if y<I-s or x<J-s);y,*_,Y=[y for y,x in t if y<I-s or x<J-s];v=(Y+1-y)//(s+1);return[[g[y+v*n][x+v*m]and c for m,c in e(r[J-s:J+1])]for n,r in e(g[I-s:I+1])]

### combined (243 (279 unzipped) bytes)
def p(g):
 e=enumerate;I,J=i,j=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c])
 while g[i-1][j-1]:i-=1;j-=1
 x=min(x for y,x in t if y<i or x<j);y,*_,Y=[y for y,x in t if y<i or x<j];s=(Y+1-y)//(I+1-i);return[[g[y+s*n][x+s*m]and c for m,c in e(r[j:J+1])]for n,r in e(g[i:I+1])]

### ovs (269 (303 unzipped) bytes)
E=enumerate
def p(g):
 I,J,W,*C=next((i,j,3+(r[j+3]>0))for i,r in E(g)for j,_ in E(r)if[*{*all(s:=r[j:j+3]+g[i+1][j:j+3])*s}][1:])
 for r in g[I:I+W]:C+=r[J:J+W],;r[J:J+W]=[0]*W
 [g:=[r for*r,in zip(*g)if any(r)]for _ in'  '];B=len(g)//W;return[[V*(v>0)for v,V in zip(r[::B],R)]for r,R in zip(g[::B],C)]
