# joking (88 vs 69 bytes for gold)
p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c^c-0**n>>d&4for c in b][::-1],*p(a,n-1))]

##
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c%(d+4)+(n>c)*4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=-63:n*a or[*map(lambda*b,d=0:[d:=c%(d+4)+(n==c)*4for c in b][::-1],*p(a,n+1))]
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c^c-(n>0)>>d&4for c in b][::-1],*n*a or p(a,n+1))]
p=lambda a,n=62:[*map(lambda*b,d=0:[d:=c^c+n//63>>d&4for c in b][::-1],*-n*a or p(a,n-1))]
p=lambda a,n=-62:[(d:=0)or[d:=c%(d+4)+(n>c)*4for c in a]for a[::-1]in zip(*n*a or p(a,n+1))]
p=lambda a,n=-62:[[(n>a[-1])*4+a.pop()%(c+4)for c in[0]+a[:0:-1]]for*a,in zip(*n*a or p(a,n+1))]

### xsot (93 bytes)
p=lambda a,n=-62:[*map(lambda*b,d=0:[(d:=c%(d+4)+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]

##
# by att
# innermost call will replace black with yellow
# remaining calls flood fill from black (d=0 initialises it from the border)
p=lambda a,n=-62:[*map(lambda*b,d=0:[(c%2|d//3)*(d:=c+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]
# equivalent to
p=lambda a,n=-62:[*map(lambda*b,d=0:[(c==3 or d>=3)*(d:=c+(c==0 and n==1)*4)for c in b][::-1],*n*a or p(a,n+1))]

##
# based on ovs
p=lambda g,k=79,s='04':-k*g or p([eval(str([0]+r).replace(*s))[1:]for*r,in zip(*g)][::-1],k-1,['0, 4','0, 0'])

def p(m):
 N=len(m:=eval(str(m).replace(*'04')))
 for i in range(N*N):
  q=(m[r:=i//N][c:=i%N]==4>1>c%~-N*(r%~-N))*[(r,c)]
  while q:
   m[r][c]=0;(y,x),*q=q
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
    if-1<i<N>j>-1<4==m[i][j]:m[i][j]=0;q+=(i,j),
 return m

### combined (93 bytes)
p=lambda a,n=-62:[*map(lambda*b,d=0:[(d:=c%(d+4)+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]

### att (98 bytes)
p=lambda a,n=-62:[*map(lambda*b,d=0:[(c%2|d//3)*(d:=c+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]

### ovs (121 bytes)
def p(g):g=eval(str(g).replace(*'04'));[g:=[[v%(q+4)for v,q in zip(r,[0]+r)]for*r,in zip(*g)][::-1]for _ in g*4];return g
