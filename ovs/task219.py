def p(g):
 S=H=i=0
 while g[i:]:
  if g[i]>g[0]:
   H=H or g[i:].index(g[0]);s={(i+o,O)for o in range(H)for O in range(10)if g[i+o][O]};S=S or s;o,O=next((o,O)for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S)
   for h,k in S-A:
    if-1<k+O<10:g[h+o][k+O]=1
   i+=H
  i+=1
 return g

## 262/292
def p(g):
 S=H=i=0
 while g[i:]:
  if g[i]>g[0]:H=H or g[i:].index(g[0]);s={(a,o//H)for o in range(H*10)if g[a:=i+o%H][o//H]};S=S or s;next([0for h,k in S-A if-1<k+O<10for g[h+o][k+O]in[1]]for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S);i+=H
  i+=1
 return g

## 244/244 with 8 failures: doesn't handle the case where the first row a pattern is missing completely
def p(g):
 o=H=i=0
 while g[i:]:
  if g[i]>g[0]:o=o or i;H=H or g[i:].index(g[0]);g[i:i+H]=[A for O in(0,-1,1,2)if(A:=[[y%7-2%~x for x,y in zip(R,r[:O%4%3]+r[O<0:]+[0])]for R,r in zip(g[i:],g[o:o+H])])if'7'not in'%s'%A][0];i+=H
  i+=1
 return g
