# att (144 vs 115 bytes for gold)
E=enumerate
p=lambda g:[[v+sum(k*((t:=(g+g)[i-(~-k&2)+1]+[0])[s:=j-(-1)**k]>t[j]|[*g[i],0][s])for k in(1,2,3,4))for j,v in E(r)]for i,r in E(g)]

### xsot (190 bytes)
def p(m):
 for r in(R:=range(N:=len(m))):
  for c in R:
   for i,y,x in[(1,1,1),(2,1,-1),(3,-1,1),(4,-1,-1)]:
    if r+y<N>c+x>=m[r][c]==0<m[r+y][c+x]==5==m[r+y*2][c+x*2]:m[r][c]=i
 return m
