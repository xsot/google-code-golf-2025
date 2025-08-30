# att (94 vs 89 bytes for gold)
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]

### combined (tied, 94 bytes)
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]

### ovs (182 bytes)
def p(g):
 def t(*I):
  for i in I:
   if(r:=g[i//h%h])[i%h]==1:r[i%h]=0;t(i+1,i-1,i+h,i-h)
 h=len(g);g=[[v or 1 for v in l]for l in g];[t(a*h,a,a*h-1,a-h)for a in range(h)];return g
