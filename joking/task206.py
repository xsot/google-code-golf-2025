# 141
def p(g):
 W=len(g[0]);s=sum(G:=g,[]).index(5)+~W
 for _ in'  ':G=[r for*r,in zip(*G)if{*r}-{0,5}]
 for g[s//W][s%W:s%W+3]in G:s+=W
 return g

##
def p(g,E=enumerate):
 r,c=map(min,*[(a,b)for a,x in E(g)for b,y in E(x)if y%5or y>0==(s:=a,t:=b)])
 for i in-1,0,1:g[s+i][t-1:t+2]=g[r-~i][c:c+3]
 return g