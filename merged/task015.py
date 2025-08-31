# combined (107 vs 98 bytes for gold)
p=lambda i,k=3,r=range(9):-k*i or p([[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r],k-1)

### ovs (119 bytes)
E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]
