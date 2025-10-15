# joking (79 bytes, gold)
p=lambda i,*w,r=[[0]*10]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or-i%8*w.count(5)%5

##
p=lambda i,r=[[0]*25]*25,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or sum(w)%8*i//8

### att (94 bytes)
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]

### combined (94 bytes)
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]

### ovs (123 bytes)
E=enumerate
p=lambda g:[[v*~sum(abs(j-J)+abs(i-I)==1for I,R in E(g)for J,V in E(R)if V)%8%5for j,v in E(r)]for i,r in E(g)]
