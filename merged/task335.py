# joking (110 bytes, gold)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|(n%6*2in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-3)


## almost identical to 246
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k*6+2in x)*4for y in x],*i)],k-1)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|(n%6*2in b)*(d:=~9%~sum(c)+d&4)for c in a[::-1]]for*b,in zip(*a)],n-3)
p=lambda a,n=15,d=0:-n*a or p([[b.pop()|(n*7&26in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-2)
p=lambda a,n=23,d=0:-n*a or p([[b.pop()|(-~n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)
p=lambda a,n=24,d=0:n and p([[b.pop()|(n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)or a
p=lambda a,n=25,d=0:1//n*a or p([[b.pop()|(n&10in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-6)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|4*(n%6*2in(d:=d^-5%~sum(c)%3)*b)for c in a[::-1]]for*b,in zip(*a)],n-3)

## alt 110
p=lambda a,d=0:[a:=[[b.pop()|(n in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)]for n in[8,2]*2][3]

### att (113 bytes)
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|4*(n%6*2in b)*(d:=d^any({*c}-{4}))for c in a[::-1]]for*b,in zip(*a)],n-3)

### combined (133 bytes)
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
