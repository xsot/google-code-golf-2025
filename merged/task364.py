# ovs (156 vs 163 bytes for gold)
p=lambda i,k=39:-k*i or p([[[y.bit_count()*5%14%9,y and(u*t>0)<<k%4+2|y|u][k>0]for y,t,u in zip(x,[0,*x],s)]for*x,s in zip(*i,[[0]*99,*zip(*i)])][::-1],k-1)

### joking+mwi (163 bytes)
p=lambda i,k=39:-k*i or p([[y and(u>0<t)*2**(k%4+2)|y|u if k else y.bit_count()*5%14%9for y,t,u in zip(x,[0,*x],s)]for*x,s in zip(*i,[[0]*99,*zip(*i)])][::-1],k-1)

### xsot (315 bytes)
def p(m):
 M,N,*v=len(m),len(m[0])
 for i in range(M*N):
  z,*s=0,;q=(m[r:=i//N][c:=i%N]>2)*[(r,c)]
  while q:(y,x),*q=q;s+=(y,x),;b=0;[(b:=b*2|(M>i>-1<j<N!=3==m[i][j]!=((i,j)in v or(q:=q+[(i,j)]))))for i,j in[(y,x+1),(y+1,x),(y,x-1),(y-1,x)]];v+=(y,x),;z+=696553536>>b*2&3
  for r,c in s:m[r][c]=46%(8+z)
 return m

###########
def p(m):
    rows, cols = len(m), len(m[0])
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == 3:
                shape_cells = []
                signature = 0
                q = [(r, c)]
                visited.add((r, c))
                while q:
                    curr_r, curr_c = q.pop(0)
                    shape_cells.append((curr_r, curr_c))
                    b = 0
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        b *= 2
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and m[nr][nc] == 3:
                            b |= 1
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
                    if b in [0b0111, 0b1110, 0b1011, 0b1101]:
                        signature += 2
                    if b in [0b0011, 0b0110, 0b1100, 0b1001]:
                        signature += 1

                shape_type = [0,1,6,2][signature]

                for cell_r, cell_c in shape_cells:
                    m[cell_r][cell_c] = shape_type
    return m
