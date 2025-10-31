# compression_experiments (199 (259 unzipped) vs 166 bytes for gold)
def p(i):g=max((len(n:=[(n,f)for n in range(21)for f in range(21)if i[n][f]==e]),n)for e in range(21)[1:])[1];return[[max(((a-l*r,e-l*o)in g)*i[n+r][f+o]for n,f in g for r in[-4,0,4]for o in[-4,0,4]for l in range(21)[1:])for e in range(21)]for a in range(21)]

### mwi (200 (259 unzipped) bytes)
def p(i):r=max((len(e:=[(e,a)for e in range(21)for a in range(21)if i[e][a]==g]),e)for g in range(21)[1:])[1];return[[max(((y-o*f,g-o*n)in r)*i[e+f][a+n]for e,a in r for f in[-4,0,4]for n in[-4,0,4]for o in range(21)[1:])for g in range(21)]for y in range(21)]

##

# 230b uncompressed
W=range(21)
t=-4,0,4
def p(g):R=max([(len(p:=[(i,j)for i in W for j in W if g[i][j]==x]),p)for x in W[1:]])[1];return[[max(((y-k*d,x-k*D)in R)*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:])for x in W]for y in W]

##

# replacing [1:4] with [1:] saves a byte at the cost of a lot of speed.
# for this version, that removal doesn't save after compression so i left in the 4
def p(g):R=max([{(i,j)for i in range(21)[x:x+3]for j in range(21)[y:y+3]if g[i][j]}for x in range(21)for y in range(21)],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in[-4,0,4]for D in[-4,0,4]for k in range(21)[1:4]for c in R)for x in range(21)]for y in range(21)]

##

p=lambda g:(R:=max([{(i,j)for i in range(21)[I:I+3]for j in range(21)[J:J+3]if g[i][j]}for I in range(21)for J in range(21)],key=len),[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in(-4,0,4)for D in(-4,0,4)for k in range(21)[1:]for c in R)for x in range(21)]for y in range(21)])[1]

### ovs (209 (280 unzipped) bytes)
# W[1:4] -> W[1:] possible golf. doesn't save a byte when compressed
def p(g):R=max([[(i,j)for i in range(21)[x:x+3]for j in range(21)[y:y+3]if g[i][j]]for x in range(21)for y in range(21)],key=len);return[[max(((y-k*d,x-k*D)in R)*g[i+d][j+D]for i,j in R for d in[-4,0,4]for D in[-4,0,4]for k in range(21)[1:4])for x in range(21)]for y in range(21)]

## 235 unzipped:
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max(((y-k*d,x-k*D)in R)*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:])for x in W]for y in W]

### joking (218 (289 unzipped) bytes)
# faster
def p(g):R=max([{(i,j)for i in range(21)[I:I+3]for j in range(21)[J:J+3]if g[i][j]}for I in range(21)for J in range(21)],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in[-4,0,4]for D in[-4,0,4]for k in range(21)[1:4]for c in R)for x in range(21)]for y in range(21)]

### xsot (223 (244 unzipped) bytes)
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:]for c in R)for x in W]for y in W]

### combined (223 (244 unzipped) bytes)
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:]for c in R)for x in W]for y in W]
