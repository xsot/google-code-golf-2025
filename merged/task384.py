# att (65 vs 64 bytes for gold)
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))for _ in'  'if 4in b]

### combined (tied, 65 bytes)
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))for _ in'  'if 4in b]

### xsot (160 bytes)
def p(m,R=range):r,c=zip(*[(r,c)for i in R(81)if m[r:=i//9][c:=i%9]]);return sum([[sum([[v,v]for v in l[min(c):max(c)+1]],[])]*2for l in m[min(r):max(r)+1]],[])

###
def p(m,R=range):r,c=zip(*[(r,c)for i in R(81)if m[r:=i//9][c:=i%9]]);return sum([[sum([[v,v]for v in l[min(c):max(c)+1]],[])]*2for l in m[min(r):max(r)+1]],[])
def p(m,R=range):r,c=zip(*[(r,c)for i in R(81)if m[r:=i//9][c:=i%9]]);return sum([[sum([[v,v]for v in m[r][min(c):max(c)+1]],[])]*2for r in R(min(r),max(r)+1)],[])
def p(m,R=range):r,c=zip(*[(r,c)for r in R(9)for c in R(9)if m[r][c]]);return sum([[sum([[v,v]for v in m[r][min(c):max(c)+1]],[])]*2for r in R(min(r),max(r)+1)],[])

def p(matrix):
    # 1. Find the coordinates of all non-zero values in the matrix.
    one_coords = [
        (r, c) for r, row in enumerate(matrix) for c, val in enumerate(row) if val
    ]

    # 2. Determine the bounding box of the submatrix.
    rows, cols = zip(*one_coords)
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)

    # 3. Extract the submatrix and scale it up by 2x in one go.
    #    For each row in the submatrix, we create a new row where each element is
    #    duplicated. Then, we duplicate that newly created row.
    scaled_result = [
        [val for val in matrix[r][min_c : max_c + 1] for _ in range(2)]
        for r in range(min_r, max_r + 1)
        for _ in range(2)
    ]

    return scaled_result
