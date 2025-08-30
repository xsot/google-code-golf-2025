# att (75 vs 81 bytes for gold)
p=eval('lambda a:[[max(sum(a,()),key=bool)'+'for*a,in map(zip,a,a[5:])]'*2)

### joking+mwi (81 bytes)
p=eval('lambda a:[[next(filter(int,sum(a,())),0)'+'for*a,in map(zip,a,a[5:])]'*2)

### ovs (88 bytes)
p=lambda g:[[[*filter(abs,u),0][0]for u in zip(a,a[5:],b,b[5:])]for a,b in zip(g,g[5:])]
