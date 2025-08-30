def p(g,e=enumerate,d=[(r//3-1,r%3-1)for r in range(9)]):
 for a,r in e(g):
  for b,c in e(r[:-1]):
   if r[b-1]==r[b+1]==g[a-1][b]==g[a+1][b]>0 or g[a-1][b-1]==g[a+1][b-1]==g[a-1][b+1]==g[a+1][b+1]>0:
    for h,w in d:
     Y,X=a+h*4,b+w*4;f=max(g[y+Y][r+X]for y,r in d)
     for r in d:
      for y,r in d:
       if len(g)>y+Y>-1<r+X<len(g[0]):g[y+Y][r+X]=g[a+y][b+r]and f
      Y+=h*4;X+=w*4
    return g