# brute force
def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(16+t%15-w):
  for s in 0,1:
   u=*map(list,g),
   for x in u[6:]:
    s+=any(x[t:w])
    for b in range(w-t):u[s][b+l]+=x[b+t]>4;x[b+t]=0
   if k:=p(u):return k
 if{*sum(g[:3],[])}=={1,2}:return g