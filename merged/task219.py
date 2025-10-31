# compression_experiments (242 (261 unzipped) vs 241 bytes for gold)
def p(o):
 e=n=i=0
 while o[i:]:
  if o[i]>o[0]:e=e or i;n=n or o[i:].index(o[0]);o[i-1:i+n]=[f for r in(0,-1,1,2)for t in(e-1,e)if 7not in sum(f:=[[o%7-2%~h for h,o in zip(h,o[:r%4%3]+o[r<0:]+[0])]for h,o in zip(o[i-1:i+n],o[t:])],[])][0];i+=n
  i+=1
 return o

### ovs (243 (261 unzipped) bytes)
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

### att (291 (307 unzipped) bytes)
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)

### combined (291 (307 unzipped) bytes)
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)
