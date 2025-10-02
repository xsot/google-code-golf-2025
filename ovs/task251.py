p=lambda a,n=-42:[[max(n,14>>d&b.pop())for d in[0]+b[:0:-1]]for*b,in zip(*n*a or p(a,n+1))]

##

def p(g):
 def t(*I):
  for i in I:
   if(r:=g[i//h%h])[i%h]==1:r[i%h]=0;t(i+1,i-1,i+h,i-h)
 h=len(g);g=[[v or 1 for v in l]for l in g];[t(a*h,a,a*h-1,a-h)for a in range(h)];return g
