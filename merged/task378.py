# xsot (281 vs 145 bytes for gold)
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
