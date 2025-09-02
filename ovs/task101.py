def p(g):
 V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==C}for C in range(5)];[s.add(I)for I in[*M]*2for i in s|m if abs(I-i)in(1,20)]
 for i in M-s:
  A=min(len({*range(i-2*k,i+3*k,k)}&M)for k in(1,20));y=min(s);v|={N:=i-(y-max(s))*A}
  for I in m:
   if{k:=i-(y-I)*A*(N in M!=i not in{N}^v)}&V:g[k//20][k%20]=1
 return g
