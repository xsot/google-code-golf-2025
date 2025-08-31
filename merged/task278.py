# combined (143 vs 118 bytes for gold)
p=lambda i,k=3,e=enumerate:-k*i or p([[y or("2, 2"in str([h[a:a+3]for h in i[b-(b>0):b+2]]))*3for b,y in e(x)]for a,x in e(zip(*i))][::-1],k-1)

### ovs (179 bytes)
def p(g):E=enumerate;L=abs;S={(i,j)for i,r in E(g)for j,v in E(r)if v};return[[v or 3*any(L(a-I)+L(A-J)==1==L(i-I)|L(j-J)for a,A in S for I,J in S)for j,v in E(r)]for i,r in E(g)]

### xsot (257 bytes)
def p(m):
 M,N=len(m),len(m[0])
 for i in range(N*M):
  for u,v,s in[(r:=i//N,(c:=i%N)+1,b'#Cc'),(r+1,c,b'\x80\x81\x82')]:
   for k in(M>u>-1<v<N>m[r][c]==m[u][v]==2)*(b' @`!a"Bb'+s):
    if M>(y:=r+k//32-2)>-1<(x:=c+k%8-1)<N!=m[y][x]!=2:m[y][x]=3
 return m

###
def p(m):
    M,N=len(m),len(m[0])
    for i in range(N*M):
        for nr, nc in[(r:=i//N,(c:=i%N)+1),(r+1,c)]:
            for cell_r, cell_c in [(r,c),(nr,nc)]*(M>nr>-1<nc<N>m[r][c]==m[nr][nc]==2):
                for i in b' @`!a"Bb':
                    i,j =cell_r+i//32-2, cell_c + i%8-1
                    if M>i>-1<j<N and m[i][j]!=2:
                        m[i][j] = 3
    return m

###
def p(matrix):
    """
    Finds horizontally/vertically connected pairs of 2s in a matrix and
    changes their neighbors (including diagonals) to 3s.

    Args:
        matrix: A list of lists of integers (0 or 2).

    Returns:
        A new matrix with the neighbors of 2-pairs changed to 3.
    """
    rows, cols = len(matrix), len(matrix[0])

    # Use a set to store neighbor coordinates, automatically handling duplicates.
    coords_to_change = set()

    # PASS 1: Find pairs and collect coordinates of their neighbors.
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 2:
                continue

            # To find each pair only once, check neighbors to the right and down.
            # This now EXCLUDES diagonal checks for forming a pair.
            # (0, 1) is right, (1, 0) is down.
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is in bounds and is also a '2'
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 2:
                    # Found a valid pair: (r, c) and (nr, nc).
                    # Now, find all 8 neighbors of BOTH cells in the pair.
                    for cell_r, cell_c in [(r, c), (nr, nc)]:
                        # Iterate through the 8 neighbors (including diagonals)
                        for r_offset in range(-1, 2):
                            for c_offset in range(-1, 2):
                                if r_offset == 0 and c_offset == 0:
                                    continue

                                neighbor_r, neighbor_c = cell_r + r_offset, cell_c + c_offset

                                # If the neighbor is within bounds, add it to the set.
                                if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols:
                                    coords_to_change.add((neighbor_r, neighbor_c))

    # PASS 2: Modify the new matrix based on the collected coordinates.
    for r, c in coords_to_change:
        # Only change cells that were not originally 2s.
        if matrix[r][c] != 2:
            matrix[r][c] = 3

    return matrix
