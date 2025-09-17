# ovs (143 bytes, gold)
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(f"0(?=({(s:='.%s0'%{3*len(i)+1})}, 0)*{s}, ., [^0]{s*2}, (.))","\\2",str(p(i,k-1)))))][::-1]

##

def p(g,k=-3):u=range(len(g)-2);[exec("q-=1;P-=1;g[q][P]=g[y+2][x+2];"*min(P:=x,q:=y)*(g[y+1][x+1]<g[y+1][x]&g[y][x+1]))for y in u for x in u];return g*k or p([*map(list,zip(*g[::-1]))],k+1)

### joking (144 bytes)
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(f"0(?=({(s:=f'.{ {3*len(i)+1}}0')}, 0)*{s}, ., [^0]{s*2}, (.))","\\2",str(p(i,k-1)))))][::-1]

### combined (190 bytes)
def p(g,k=-3):u=range(len(g)-2);[exec("q-=1;P-=1;g[q][P]=g[y+2][x+2];"*min(P:=x,q:=y)*(g[y+1][x+1]<g[y+1][x]&g[y][x+1]))for y in u for x in u];return g*k or p([*map(list,zip(*g[::-1]))],k+1)

### xsot (265 (281 unzipped) bytes)
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
