# joking (83 bytes, gold)
p=lambda i:[*eval("map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*"*4+"i))))")]

##
p=lambda i,k=3:-k*i or[*map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*p(i,k-1))]

### combined (87 bytes)
p=lambda i,k=3:-k*i or[(s:=0)or[-y%~s%8+(s:=y)for y in x]for x in zip(*p(i,k-1))][::-1]

### ovs (88 bytes)
p=lambda g,k=-3:g*k or p([[a+-a%~b%8for a,b in zip(r,[0]+r)]for*r,in zip(*g[::-1])],k+1)
