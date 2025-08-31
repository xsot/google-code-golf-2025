# joking+mwi (138 bytes, gold)
import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m,q=[re.findall("([^50](, [1-9])+)",str(i)*9)for _ in i]:q[m.end()%8].pop(0)[0],str(i)))

### xsot (197 bytes)
def p(m):s=sum(m,[]);a=[x%5>0for x in s];x=a.index(1);w=a[x:].index(i:=0);exec("for j in range((a[x:][::10]+a).index(0)*(m[r:=i//10][c:=i%10]==5)):m[r+j][c:c+w]=s[x+10*j:][:w]\ni+=1\n"*99);return m

##
def p(m):s=sum(m,[]);a=[x%5>0for x in s];x=a.index(1);w=a[x:].index(i:=0);exec("for j in range((a[x:][::10]+a).index(0)*(m[r:=i//10][c:=i%10]==5)):m[r+j][c:c+w]=s[x+10*j:][:w]\ni+=1\n"*99);return m
def p(m):a=[x%5>0for x in sum(m,[])];x=a.index(1);w=a[x:].index(i:=0);exec("for j in range((a[x:][::10]+a).index(0)*(m[r:=i//10][c:=i%10]==5)):m[r+j][c:c+w]=m[x//10+j][x%10:x%10+w]\ni+=1\n"*99);return m

def p(m):
    a=[x%5>0for x in sum(m,[])]
    x=a.index(1)
    h=(a[x:][::10]+[0]).index(0)
    w=(a[x:]+[0]).index(0)
    for i in range(100):
        for j in range(h*(m[r:=i//10][c:=i%10]==5)):m[r+j][c:c+w]=m[x//10+j][x%10:x%10+w]
    return m

def p(matrix: list[list[int]]) -> list[list[int]]:
    """
    Colors rectangles made of 5s with the pattern of a non-5 rectangle.

    Args:
        matrix: A 10x10 list of lists containing 0s (background), one
                rectangle of various digits, and other rectangles of 5s.
                All rectangles have the same area.

    Returns:
        A new 10x10 matrix with the 5-rectangles colored in.
    """
    # 1. Find the target pattern and its dimensions.
    try:
        # Find the top-left corner of the non-5/non-0 rectangle concisely.
        start_r, start_c = next(
            (r, c) for r, row in enumerate(matrix)
            for c, val in enumerate(row) if val not in [0, 5]
        )
    except StopIteration:
        # If no target rectangle exists, return a copy of the original.
        return [row[:] for row in matrix]

    # Determine the height and width from the starting corner.
    h = 0
    while start_r + h < 10 and matrix[start_r + h][start_c] != 0:
        h += 1
    w = 0
    while start_c + w < 10 and matrix[start_r][start_c + w] != 0:
        w += 1

    # Extract the pattern using list slicing.
    pattern = [row[start_c : start_c + w] for row in matrix[start_r : start_r + h]]

    # 2. Create a new matrix to modify.
    new_matrix = [row[:] for row in matrix]

    # 3. Find every 5-rectangle and apply the pattern.
    for r in range(10 - h + 1):
        for c in range(10 - w + 1):
            # A top-left corner of a 5-rectangle is a 5 preceded by 0s (or at an edge).
            is_top_left_of_5_rect = (
                new_matrix[r][c] == 5 and
                (r == 0 or new_matrix[r - 1][c] == 0) and
                (c == 0 or new_matrix[r][c - 1] == 0)
            )
            if is_top_left_of_5_rect:
                # "Color" the area by replacing 5s with the pattern.
                for i in range(h):
                    for j in range(w):
                        new_matrix[r + i][c + j] = pattern[i][j]

    return new_matrix
