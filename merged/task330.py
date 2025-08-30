# joking+mwi (139 vs 137 bytes for gold)
p=lambda i,k=179:-k*i or p([[{*[k:=k-1]*y}if k>78else[y and{*e}|y,118%~len(y)%3][k<1]for y,e in zip(x,[[],*x])]for x in zip(*i[::-1])],k-1)

### xsot (266 bytes)
def p(m):
 for i in range(99):
  z,*s=0,;q=(m[r:=i//10][c:=i%10]==5)*[(r,c)]
  while q:
   m[r][c]=9;(y,x),*q=q;z+=1;s+=(y,x),
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
    if-1<i<10>j>-1<5==m[i][j]:m[i][j]=9;q+=(i,j),
  for r,c in s:m[r][c]=1+(z==6)
 return m

# very similar to 369, but shorter since input size is constant
