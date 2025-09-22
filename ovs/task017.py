p=lambda g:[g:=[*zip(*[max(a*all(len({*r,0})<3for r in zip(b,a))for a in g)for b in g])]for _ in g][1]

##

R=range(21);p=lambda a:[[max(max(a[i%(n:=(s:=bytes(max(a,key=all))).find(s[:4],1))::n])[j%n::n])for j in R]for i in R]
R=range(21);p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
R=range(21);p=lambda g,K=-3:K*g or p([*zip(*[[[*map(sum,w)]for k in R if max(map(len,w:=[{*r[~i::k+1]}-{0}for i in R]))<2][0]for r in g])],K+1)
