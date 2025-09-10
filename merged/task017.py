# ovs (118 vs 99 bytes for gold)
R=range(21)
p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)

##

R=range(21)
p=lambda g,K=-3:K*g or p([*zip(*[[[*map(sum,w)]for k in R if max(map(len,w:=[{*r[~i::k+1]}-{0}for i in R]))<2][0]for r in g])],K+1)

### att (120 bytes)
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)

### combined (120 bytes)
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
