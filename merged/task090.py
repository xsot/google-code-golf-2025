# ovs (189 vs 159 bytes for gold)
e=enumerate
p=lambda a:min([j<=i,(C:=str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]).count)('7'),-C('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b))[3]

### att (197 bytes)
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]

### combined (197 bytes)
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]
