# joking+mwi (244 (250 unzipped) vs 145 bytes for gold)
def p(g):
 for y in(u:=range(1,h:=len(g)-1)):
  for x in u:
   c=g[y][x];A,B,C,D=[c==g[y+Y][x+X]for Y,X in[[0,1],[0,-1],[1,0],[-1,0]]];a,b,p,q=2*C-1,2*A-1,x,y
   while(A^B)*(C^D)*(g[y+a][x+b]^c)*c>0<p<h>q>0:q-=a;p-=b;g[q][p]=g[y+2*a][x+2*b]
 return g

### xsot (281 bytes)
def p(m):
 n=len(m);(x,*_,X),(y,*_,Y)=map(sorted,zip(*[(r,c)for i in range(n*n)if m[r:=i//n][c:=i%n]]));a=[(x,y,-1,-1),(x,Y,-1,1),(X,y,1,-1),(X,Y,1,1)]
 for r,c,i,j in a:
  while n>c+j>-1<r+i<n:r+=i;c+=j;m[r][c]=min(set(sum(m,[]))-{0,sorted([m[u][v]for u,v,*_ in a])[1]})
 return m

###
def p(m):
    n = len(m)
    # bounding box
    rows, cols = zip(*[(r,c)for i in range(n*n)if m[r:=i//n][c:=i%n]])
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)

    # this gets us the color to use for the diagonal
    border = sorted([m[max_r][max_c],m[max_r][min_c],m[min_r][max_c],m[min_r][min_c]])[1]
    e = min(set(sum(m,[])) - {0, border})

    directions = [
        (min_r - 1, min_c - 1, -1, -1),
        (min_r - 1, max_c + 1, -1, 1),
        (max_r + 1, min_c - 1, 1, -1),
        (max_r + 1, max_c + 1, 1, 1),
    ]

    for r_start, c_start, dr, dc in directions:
        r, c = r_start, c_start
        while 0 <= r < n and 0 <= c < n:
            m[r][c] = e
            r += dr
            c += dc
    return m
