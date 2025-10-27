# joking (242 (256 unzipped) vs 239 bytes for gold)
# zip fiddling
def	p(g):
	r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
	for	l	in	range(t%15+16-w):
		for	s	in	1,0:
			u=*map(list,g),
			for	x	in	g[6:]:
				s+=any(x[t:w])
				for	b	in	range(t,w):g[s][b-t+l]+=x[b]>4;x[b]=0
			g=p(g)or	u
	if{*g[1]+g[2]}=={1,2}:return	g

##
def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(t%15#['+16-w','-w+16']##):
  for s in #['1,0','0,1']##:
   u=*map(list,g),
   for x in g[6:]:
    s+=any(x[t:w])
    for b in range(t,w):g[s][b-t+l]+=#['x[b]>4','4<x[b]']##;x[b]=0
   g=p(g)or u
 if{*#['g[1]+g[2]','g[2]+g[1]']##}=={#['1,2','2,1']##}:return g

### ovs (244 (256 unzipped) bytes)
def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(16+t%15-w):
  for s in 0,1:
   u=*map(list,g),
   for x in g[6:]:
    s+=any(x[t:w])
    for b in range(t,w):g[s][b-t+l]+=x[b]>4;x[b]=0
   g=p(g)or u
 if{*g[1]+g[2]}=={1,2}:return g

##

def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   A in p or 0in(x-y-4%y<=min(x-y for x,y in zip(A,c))for x,y in zip(A,c))or Q(o+len(A),p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*len(A)):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(b'\n%0s\n'%A)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=b'\n%0s\n'%bytes(K);S={*K.split(b'\n')};Q(0,{});return g
# the 0 in %0s is necessary to avoid variable substitution replacing the s with another letter

### garry_moss (288 (395 unzipped) bytes)
def p(p):
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in range(16):
  if(5in a[i::r])>i/r:p+=[i]
  elif p:i=[n for n in range(150)if a[n]>4and n%r in p];e+=[[n-i[0]for n in i]];p=[];n=[i+[n]for i in n for n in range(45)if 1>a[n]]
 for i in n:
  i=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in range(150)]
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in range(10)]

### mwi (336 (409 unzipped) bytes)
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   A in p or len(A)==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+len(A),p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*len(A)):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(b'\n'+A+b'\n')]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=b'\n'+bytes(K)+b'\n';S={*K.split(b'\n')};Q(0,{});return g

### combined (340 (391 unzipped) bytes)
t=b'\n'
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   h=len(A);A in p or h==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+h,p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*h):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(t+A+t)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=t+bytes(K)+t;S={*K.split(t)};Q(0,{});return g
