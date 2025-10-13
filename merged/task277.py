# ovs (158 bytes, gold)
z=[0]
p=lambda g,k=-19,h=2,q=z*9:k*g or p([q:=[v and[v//sum(g,z).count(v),h:=h*64,*[P|p|v]*17,v%63][k]for P,p,v in zip(z+q,z+r,r)]for*r,in zip(*g[::-1])],k+1)

### att (166 bytes)
z=[0]
p=lambda g,k=-15,h=1,q=z*9:k*g or p([q:=[v and[2-v//max(f:=sum(g,z)),h:=h*2,*[P|p|v]*6,f.count(v)][k//2]for P,p,v in zip(z+q,z+r,r)]for*r,in zip(*g[::-1])],k+1)

### combined (199 bytes)
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
