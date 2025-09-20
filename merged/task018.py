# ovs (301 (387 unzipped) bytes, gold)
def p(g):G={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g};[(s:={j},[abs(x-y)<2==s.add(x)for x in[*G]*5for y in[*s]],[*s][3:]and[5for a in[1,3,6,7]for O in G if all(G[A]in{max(f:=[G[j]for j in G],key=f.count),G.get((A-j-a//4*(A-j).real*2)*1j**a+O)}for A in s)for x in s for i,g[int(i.imag)][int(i.real)]in(((x-j-a//4*(x-j).real*2)*1j**a+O,G[x]),(x,0))])for j in G];return g

### mwi (313 (396 unzipped) bytes)
def	p(g):
	def	p(p,v):g[int(p.imag)][int(p.real)]=v
	G={i*1j+j:v	for	i,r	in	enumerate(g)for	j,v	in	enumerate(r)if	v}
	for	j	in	G:s={j};[abs(x-y)<2==s.add(x)for	x	in[*G]*5for	y	in[*s]];[*s][3:]and[p((x-j-a//4*(x-j).real*2)*1j**a+O,G[x])==p(x,0)for	a	in[1,3,6,7]for	O	in	G	if	all(G[A]in{max(G.values(),key=[*G.values()].count),G.get((A-j-a//4*(A-j).real*2)*1j**a+O)}for	A	in	s)for	x	in	s]
	return	g

##
def p(g):
 def p(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[p((x-j-a//4*(x-j).real*2)*1j**a+O,G[x])==p(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((A-j-a//4*(A-j).real*2)*1j**a+O)}for A in s)for x in s]
 return g

### combined (327 (374 unzipped) bytes)
E=enumerate
def p(g):
 def S(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in E(g)for j,v in E(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[S(T(x-j),G[x])==S(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((T:=lambda x:(x-a//4*x.real*2)*1j**a+O)(A-j))}for A in s)for x in s]
 return g
