# combined (134 vs 112 bytes for gold)
p=lambda i:max([[x[a%9:][:9-a//9%9]for x in i[a//81%9:][:9-a//729]]for a in range(9**4)],key=lambda p:"0"in(r:=str(p))or r.count("2"))

### xsot (181 bytes)
def p(m,b=[0]*3):
 for k in range(99):
  R=r=k//10
  while R<10>0<m[R][c:=k%10]:R+=1
  b=max(b,[sum(a:=[l[c:[*m[r],0].index(0,c)]for l in m[r:R]],[]).count(2),-r,-c,a])
 return b[3]

#######
def p(matrix):
    """
    Finds the filled rectangle with the most 2s in a matrix.

    The matrix is assumed to contain disjoint, filled rectangles of non-zero digits,
    separated by zeros.

    Args:
        matrix: A list of lists of integers representing the matrix.

    Returns:
        A list of lists representing the rectangle with the highest count of 2s.
        Returns None if the matrix is empty or contains no non-zero rectangles.
    """
    rows, cols = len(matrix), len(matrix[0])

    best_rectangle = None
    max_twos_count = -1

    for r in range(rows):
        for c in range(cols):
            # 1. Find the rectangle's dimensions (width and height)
            # Scan right to find width
            width = 0
            while c + width < cols and matrix[r][c + width] != 0:
                width += 1

            # Scan down to find height
            height = 0
            while r + height < rows and matrix[r + height][c] != 0:
                height += 1

            # 2. Extract the rectangle and count its 2s
            current_rectangle = [row[c : c + width] for row in matrix[r : r + height]]
            current_twos = sum(row.count(2) for row in current_rectangle)

            # 3. Check if this is the best rectangle so far
            #    In case of a tie, prefer the earlier one
            if current_twos > max_twos_count:
                max_twos_count = current_twos
                best_rectangle = current_rectangle

    return best_rectangle
