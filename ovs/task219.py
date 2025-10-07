E=enumerate
def p(g):
 S=H=i=0
 while g[i:]:
  if g[i]>g[0]:
   H=H or g[i:].index(g[0]);s={(o,h)for o,O in E(g[i:i+H],i)for h,H in E(O)if H};S=S or s;o,O=next((o,O)for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S)
   for h,k in S-A:
    if-1<k+O<10:g[h+o][k+O]=1
   i+=H-1
  i+=1
 return g

## 283/309
def p(a,h=0):
 b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=zip(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*zip(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
 for m,n in zip(q,r):n[l:]=[x+(e*y>x)for x,y in zip(n[l:],m[l+j-i:]+u)]
 return h//52*a or p(a,h+1)
