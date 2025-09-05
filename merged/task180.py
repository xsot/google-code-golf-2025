# att (81 vs 2500 bytes for gold)
p=eval('lambda a:[[max(sum(a+a,())[1:],key=bool)'+'for*a,in map(zip,a,a[4:])]'*2)

### combined (tied, 81 bytes)
p=eval('lambda a:[[max(sum(a+a,())[1:],key=bool)'+'for*a,in map(zip,a,a[4:])]'*2)

### ovs (82 bytes)
p=lambda g:[[max(x,key=bool)for x in zip(r[4:],R,R[4:],r)]for r,R in zip(g,g[4:])]

### xsot (84 bytes)
p=lambda m:[[r[c+4]or R[c]or R[c+4]or r[c]for c in range(4)]for r,R in zip(m,m[4:])]
##
p=lambda m:[[r[c+4]or R[c]or R[c+4]or r[c]for c in range(4)]for r,R in zip(m,m[4:])]
p=lambda m,R=range(4):[[m[r][c+4]or m[r+4][c]or m[r+4][c+4]or m[r][c]for c in R]for r in R]
