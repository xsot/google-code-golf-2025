# att (83 vs 86 bytes for gold)
p=lambda a:[*map(f:=lambda d,*b,c=0:[c|(c:=d)>>2|(d:=e)for e in[*b,0]],*map(f,*a))]

### joking+mwi (88 bytes)
z=0,
p=lambda a:[*map(f:=lambda*b:[c|e|d>>2for c,d,e in zip(z+b,b,b[1:]+z)],*map(f,*a))]

### ovs (122 bytes)
E=enumerate
p=lambda g:[[5&82>>min((i-I)**2+(j-J)**2for I,R in E(g)for J,V in E(R)if V)**2for j,v in E(r)]for i,r in E(g)]
