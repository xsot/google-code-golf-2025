# compression_experiments (258 (431 unzipped) bytes, gold)
def p(e):
 i,r,o,u,n=[{a+m*20for m,e in enumerate(e)for a,e in enumerate(e)if e==f}for f in range(5)]
 for f in o:u|={f for f in o for m in r|u if abs(f-m)in(1,20)}
 for f in o:b={f}-n and{f-min(len({f+m*(s-2)for s in range(5)}&o)for m in(1,20))*(min(u)-max(u))}&o;n|=b;e=[[e or a+m*20in(b and{f-min(len({f+m*(s-2)for s in range(5)}&o)for m in(1,20))*(min(u)-m)for m in r})for a,e in enumerate(e)]for m,e in enumerate(e)]
 return e

### ovs (259 (431 unzipped) bytes)
def p(g):
 f,m,M,s,v=[{j+I*20for I,g in enumerate(g)for j,g in enumerate(g)if g==i}for i in range(5)]
 for i in M:s|={i for i in M for I in m|s if abs(i-I)in(1,20)}
 for i in M:k={i}-v and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in(1,20))*(min(s)-max(s))}&M;v|=k;g=[[g or j+I*20in(k and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in(1,20))*(min(s)-I)for I in m})for j,g in enumerate(g)]for I,g in enumerate(g)]
 return g

##
def p(g):
 T=1,20;V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==C}for C in range(5)];[s.add(I)for I in[*M]*2for i in m|s if abs(I-i)in T]
 for i in M-s:
  A=min(len({*range(i-2*k,i+3*k,k)}&M)for k in T);N={i}-v and{i-A*(min(s)-max(s))}&M;v|=N
  for k in N and{i-A*(min(s)-I)for I in m}&V:g[k//20][k%20]=1
 return g

### joking (263 (444 unzipped) bytes)
def p(g):
 f,m,M,s,v=[{j+I*20for I in range(len(g))for j in range(len(g[I]))if g[I][j]==i}for i in range(5)]
 for i in M:s|={i for i in M for I in m|s if abs(i-I)in[1,20]}
 for i in M:k={i}-v and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in[1,20])*(min(s)-max(s))}&M;v|=k;g=[[g[I][j]or j+I*20in(k and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in[1,20])*(min(s)-I)for I in m})for j in range(len(g[I]))]for I in range(len(g))]
 return g

##
def p(g):
 f,m,M,s,v=[{j+I*#[20,21]##for I in range(len(g))for j in range(len(g[I]))if g[I][j]==n}for n in range(5)]
 for i in M:s|={i for i in M for I in m|s if abs(i-I)in[1,#[prev_vals[0]]##]}
 for i in M:k={i}-v and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in[1,#[prev_vals[0]]##])*(min(s)-max(s))}&M;v|=k;g=[[g[I][j]or j+I*#[prev_vals[0]]##in(k and{i-min(len({i+I*(n-2)for n in range(5)}&M)for I in[1,#[prev_vals[0]]##])*(min(s)-I)for I in m})for j in range(len(g[I]))]for I in range(len(g))]
 return g

### mwi (328 (464 unzipped) bytes)
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

### combined (333 (447 unzipped) bytes)
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
