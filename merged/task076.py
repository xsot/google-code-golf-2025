# compression_experiments (270 (384 unzipped) bytes, gold)
def	p(t):
	r={min(n:={g*1j+s:f	for	g,f	in	enumerate(t)for	s,f	in	enumerate(f)if	f},key=n.get)};e=n;[abs(s-g)<2!=r.add(g)for	g	in[*e]*6for	s	in[*r]]
	for	g,f	in	enumerate(t):
		for	s	in	e:o=min(n:={(s-g//4*s.real*2)*1j**g:e[s]^2for	s	in[*r]},key=n.get)-s;t=min(e.get(s-o,3)==13%-~n[s]^2for	s	in[*n])*[[n.get(g*1j+s+o,f^2)^2for	s,f	in	enumerate(f)]for	g,f	in	enumerate(t)]or	t
	return	t

### joking (272 (384 unzipped) bytes)
def	p(g):
	I={min(J:={i*1j+j:r	for	i,r	in	enumerate(g)for	j,r	in	enumerate(r)if	r},key=J.get)};G=J;[abs(j-i)<2!=I.add(i)for	i	in[*G]*6for	j	in[*I]]
	for	i,r	in	enumerate(g):
		for	j	in	G:P=min(J:={(j-i//4*j.real*2)*1j**i:G[j]^2for	j	in[*I]},key=J.get)-j;g=min(G.get(j-P,3)==13%-~J[j]^2for	j	in[*J])*[[J.get(i*1j+j+P,r^2)^2for	j,r	in	enumerate(r)]for	i,r	in	enumerate(g)]or	g
	return	g

##
def p(g):
 I={min(J:={i*1j+j:r for i,r in enumerate(g)for j,r in enumerate(r)if r},key=J.get)}#[';','\n ']##G=J#[';','\n ']##[abs(j-i)<2!=I.add(i)for i in[*#[*'GJ']##]*6for j in[*I]]
 for i,r in enumerate(g):
  for j in#['[*G]',' G']##:P=min(J:={(j-i//4*j.real*2)*1j**i:G[j]^2for j in[*I]},key=J.get)-j;g=min(G.get(j-P,3)==#[13,73]##%-~J[j]^2for j in[*J])*[[J.get(i*1j+j+P,r^2)^2for j,r in enumerate(r)]for i,r in enumerate(g)]or g
 return g

### ovs (276 (380 unzipped) bytes)
def p(g):
 I={min(J:={j+i*1j:I for i,r in enumerate(g)for j,I in enumerate(r)if I},key=J.get)};G=J;[abs(j-i)<2!=I.add(i)for i in[*G]*6for j in[*I]]
 for i,r in enumerate(g):
  for j in G:P=min(J:={(j-i//4*j.real*2)*1j**i:G[j]^2for j in I},key=J.get)-j;g=all(G.get(j-P,3)==13%-~J[j]^2for j in J)*[[J.get(i*1j+j+P,I^2)^2for j,I in enumerate(r)]for i,r in enumerate(g)]or g
 return g

### mwi (295 (381 unzipped) bytes)
def p(g):
 G={j+i*1j:v^2for i,r in enumerate(g)for j,v in enumerate(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a,r in enumerate(g):
  for I in G:P=min(J:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=J.get)-I;g=g*any(13%-~J[y]^G.get(y-P,1)for y in J)or[[J.get(i*1j+j+P,v^2)^2for j,v in enumerate(r)]for i,r in enumerate(g)]
 return g


##
E=enumerate
def p(g):
 G={j+i*1j:v^2for i,r in E(g)for j,v in E(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a in range(8):
  for I in G:P=min(J:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=J.get)-I;g=g*any(13%-~J[y]^G.get(y-P,1)for y in J)or[[J.get(i*1j+j+P,v^2)^2for j,v in E(r)]for i,r in E(g)]
 return g

### combined (305 (355 unzipped) bytes)
E=enumerate
def p(g):
 G={j+i*1j:v^2for i,r in E(g)for j,v in E(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a in range(8):
  for I in G:i=min(r:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=r.get)-I;g=g*any(13%-~r[y]^G.get(y-i,1)for y in r)or[[r.get(I*1j+j+i,v^2)^2for j,v in E(R)]for I,R in E(g)]
 return g
