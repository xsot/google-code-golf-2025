def p(g):
 T=1,20;V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==C}for C in range(5)];[s.add(I)for I in[*M]*2for i in m|s if abs(I-i)in T]
 for i in M-s:
  A=min(len({*range(i-2*k,i+3*k,k)}&M)for k in T);N={i}-v and{i-A*(min(s)-max(s))}&M;v|=N
  for k in N and{i-A*(min(s)-I)for I in m}&V:g[k//20][k%20]=1
 return g
