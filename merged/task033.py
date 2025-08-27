p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]

### att (79 bytes)
r=range(17)
p=lambda a:[[a[i][j]or a[i%6][j%6]and a[5][5]for j in r]for i in r]
