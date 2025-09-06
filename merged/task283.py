# att (94 vs 82 bytes for gold)
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]

### combined (tied, 94 bytes)
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]

### ovs (123 bytes)
E=enumerate
p=lambda g:[[v*~sum(abs(j-J)+abs(i-I)==1for I,R in E(g)for J,V in E(R)if V)%8%5for j,v in E(r)]for i,r in E(g)]
