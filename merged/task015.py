# mwi (106 vs 98 bytes for gold)
p=lambda i,r=range(9):[i:=[[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r]for _ in i][3]

### combined (107 bytes)
p=lambda i,k=3,r=range(9):-k*i or p([[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r],k-1)

### att (111 bytes)
p=eval('lambda a:[[(b:=sum(a,()))[4]or(1in b[1::2])*7|4*(2in b[::2])'+'for*a,in map(zip,a[8:]+a,a,a[1:]+a)]'*2)

### ovs (119 bytes)
E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]
