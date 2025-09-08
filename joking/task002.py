p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c%(d+4)+(n>c)*4for c in b][::-1],*n*a or p(a,n+1))]

##
p=lambda a,n=-63:n*a or[*map(lambda*b,d=0:[d:=c%(d+4)+(n==c)*4for c in b][::-1],*p(a,n+1))]