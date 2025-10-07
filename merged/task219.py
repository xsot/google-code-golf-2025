# joking (254 (318 unzipped) vs 244 bytes for gold)
def	p(g):
	t=S=i=0
	while	g[i:]:
		if	g[0]<g[i]:
			t=t	or	g[i:].index(g[0]);s={(o,O)for	o	in	range(i,i+t)for	O	in	range(10)if	g[o][O]};S=S	or	s;o,O=next((o,O)for	O	in(0,-1,1,2)for	o	in	range(i)if(A:={(h-o,H-O)for	h,H	in	s	if-1<H-O<10})<=S)
			for	h,H	in	S-A:
				if-1<H--O<10:g[o+h][H--O]=1
			i+=t-1
		i+=1
	return	g

##
def p(g):
 #[*perms('S=t=i','=')]##=0
 while g[i:]:
  if g[0]<g[i]:
   t=t or g[i:].index(g[0])#[';','\n   ']##s={(o,O)for o in range(i,i+t)for O in range(10)if g[o][O]}#[';','\n   ']##S=S or s#[';','\n   ']##o,O=next((o,O)for O in(0,-1,1,2)for o in range(i)if(A:={(h-o,H-O)for h,H in s if-1<H-O<10})<=S)
   for h,H in S-A:
    if-1<H--O<10:g[o+h][H--O]=1
   i+=t-1
  i+=1
 return g

### ovs (257 (316 unzipped) bytes)
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
