p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c^c-0**n>>d&4for c in b][::-1],*p(a,n-1))]

##
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c%(d+4)+(n>c)*4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=-63:n*a or[*map(lambda*b,d=0:[d:=c%(d+4)+(n==c)*4for c in b][::-1],*p(a,n+1))]
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c^c-(n>0)>>d&4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=62:[*map(lambda*b,d=0:[d:=c^c+n//63>>d&4for c in b][::-1],*-n*a or p(a,n-1))]
p=lambda a,n=-62:[(d:=0)or[d:=c%(d+4)+(n>c)*4for c in a]for a[::-1]in zip(*n*a or p(a,n+1))]
p=lambda a,n=-62:[[(n>a[-1])*4+a.pop()%(c+4)for c in[0]+a[:0:-1]]for*a,in zip(*n*a or p(a,n+1))]