# ovs (280 (380 unzipped) vs 276 bytes for gold)
def p(g):
 I={min(J:={j+i*1j:I for i,r in enumerate(g)for j,I in enumerate(r)if I},key=J.get)};G=J;[abs(j-i)<2!=I.add(i)for i in[*G]*6for j in[*I]]
 for i,r in enumerate(g):
  for j in G:P=min(J:={(j-i//4*j.real*2)*1j**i:G[j]^2for j in I},key=J.get)-j;g=all(13%-~J[j]^G.get(j-P,3)==2for j in J)*[[J.get(i*1j+j+P,I^2)^2for j,I in enumerate(r)]for i,r in enumerate(g)]or g
 return g

### joking (283 (381 unzipped) bytes)
# variable renaming
def p(g):
 G={j+i*1j:I^2for i,r in enumerate(g)for j,I in enumerate(r)if I};[abs(j-i)<2!=I.add(i)for j in G if G[j]%2if[I:={j}]for i in[*G]*6for j in[*I]]
 for i,r in enumerate(g):
  for j in G:P=min(J:={(j-i//4*j.real*2)*1j**i:G[j]for j in I},key=J.get)-j;g=g*any(13%-~J[j]^G.get(j-P,1)for j in J)or[[J.get(i*1j+j+P,I^2)^2for j,I in enumerate(r)]for i,r in enumerate(g)]
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
