def p(g,E=enumerate):
 r,c=map(min,*[(a,b)for a,x in E(g)for b,y in E(x)if y%5or y>0==(s:=a,t:=b)])
 for i in-1,0,1:g[s+i][t-1:t+2]=g[r-~i][c:c+3]
 return g