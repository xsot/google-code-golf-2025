# joking (285 (456 unzipped) bytes, gold)
def	p(g):
	for	G	in	60*[g]:g=[[*G]for	G	in	zip(*g[max(map(len,str(g[0]).split('0')))<12:][::-1])]
	for	G	in	60*[[v[x:x+3]for	v	in	G[y:y+3]]for	y,p	in	enumerate(G[2:])for	x,p	in	enumerate(p[2:])][::-1]:
		for	y,p	in	enumerate(g*({*sum(G,[])}^{0}>{2,0})):
			for	x,p	in	enumerate(p):
				for	n,p	in	enumerate(G*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for	n,p	in	enumerate(G)for	m,p	in	enumerate(p))):g[n+y][x:x+3],*G=p,
		G[:]=[[*G]for	G	in	zip(*G[::-1])]
	return	g

##
def p(g):
 for G in #[*range(60,100,4)]##*[g]:g=[[*G]#['','[::-1]']##for G in zip(*g[max(map(len,str(g[0]).split('0')))<12:]#[*{'','[::-1]'*('[::-1]'not in prev_vals[-1:])}]##)]#['[::-1]'*('[::-1]'not in prev_vals[-2:])]##
 for G in #[prev_vals[0]]##*[[v[x:x+3]for v in G[y:y+3]]for y,p in enumerate(G[2:])for x,p in enumerate(p[2:])][::-1]:
  for y,p in enumerate(g*({*sum(G,[])}^{0}>{2,0})):
   for x,p in enumerate(p):
    for n,p in enumerate(G*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in enumerate(G)for m,p in enumerate(p))):g[n+y][x:x+3],*G=p,
  G[:]=[[*G]#['','[::-1]']##for G in zip(*G#['[::-1]'*('[::-1]'!=prev_vals[-1])]##)]
 return g

### ovs (297 (394 unzipped) bytes)
e=enumerate
def p(g):
 for G in[g]*60:*g,=map(list,zip(*g[max(map(len,str(g[0]).split('0')))<12:][::-1]))
 for s in [[v[x:x+3]for v in G[y:y+3]]for y,p in e(G[2:])for x,p in e(p[2:])][::-1]*4:
  for y,p in e(g*({*sum(s,s[0])}^{0}>{2,0})):
   for x,p in e(p):
    for n,p in e(s*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in e(s)for m,p in e(p))):g[n+y][x:x+3],*s=p,
  s[:]=zip(*s[::-1])
 return g

### xsot (304 (465 unzipped) bytes)
e=enumerate
def p(g):
 w=[(y,x,s)for y,p in e(g[:-2])for x,p in e(p[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0,
 u=[[y[0]for y in zip(x,*g)if sum(y)]for x in g if sum(x)]
 for y,x,s in w[::-1]:
  for n,p in e(s*4):
   for y,p in e(u):
    for x,p in e(p):
     for n,p in e(s*all((2*(2*u)[n+y])[m+x]==2*(2!=r)for n,p in e(s)for m,r in e(p))):u[n+y][x:x+3]=p;s=[]
   s=*zip(*s[::-1]),
 return u

### mwi (324 (460 unzipped) bytes)
def p(g):
 e=enumerate;w=[(y,x,s)for y,r in e(g[:-2])for x,c in e(r[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0;u=[[y[0]for y in zip(x,*g)if any(y)]for x in g if any(x)]
 for y,x,s in w[::-1]:
  for p in'p in':
   for Y,R in e(u):
    for X,p in e(R):
     for n,j in e(s*all(((u*2)[n+Y]*2)[m+X]==2*(2!=r)for n,j in e(s)for m,r in e(j))):u[n+Y][X:X+3]=j;s=[]
   s=*zip(*s[::-1]),
 return u

### combined (325 (460 unzipped) bytes)
def p(g):
 e=enumerate;w=[(y,x,s)for y,r in e(g[:-2])for x,c in e(r[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,_ in e(s):g[y+n][x:x+3]=0,0,0;u=[[y[0]for y in zip(x,*g)if any(y)]for x in g if any(x)]
 for y,x,s in w[::-1]:
  for _ in'_ in':
   for Y,R in e(u):
    for X,_ in e(R):
     for n,j in e(s*all(((u*2)[n+Y]*2)[m+X]==2*(2!=r)for n,j in e(s)for m,r in e(j))):u[n+Y][X:X+3]=j;s=[]
   s=*zip(*s[::-1]),
 return u

### garry_moss (367 (561 unzipped) bytes)
def p(u):
 i=range(9);c={};f=lambda a:[a(p,s,[u[p+a//3][s+a%3]for a in i])for p in range(len(u)-2)for s in range(len(u[0])-2)]
 def p(p,s,n):
  if len(r:={*n})==2and r&{0,2}=={2}:
   n=tuple(a==2for a in n);k={n:sum(r)-2}
   for a in range(4):c[n]=k;n=tuple(n[a%3*3+2-a//3]for a in i)
   for a in i:u[p+a//3][s+a%3]=0
 f(p);u=[*map(list,zip(*filter(any,[*map(list,zip(*filter(any,u)))])))];[f(lambda p,s,n:(t:=c.get(n:=tuple(a==0for a in n)))and(a or n in t)and(r:=t.popitem()[1],[u[p+a//3].__setitem__(s+a%3,(r,2)[n[a]])for a in i]))for a in range(2)];return u
