def p(g):
 q=H=i=0
 while g[i:]:
  if g[i]>g[0]:q=q or i;H=H or g[i:].index(g[0]);g[i-1:i+H]=[A for O in(0,-1,1,2)for o in(q-1,q)if 7not in sum(A:=[[g%7-2%~R for R,g in zip(R,g[:O%4%3]+g[O<0:]+[0])]for R,g in zip(g[i-1:i+H],g[o:])],[])][0];i+=H
  i+=1
 return g
