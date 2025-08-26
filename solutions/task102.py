R=range;W=R(12)
def p(g):
 def t(C):
  for _ in W:C|={(a+d,A+D)for a,A in C for d,D in[(1,0),(-1,0),(0,1),(0,-1)]if-1<a+d<12>A+D>=0==g[a+d][A+D]}
  y,x=min(C);Y,X=max(C)
  if X-x==Y-y!=C=={(a,b)for a in R(y,Y+1)for b in R(x,X+1)}:
   for i,j in C:g[i][j]=2
 [g[i][j]or t({(i,j)})for i in W for j in W];return g