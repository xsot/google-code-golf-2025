def p(g):
 e=enumerate;I,J=i,j=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c])
 while g[i-1][j-1]:i-=1;j-=1
 x=min(x for y,x in t if y<i or x<j);y,*_,Y=[y for y,x in t if y<i or x<j];s=(Y+1-y)//(I+1-i);return[[g[y+s*n][x+s*m]and c for m,c in e(r[j:J+1])]for n,r in e(g[i:I+1])]