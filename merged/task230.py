# joking (114 bytes, gold)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub(f"0(?=, 0.{ {len(m)*3}}.5, 5)","3**i%5",str(p(m,i-1))))[::-1])]

### xsot (125 bytes)
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=.{%d}0, 5.{%d}5)"%((len(m)*3+1,)*2),"3421"[i],str(p(m,i-1)[::-1]))))]

##
def p(m):
 for r in(R:=range(N:=len(m))):
  for c in R:
   for i,y,x in[(1,1,1),(2,1,-1),(3,-1,1),(4,-1,-1)]:
    if r+y<N>c+x>=m[r][c]==0<m[r+y][c+x]==5==m[r+y*2][c+x*2]:m[r][c]=i
 return m

### combined (126 bytes)
p=lambda i,k=3,e=enumerate:-k*i or p([[y or-7**k%5*(i[-b][a-1]*i[1-b][a-2]>9)for b,y in e(x)]for a,x in e(zip(*i[::-1]))],k-1)

### ovs (144 bytes)
E=enumerate
p=lambda g:[[v+sum(k*((t:=(g+g)[i-(~-k&2)+1]+[0])[s:=j-(-1)**k]>t[j]|[*g[i],0][s])for k in(1,2,3,4))for j,v in E(r)]for i,r in E(g)]
