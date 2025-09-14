# att (153 vs 159 bytes for gold)
s='for %s,b in enumerate(%s)'
exec(f"p=lambda a:max([j>i,-(C:=sum(g:=[[b|6*(i<=m<=j)*(k<=n<=l){s}]{s}],a).count)(7),C(6),g]{s*4})[3]"%(*'nbmaiakbjalb',))

##
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]

### joking (156 bytes)
s='for %s,b in enumerate(%s)';exec(f"p=lambda a:min([j<=i,(C:=str(g:=[[b|6*(i<=m<=j)*(k<=n<=l){s}]{s}]).count)('7'),-C('6'),g]{s*4})[3]"%(*'nbmaiakbjalb',))

### ovs (189 bytes)
e=enumerate
p=lambda a:min([j<=i,(C:=str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]).count)('7'),-C('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b))[3]

### combined (197 bytes)
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]
