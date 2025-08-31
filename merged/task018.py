# joking+mwi (332 (374 unzipped) bytes, gold)
E=enumerate
def p(g):
 def S(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in E(g)for j,v in E(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[S(T(x-j),G[x])==S(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((T:=lambda x:(x-a//4*x.real*2)*1j**a+O)(A-j))}for A in s)for x in s]
 return g

### ovs (374 bytes)
E=enumerate
def p(g):
 def S(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in E(g)for j,v in E(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[S(T(x-j),G[x])==S(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((T:=lambda x:(x-a//4*x.real*2)*1j**a+O)(A-j))}for A in s)for x in s]
 return g
