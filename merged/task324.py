# ovs (228 (261 unzipped) bytes, gold)
def p(g):k,K,b,B=T=sorted({*sum(g,[])},key=sum(g,[]).count);return[[([T[k!=C!=T[~all({k,B}!={*r}!={K,b}for r in[*zip(*g)]+g)]]for y,r in enumerate(g)for x,c in enumerate(r)if c in(k,K)!=abs(x-X)==abs(y-Y)]+[C])[0]for X,C in enumerate(r)]for Y,r in enumerate(g)]

## 237 unzipped:
def p(g,e=enumerate):s=sum(g,[]);k,K,b,B=T=sorted({*s},key=s.count);return[[([T[k!=C!=T[~all({k,B}!={*r}!={K,b}for r in[*zip(*g)]+g)]]for y,r in e(g)for x,c in e(r)if c in(k,K)!=abs(x-X)==abs(y-Y)]+[C])[0]for X,C in e(R)]for Y,R in e(g)]

### joking (253 (317 unzipped) bytes)
def	p(g):k,K,b,B=sorted({*sum(g,[])},key=sum(g,[]).count);b=[B,b][all({K,b}!={*r}!={k,B}for	r	in[*zip(*g)]+g)];[0for	y,r	in	enumerate(zip(*zip(*g)))for	x,r	in	enumerate(r)for	z,Y	in	enumerate(g)for	Y	in(-z,z)if	r	in(k,K)for	X	in(-z,z)if	len(g)>Y+y>-1<X+x<len(g[0])for	g[Y+y][X+x]in[(k,K)[k!=g[Y+y][X+x]!=b]]];return	g

##
def p(g):k,K,b,B=sorted({*sum(g,[])},key=sum(g,#['g','[]']##).count);b=[B,b][all({K,b}!={*r}!={k,B}for r in[*zip(*g)]+g)];[#[*range(10)]##for y,r in enumerate(zip(*zip(*g)))for x,r in enumerate(r)for z,#[*'_YX']## in enumerate(g)for Y in(-z,z)if r in(k,K)for X in(-z,z)if len(g)>Y+y>-1<X+x<len(g[0])for g[Y+y][X+x]in[(k,K)[k!=g[Y+y][X+x]!=b]]];return g

### mwi (288 (343 unzipped) bytes)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,s in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g

### combined (289 (343 unzipped) bytes)
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,_ in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g
