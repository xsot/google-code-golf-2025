import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=.{%d}0, 5.{%d}5)"%((len(m)*3+1,)*2),"3421"[i],str(p(m,i-1)[::-1]))))]

##
def p(m):
 for r in(R:=range(N:=len(m))):
  for c in R:
   for i,y,x in[(1,1,1),(2,1,-1),(3,-1,1),(4,-1,-1)]:
    if r+y<N>c+x>=m[r][c]==0<m[r+y][c+x]==5==m[r+y*2][c+x*2]:m[r][c]=i
 return m