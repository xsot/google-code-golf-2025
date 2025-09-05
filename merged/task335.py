# combined (133 vs 2500 bytes for gold)
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k*6+2in x)*4for b,y in enumerate(x)]for x in zip(*i)],k-1)

### xsot (199 bytes)
def p(m):
 I=sum(m,[]).index;N=len(m[0])
 for c in range(min(x:=I(2)%N,X:=I(8)%N),max(x,X)+1):m[y:=I(2)//N][c]=4
 for r in range(min(y,Y:=I(8)//N),max(y,Y)+1):m[r][X]=4
 m[y][x]=2;m[Y][X]=8
 return m

##
def p(m):
 I=sum(m,[]).index;N=len(m[0]);i=I(2);j=I(8);y=i//N;x=i%N;Y=j//N;X=j%N
 for c in range(min(x,X),max(x,X)+1):m[y][c]=4
 for r in range(min(y,Y),max(y,Y)+1):m[r][X]=4
 m[y][x]=2;m[Y][X]=8
 return m

def p(matrix: list[list[int]]):
    """
    Draws an L-shaped line of 4s from a 2 to an 8 in a 2D matrix.

    The function finds the unique 2 and 8, then draws a line by first moving
    horizontally from the 2's row to the 8's column, and then vertically to
    the 8's row. The line is made of 4s and does not overwrite the 2 and 8.

    Args:
        matrix: A list of lists of integers (0, 2, 8). It is modified in-place.
    """
    # 1. Find the coordinates of 2 and 8
    r2, c2 = next((r, c) for r, row in enumerate(matrix) for c, val in enumerate(row) if val == 2)
    r8, c8 = next((r, c) for r, row in enumerate(matrix) for c, val in enumerate(row) if val == 8)

    # 2. Draw the horizontal and vertical lines with 4s
    # This will overwrite the 2 and 8, which we'll fix in the next step.
    for c in range(min(c2, c8), max(c2, c8) + 1):
        matrix[r2][c] = 4  # Horizontal line on the starting row
    for r in range(min(r2, r8), max(r2, r8) + 1):
        matrix[r][c8] = 4  # Vertical line on the ending column

    # 3. Restore the 2 and 8 so they are not overlapped by the line
    matrix[r2][c2] = 2
    matrix[r8][c8] = 8

    return matrix
