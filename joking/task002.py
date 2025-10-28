p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c^c-0**n>>d&4for c in b][::-1],*p(a,n-1))]

##
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c%(d+4)+(n>c)*4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=-63:n*a or[*map(lambda*b,d=0:[d:=c%(d+4)+(n==c)*4for c in b][::-1],*p(a,n+1))]
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c^c-(n>0)>>d&4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=62:[*map(lambda*b,d=0:[d:=c^c+n//63>>d&4for c in b][::-1],*-n*a or p(a,n-1))]
p=lambda a,n=-62:[(d:=0)or[d:=c%(d+4)+(n>c)*4for c in a]for a[::-1]in zip(*n*a or p(a,n+1))]
p=lambda a,n=-62:[[(n>a[-1])*4+a.pop()%(c+4)for c in[0]+a[:0:-1]]for*a,in zip(*n*a or p(a,n+1))]

p=lambda a,n=11:-n*a or[(d:=0)or[d:=c^c-0**n>>d&4for c in b][::-1]for*b,in zip(*p(a,n-1))]
p=lambda a,n=11,d=0:-n*a or[[d:=c^c-0**n>>d&4for c in[0]+b][:0:-1]for*b,in zip(*p(a,n-1))]
p=lambda a,n=-66:[eval(str([0]+b).replace(*n*"04"or["0, 4","0,0"]))[:0:-1]for*b,in zip(*n*a or p(a,n+1))]
p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c*(c==3or d>0)or(d>0==n)*4for c in b][::-1],*p(a,n-1))]
p=lambda a,n=10:~n*a or[*map(lambda*b,d=0:[d:=c*(c==3or d>0)or(d>0>n)*4for c in b][::-1],*p(a,n-1))]
p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=(c or 0**n*4)*(c&3|d>0)for c in b][::-1],*p(a,n-1))]
p=lambda a,*b,n=11,d=0:[d:=c^c-0**a>>d&4for c in b][::-1]or-n*a or[*map(p,[n]*20,*p(a,n=n-1))]

p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c&3|(0is c)*4or d>0and c for c in b][::-1],*p(a,n-1))]
p=lambda a,n=11:-n*a or[[n:=c&3|(0is c)*4or n>0and c for c in[0>1]+b][:0:-1]for*b,in zip(*p(a,n-1))]