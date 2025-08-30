# att (89 vs 86 bytes for gold)
p=lambda a:[*map(f:=lambda*b:[c|e|d>>2for c,d,e in zip([0,*b],b,b[1:]+(0,))],*map(f,*a))]

### ovs (122 bytes)
E=enumerate
p=lambda g:[[5&82>>min((i-I)**2+(j-J)**2for I,R in E(g)for J,V in E(R)if V)**2for j,v in E(r)]for i,r in E(g)]
