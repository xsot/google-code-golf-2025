# compression_experiments (243 (261 unzipped) bytes, gold)
def p(i):
 t=r=f=0
 while i[f:]:
  if i[f]>i[0]:t=t or f;r=r or i[f:].index(i[0]);i[f-1:f+r]=[n for o in(0,-1,1,2)for d in(t-1,t)if 7not in sum(n:=[[i%7-2%~e for e,i in zip(e,i[:o%4%3]+i[o<0:]+[0])]for e,i in zip(i[f-1:f+r],i[d:])],[])][0];f+=r
  f+=1
 return i

### ovs (244 (261 unzipped) bytes)
def p(g):
 q=H=i=0
 while g[i:]:
  if g[i]>g[0]:q=q or i;H=H or g[i:].index(g[0]);g[i-1:i+H]=[A for O in(0,-1,1,2)for o in(q-1,q)if 7not in sum(A:=[[g%7-2%~R for R,g in zip(R,g[:O%4%3]+g[O<0:]+[0])]for R,g in zip(g[i-1:i+H],g[o:])],[])][0];i+=H
  i+=1
 return g

### joking (254 (318 unzipped) bytes)
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
