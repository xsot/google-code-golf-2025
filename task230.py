def p(m):
 for r in(R:=range(N:=len(m))):
  for c in R:
   for i,y,x in[(1,1,1),(2,1,-1),(3,-1,1),(4,-1,-1)]:
    if r+y<N>c+x>=m[r][c]==0<m[r+y][c+x]==5==m[r+y*2][c+x*2]:m[r][c]=i
 return m