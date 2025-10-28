def p(g):G={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g};[(s:={J},[abs(x-y)<2==s.add(x)for x in[*G]*5for y in[*s]],[*s][3:]and[5for a in[1,3,6,7]for O in G if all(sum(G[x]==G.get(j)for j in[*s,(x-J-a//4*(x-J).real*2)*1j**a+O])>1for x in s)for x in s if(g:=[[{x:0,(x-J-a//4*(x-J).real*2)*1j**a+O:G[x]}.get(i*1j+j,g)for j,g in enumerate(g)]for i,g in enumerate(g)])])for J in G];return g

##
def p(g):G={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g};[(s:={j},[abs(x-y)<2==s.add(x)for x in[*G]*5for y in[*s]],[*s][3:]and[5for a in[1,3,6,7]for O in G if all(sum(G[x]==G.get(j)for j in[*s,(x-j-a//4*(x-j).real*2)*1j**a+O])>1for x in s)for x in s for i,g[int(i.imag)][int(i.real)]in(((x-j-a//4*(x-j).real*2)*1j**a+O,G[x]),(x,0))])for j in G];return g

##
def p(g):G={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g};[(s:={j},[abs(x-y)<2==s.add(x)for x in[*G]*5for y in[*s]],[*s][3:]and[5for a in[1,3,6,7]for O in G if all(G[x]in{max(f:=[G[j]for j in G],key=f.count),G.get((x-j-a//4*(x-j).real*2)*1j**a+O)}for x in s)for x in s for i,g[int(i.imag)][int(i.real)]in(((x-j-a//4*(x-j).real*2)*1j**a+O,G[x]),(x,0))])for j in G];return g
