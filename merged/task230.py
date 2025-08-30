# joking+mwi (126 vs 115 bytes for gold)
p=lambda i,k=3,e=enumerate:-k*i or p([[y or-7**k%5*(i[-b][a-1]*i[1-b][a-2]>9)for b,y in e(x)]for a,x in e(zip(*i[::-1]))],k-1)

### ovs (144 bytes)
E=enumerate
p=lambda g:[[v+sum(k*((t:=(g+g)[i-(~-k&2)+1]+[0])[s:=j-(-1)**k]>t[j]|[*g[i],0][s])for k in(1,2,3,4))for j,v in E(r)]for i,r in E(g)]

### xsot (190 bytes)
def p(m):
 for r in(R:=range(N:=len(m))):
  for c in R:
   for i,y,x in[(1,1,1),(2,1,-1),(3,-1,1),(4,-1,-1)]:
    if r+y<N>c+x>=m[r][c]==0<m[r+y][c+x]==5==m[r+y*2][c+x*2]:m[r][c]=i
 return m
