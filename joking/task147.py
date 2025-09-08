p=lambda i:[*eval("map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*"*4+"i))))")]

##
p=lambda i,k=3:-k*i or[*map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*p(i,k-1))]