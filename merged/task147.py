# ovs (73 bytes, gold)
*r,p=[0]*9,lambda i,*w:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(3in w)+7&i*9

##
p=lambda g,k=-3:g*k or p([[a+-a%~b%8for a,b in zip(r,[0]+r)]for*r,in zip(*g[::-1])],k+1)

### joking (74 bytes)
p=lambda i,*w,r=[[0]*9]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(3in w)+7&i*9


##
p=lambda i,r=[[0]*9]*9,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or-i%~max(w)%8+i
p=lambda i:[*eval("map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*"*4+"i))))")]
p=lambda i,k=3:-k*i or[*map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*p(i,k-1))]

### combined (87 bytes)
p=lambda i,k=3:-k*i or[(s:=0)or[-y%~s%8+(s:=y)for y in x]for x in zip(*p(i,k-1))][::-1]
