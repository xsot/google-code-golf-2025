# att (114 vs 113 bytes for gold)
p=lambda m,i=95:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("2320,,,,    133"[i%5::4],"1213,,,,121"[i%5::4])))]

### combined (tied, 114 bytes)
p=lambda m,i=95:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("2320,,,,    133"[i%5::4],"1213,,,,121"[i%5::4])))]

### xsot (118 bytes)
p=lambda m,i=91:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("3220,,,,    331"[i%7%4::4],"2113,,,,211"[i%7%4::4])))]

##
p=lambda m,i=91:-i*m or p([*zip(*eval(str(m).replace("3220,,,,    331"[i%7%4::4],"2113,,,,211"[i%7%4::4])))][::-1],i-1)
p=lambda m,i=91:-i*m or p([*zip(*eval(str(m).replace(["3, 3","2, 3","2, 1","0, "][i%7%4],["2,2","1,1","1,1","3, "][i%7%4])))][::-1],i-1)
p=lambda m,i=91:-i*m or p([*zip(*eval(str(m).replace(["0","3, 3","2, 3","2, 1"][i%7%4],["3","2,2","1,1","1,1"][i%7%4])))][::-1],i-1)
p=lambda m,i=7:-i*m or p([*zip(*eval(str(m).replace("0","3").replace("3, 3","2,2").replace("2, 3","1,1").replace("2, 1","1,1")))][::-1],i-1)

##
def p(m):
 M,N=len(m),len(m[0])
 for i in range(M*N):
  z,*s=0,;q=(m[r:=i//N][c:=i%N]<1)*[(r,c)]
  while q:
   m[r][c]=9;(y,x),*q=q;z+=1;s+=(y,x),
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
    if M>i>-1<j<N>1>m[i][j]:m[i][j]=9;q+=(i,j),
  for r,c in s:m[r][c]=4-z
 return m

####
# TODO: how to avoid doing m[r][c]=9 twice?

def p(matrix):
    """
    Finds regions of 0s in a matrix and fills each region with its size.

    The algorithm iterates through each cell of the matrix. If a cell contains a 0,
    it means we've found a new, uncounted region. A Breadth-First Search (BFS)
    is then started from that cell to find all connected 0s. The coordinates of
    these 0s are stored. Once the entire region is found, we calculate its size
    and fill all the stored coordinates in the matrix with that size.

    Args:
        matrix (list[list[int]]): A 2D list of 5s and 0s.

    Returns:
        list[list[int]]: The modified matrix with 0-regions filled by their size.
    """
    rows, cols = len(matrix), len(matrix[0])

    # Iterate through each cell in the matrix
    for r in range(rows):
        for c in range(cols):
            # If we find a 0, it's the start of a region we haven't processed yet
            if matrix[r][c] == 0:
                # Start a search to find all connected 0s
                size = 0
                q = [(r, c)]  # A queue for our BFS, starting with the current cell
                region_coords = [] # To store coordinates of the 0s in this region

                # Mark the starting cell as visited by changing it to a temporary value.
                # This prevents it from being added to the queue again.
                matrix[r][c] = -1

                while q:
                    curr_r, curr_c = q.pop(0)
                    size += 1
                    region_coords.append((curr_r, curr_c))

                    # Check all 4 neighbors (up, down, left, right)
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc

                        # Check if the neighbor is within bounds and is an unvisited 0
                        if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 0:
                            matrix[nr][nc] = -1  # Mark as visited
                            q.append((nr, nc))

                # After finding all cells in the region, fill them with the calculated size
                for fr, fc in region_coords:
                    matrix[fr][fc] = 4-size

    return matrix
