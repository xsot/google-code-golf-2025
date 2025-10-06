# att (166 vs 164 bytes for gold)
z=[0]
p=lambda g,k=-15,h=1,q=z*9:k*g or p([q:=[v and[2-v//max(f:=sum(g,z)),h:=h*2,*[P|p|v]*6,f.count(v)][k//2]for P,p,v in zip(z+q,z+r,r)]for*r,in zip(*g[::-1])],k+1)

### ovs (167 bytes)
p=lambda g,k=-15,h=1,q=[0]*9:k*g or p([q:=[v and[2-v//max(f:=sum(g,[])),h:=h*2,*[P|p|v]*6,f.count(v)][k//2]for P,p,v in zip([0]+q,[0]+r,r)]for*r,in zip(*g[::-1])],k+1)

## 187
def p(g):
 *A,=enumerate(sum(g,M:=[]))
 for j,v in A*6:M+={0},;M[j]=s={(p:=y+y//10-j-j//10)*(abs(p-I)in b'\0\n'*v*V)for y,V in A for I in M[j]};g[j//10][j%10]=3&4>>M.count(s)
 return g

### combined (199 bytes)
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
