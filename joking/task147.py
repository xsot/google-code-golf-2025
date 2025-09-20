p=lambda i,r=[[0]*9]*9,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or-i%~max(w)%8+i

##
p=lambda i:[*eval("map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*"*4+"i))))")]
p=lambda i,k=3:-k*i or[*map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*p(i,k-1))]