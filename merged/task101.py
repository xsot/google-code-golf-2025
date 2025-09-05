# ovs (281 (338 unzipped) bytes, gold)
def p(g):
 T=1,20;V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==C}for C in range(5)];[s.add(I)for I in[*M]*2for i in m|s if abs(I-i)in T]
 for i in M-s:
  A=min(len({*range(i-2*k,i+3*k,k)}&M)for k in T);N={i}-v and{i-A*(min(s)-max(s))}&M;v|=N
  for k in N and{i-A*(min(s)-I)for I in m}&V:g[k//20][k%20]=1
 return g

### mwi (330 (464 unzipped) bytes)
def p(g):
 G=g
 for _ in' '*96:G=[r[::-1]for r in zip(*G[(0,)*len(G[0])in G[:min(y for y in range(len(G))if 1in G[y])]:])];h,w=len(G),len(G[0])
 for s in[3,2,1]:
  for y in range(15):
   for x in range(-2,12):
    m=[(H,W,G[H//s][W//s],len(g[0])>x+W>-1<y+H<len(g))for H in range(s*h)for W in range(s*w)]
    if all((2^u or V)*(V<1or(g[y+H][x+W]==2)==(u==2))for H,W,u,V in m):
     for H,W,u,V in m:
      if V:g[y+H][x+W]=u+u//2
 return eval(str(g).replace(*'32'))

### combined (335 (447 unzipped) bytes)
def p(g,R=range,l=len):
 G=g
 for _ in' '*96:G=[r[::-1]for r in zip(*G[(0,)*l(G[0])in G[:min(y for y in R(l(G))if 1in G[y])]:])];h,w=l(G),l(G[0])
 for s in[3,2,1]:
  for y in R(15):
   for x in R(-2,12):
    m=[(H,W,G[H//s][W//s],l(g[0])>x+W>-1<y+H<l(g))for H in R(s*h)for W in R(s*w)]
    if all((2^u or V)*(1>V or(g[y+H][x+W]==2)==(u==2))for H,W,u,V in m):
     for H,W,u,V in m:
      if V:g[y+H][x+W]=u+u//2
 return eval(str(g).replace(*'32'))
