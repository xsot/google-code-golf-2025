# xsot (226 (244 unzipped) vs 206 bytes for gold)
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:]for c in R)for x in W]for y in W]

### ovs (262 bytes)
W=range(21)
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[{(i+k*d,j+k*D):max(g[i+d][j+D]for i,j in R)for d in(-4,0,4)for D in(-4,0,4)for k in W[1:]for i,j in R}.get((y,x),g[y][x])for x in W]for y in W]
