# att (104 vs 103 bytes for gold)
p=lambda a,n=35:-n*a or p([*map(lambda*b,d=0:[d:=c|d*(d==b[0]>n-3)for c in b[::-1]],*a[0in a[0]:])],n-1)

### combined (152 bytes)
p=lambda i,k=3,e=enumerate:-k*i or[[y or(x[0]in x[b:])*x[0]for b,y in e(x)]for x in zip(*p([*zip(*i[:min(n-1for n,s in e(i)if min(s)):-1])],k-1))][::-1]
