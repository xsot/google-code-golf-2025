# joking+mwi (206 vs 150 bytes for gold)
import re
p=lambda i,k=7,r=re.sub:-k*i or p(eval(r((h:="("+"5, "*(n:=k%5)+"5)")+((s:=f"(.{ {34-n*3}})")+"(5, "+"0, "*n+"5)")*n+s+h,lambda m,s=1:"".join(r(str(s:=s^1),"2",z)for z in m.groups()),str(i))),k-1)

### ovs (310 bytes)
R=range;W=R(12)
def p(g):
 def t(C):
  for _ in W:C|={(a+d,A+D)for a,A in C for d,D in[(1,0),(-1,0),(0,1),(0,-1)]if-1<a+d<12>A+D>=0==g[a+d][A+D]}
  y,x=min(C);Y,X=max(C)
  if X-x==Y-y!=C=={(a,b)for a in R(y,Y+1)for b in R(x,X+1)}:
   for i,j in C:g[i][j]=2
 [g[i][j]or t({(i,j)})for i in W for j in W];return g
