p=lambda a:[[r[j]or r[j+5]or s[j]or s[j+5]for j in(0,1,2,3)]for r,s in zip(a,a[5:])]

### ovs (88 bytes)
p=lambda g:[[[*filter(abs,u),0][0]for u in zip(a,a[5:],b,b[5:])]for a,b in zip(g,g[5:])]
