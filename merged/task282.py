# joking (76 vs 74 bytes for gold)
p=lambda i,*x,c=0:[c|(c:=i)>>2|(i:=y)for y in x+x[7:]]or[*map(p,*map(p,*i))]

### att (83 bytes)
p=lambda a:[*map(f:=lambda d,*b,c=0:[c|(c:=d)>>2|(d:=e)for e in[*b,0]],*map(f,*a))]

### combined (83 bytes)
p=lambda a:[*map(f:=lambda d,*b,c=0:[c|(c:=d)>>2|(d:=e)for e in[*b,0]],*map(f,*a))]

### ovs (122 bytes)
E=enumerate
p=lambda g:[[5&82>>min((i-I)**2+(j-J)**2for I,R in E(g)for J,V in E(R)if V)**2for j,v in E(r)]for i,r in E(g)]
