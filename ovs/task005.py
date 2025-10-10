# W[1:4] -> W[1:] possible golf. doesn't save a byte when compressed
def p(g):R=max([[(i,j)for i in range(21)[x:x+3]for j in range(21)[y:y+3]if g[i][j]]for x in range(21)for y in range(21)],key=len);return[[max(((y-k*d,x-k*D)in R)*g[i+d][j+D]for i,j in R for d in[-4,0,4]for D in[-4,0,4]for k in range(21)[1:4])for x in range(21)]for y in range(21)]

## 235 unzipped:
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max(((y-k*d,x-k*D)in R)*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:])for x in W]for y in W]
