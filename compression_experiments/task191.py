def p(a):
 i=[[*u]for u in zip(*a)if 1in u]
 i=[[*u]for u in zip(*i)if 1in u]
 for u in 0,1,0,1,0,1,0,1:a=u*a[::-1]or[[*u]for u in zip(*a)];[1for n,u in enumerate(a)for r,u in enumerate(a)for f,u in enumerate(all(a[n+f-1][r+e-1]==u&-2if 0<r+e<24>n+f>0else u<4for f,u in enumerate(i)for e,u in enumerate(u))*i)for e,u in enumerate(u)if 0<r+e<24>n+f>0for a[n+f-1][r+e-1]in[u]]
 return a