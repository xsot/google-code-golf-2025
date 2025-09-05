# att (197 vs 2500 bytes for gold)
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]

### combined (tied, 197 bytes)
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]
