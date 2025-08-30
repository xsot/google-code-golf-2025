# xsot (136 vs 69 bytes for gold)
p=lambda m,R=range(10):[[(d:=min(set(a:=sum(m,[]))-{0,5}))*(r==a[::10].index(d)+(s:=a.count(5))or c==a.index(d)-s)for c in R]for r in R]

####
def p(matrix: list[list[int]]) -> list[list[int]]:
    """
    Transforms a matrix by shifting a 'cross' diagonally to the bottom-left.

    The function identifies a cross (a row and column filled with a single
    digit), counts the number of '5's in the rightmost column to determine
    the shift amount, and returns a new matrix with the cross moved.

    Args:
        matrix: A list of lists of integers representing the input matrix.

    Returns:
        A new list of lists of integers with the shifted cross. Non-cross
        elements in the new matrix are 0.
    """
    rows, cols = len(matrix), len(matrix[0])

    # 1. Find the shift amount by counting 5s in the last column
    shift = sum(1 for r in range(rows) if matrix[r][cols - 1] == 5)

    # 2. Find the original cross's digit and position
    cross_digit, cross_row, cross_col = None, None, None

    # Find the cross row and the digit it's made of
    for r, row_data in enumerate(matrix):
        # A set is a simple way to check if all elements in a list are the same
        if len(set(row_data)) == 1 and row_data[0] not in [0, 5]:
            cross_digit = row_data[0]
            cross_row = r
            break

    # Find the cross column using the digit we just found
    for c in range(cols):
        if all(matrix[r][c] == cross_digit for r in range(rows)):
            cross_col = c
            break

    # 3. Calculate the new position for the cross
    new_row = cross_row + shift
    new_col = cross_col - shift

    # 4. Create a new matrix filled with zeros
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # 5. Draw the new cross onto the new matrix
    # Fill the new row
    for c in range(cols):
        new_matrix[new_row][c] = cross_digit
    # Fill the new column
    for r in range(rows):
        new_matrix[r][new_col] = cross_digit

    return new_matrix
