def p(g):
 w=len(g[0]);I=0,1,2,w,w+1,w+2,2*w,w-~w,2*w+2;O=[[*I]for _ in I];f=sum(g,[]);i=0
 for v in f:
  if v:
   P=b'@6!9<@\0'[hash((*(f[i+o]!=5for o in I),))%11]
   for o in I:O[P//9+o//w][P%9+o%w]=f[i+o];f[i+o]=0
  i+=1
 return O