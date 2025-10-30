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
