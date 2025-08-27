E=enumerate
def p(g):
 I,J,W,*C=next((i,j,3+(r[j+3]>0))for i,r in E(g)for j,_ in E(r)if[*{*all(s:=r[j:j+3]+g[i+1][j:j+3])*s}][1:])
 for r in g[I:I+W]:C+=r[J:J+W],;r[J:J+W]=[0]*W
 [g:=[r for*r,in zip(*g)if any(r)]for _ in'  '];B=len(g)//W;return[[V*(v>0)for v,V in zip(r[::B],R)]for r,R in zip(g[::B],C)]