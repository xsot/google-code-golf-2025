# joking+mwi (152 vs 123 bytes for gold)
p=lambda i,k=19,t=0:-k*i or p([[0**k*sorted({*sum(i,[])}).index(y)*2%5or(y>0)*max(s,5+(t:=s and-~t),s:=y)for y in x]for x in zip(*i[::-1])if[s:=0]],k-1)

### xsot (279 bytes)
def p(m):
 a=[]
 for k in range(99):
  w=(r:=k//10,c:=k%10),
  if m[r][c]>4:
   for x,y in[(0,1),(1,0)]:
    j=r;i=c
    while-1<(j:=j+y)<10>(i:=i+x)>-1!=m[j][i]>4:w+=(j,i),;z=m[j][i]=0
   a+=[len(w),w],
 for _,e in sorted(a)[::-1]:
  for r,c in e:m[r][c]=4**z%7
  z+=1
 return m

###
def p(m):
    rows, cols = len(m), len(m[0])
    a = []
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == 5:
                w = []
                q = [(r, c)]
                while q:
                    (row,col),*q=q
                    w+=(row, col),
                    for dr, dc in [(0, 1),(1,0)]:
                        nr, nc = row + dr, col + dc
                        if rows>nr>-1<nc<cols!=m[nr][nc]>4:
                            m[nr][nc]=0
                            q+=(nr,nc),
                a+=[len(w),w],
    i=0
    for e in sorted(a)[::-1]:
     for r,c in e[1]:m[r][c]=[1,4,2][i]
     i+=1
    return m

####
def p(matrix):
    """
    Finds three non-overlapping rectangles of 5s in a matrix, ranks them
    by size (area), and replaces the 5s with their rank (1, 2, or 3).

    Args:
        matrix (list[list[int]]): A 2D list of 5s and 0s.

    Returns:
        list[list[int]]: The matrix with 5s replaced by their rank.
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    rectangles = []

    # 1. Find all three rectangles using a search algorithm
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 5 and (r, c) not in visited:
                # Start of a new rectangle, find all its cells
                current_coords = []
                queue = [(r, c)]
                visited.add((r, c))

                while queue:
                    row, col = queue.pop(0)
                    current_coords.append((row, col))

                    # Check neighbors (up, down, left, right)
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and \
                           matrix[nr][nc] == 5 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

                # Store the rectangle's size and coordinates
                rectangles.append({'size': len(current_coords), 'coords': current_coords})

    # 2. Sort the found rectangles by size in descending order
    rectangles.sort(key=lambda r: r['size'], reverse=True)

    # 3. Replace the 5s in the matrix with their rank
    for rank, rect_info in enumerate(rectangles):
        for r_coord, c_coord in rect_info['coords']:
            matrix[r_coord][c_coord] = [1,4,2][rank]

    return matrix
