def p(m):
 n=len(m)
 for i in range(n*n):m[r][c]=m[r:=i//n][c:=i%n]or(sum([*zip(*m)][c])>0)*8
 return[l*2for l in m]*2