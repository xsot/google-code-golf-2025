# ovs (257 (316 unzipped) vs 244 bytes for gold)
def p(g):
 S=H=i=0
 while g[i:]:
  if g[i]>g[0]:
   H=H or g[i:].index(g[0]);s={(i+o,O)for o in range(H)for O in range(10)if g[i+o][O]};S=S or s;o,O=next((o,O)for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S)
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

### joking (276 (325 unzipped) bytes)
# zip fiddling
def p(i,n=0,k=0,t=2):
 f=len(r:=[i[k:]for i in i if(t:=~any(i)%3%-~t)*any(i)])
 for l in range(3,len(i)-f):
  for x in range(all(sum(q:=[[0**i+r*(i!=1)for i,r in zip(i[n:],r)]for i,r in zip(i[l:],r)],[sum([9in i[:2]for i in q]+i[l-1])<1]))*(len(i[0])-n-k)*f):i[l+x%f][x//f+n]=(-q[x%f][x//f]&9)%9
 return k*i or p(i,-~n%3,n>1)

##
def p(i,n=0,k=0):
 t=2;f=len(r:=[x[k:]for x in i if(t:=~any(x)%3%-~t)*any(x)])
 for l in range(3,len(i)-f):
  for x in range(all(sum(q:=[[0**i+r*(i!=1)for i,r in zip(i[n:],r)]for i,r in zip(i[l:],r)],[sum([9in x[:2]for x in q]+i[l-1])<1]))*(len(i[0])-n-k)*f):i[l+x%f][x//f+n]=(-q[x%f][x//f]&9)%9
 return k*i or p(i,-~n%3,n>1)

### att (289 (307 unzipped) bytes)
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)

### combined (289 (307 unzipped) bytes)
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)
