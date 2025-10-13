# att (130 bytes, gold)
exec("p=lambda a:[[max({*max(a)}-{5})*any(a[i][j]%5or 2==sum(m-n-i+j+k%5==2<a[m][n]"+'for %s in range(10)%s'*6%(*'m n k)_)j]i]',))

### ovs (134 bytes)
exec("p=lambda a:[[max({*max(a)}-{5})*any(0<a[i][j]%5or 2==sum(m-n-i+j+k%5-2==0<a[m][n]"+'for %s in range(10)%s'*6%(*'m n k)_)j]i]',))

## +2 bytes, runtime/10:
exec("p=lambda a:[[max({*max(a)}-{5})*(0<a[i][j]%5or 2==sum(m-n-i+j+k%5-2==0<a[m][n]"+'for %s in range(10)%s'*5%(*'m n k','))',*'j]i]'))

### joking (140 bytes)
exec("p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j]or sum(m-n-i+j+k%5-2==0<a[m][n]"+'for %s in range(10)%s'*5%(*'m n k',')==2)',*'j]i]'))

##
exec("p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j])or 15&c*16>>2*sum(m-n-i+j+k%5-2==0<a[m][n]"+'for %s in range(10)%s'*5%(*'m n k)j]i]',))
s='for %s in range(10)';exec("p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j]or sum(m-n-i+j+k%5-2==0<a[m][n]"+f"{s*3})==2){s}]{s}]"%(*'mnkji',))

### combined (150 bytes)
r=range(10)
p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j]or sum(m-n-i+j+k%5-2==0<a[m][n]for m in r for n in r for k in r)==2)for j in r]for i in r]
