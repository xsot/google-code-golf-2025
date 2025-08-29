# att (88 vs 86 bytes for gold)
z=0,
p=lambda a:[*map(f:=lambda*b:[c|e|d>>2for c,d,e in zip(z+b,b,b[1:]+z)],*map(f,*a))]

### ovs (122 bytes)
E=enumerate
p=lambda g:[[5&82>>min((i-I)**2+(j-J)**2for I,R in E(g)for J,V in E(R)if V)**2for j,v in E(r)]for i,r in E(g)]
