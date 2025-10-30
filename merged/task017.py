# ovs (102 bytes, gold)
p=lambda g:[g:=[*zip(*[max(a*all(len({*r,0})<3for r in zip(b,a))for a in g)for b in g])]for _ in g][1]

##

R=range(21);p=lambda a:[[max(max(a[i%(n:=(s:=bytes(max(a,key=all))).find(s[:4],1))::n])[j%n::n])for j in R]for i in R]
R=range(21);p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
R=range(21);p=lambda g,K=-3:K*g or p([*zip(*[[[*map(sum,w)]for k in R if max(map(len,w:=[{*r[~i::k+1]}-{0}for i in R]))<2][0]for r in g])],K+1)

### mwi (118 bytes)
R=range(21);p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)

## Approach copied from task110, fails 1 testcase
p=lambda g,k=-3:k*g or p([*zip(*[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g])],k+1)

### att (120 bytes)
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)

### combined (120 bytes)
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
