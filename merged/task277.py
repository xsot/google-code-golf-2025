# ovs (194 vs 164 bytes for gold)
def p(g):
 M=g*28
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:M[i]=s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];g[i//30][i%10]=3-M.count(s)
 return g

### combined (199 bytes)
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
