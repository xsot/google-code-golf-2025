# xsot (92 vs 73 bytes for gold)
def p(M,m=[[0]*6]*6):
 for i in[0,1,2]*9:m[i][:3]=M[i];*m,=map(list,zip(*m[::-1]))
 return m

##
def rotate_matrix_counter_clockwise(matrix):
    """
    Rotates a square matrix 90 degrees counter-clockwise.

    Args:
        matrix (list of lists): The N x N matrix to rotate.

    Returns:
        list of lists: The new, rotated N x N matrix.
    """
    n = len(matrix)
    # Create a new blank matrix of the same size
    rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # The transformation for a counter-clockwise rotation is:
    # The element at [row][col] moves to [n - 1 - col][row]
    for r in range(n):
        for c in range(n):
            rotated_matrix[n - 1 - c][r] = matrix[r][c]

    return rotated_matrix

def p(matrix_3x3):
    """
    Creates a 6x6 matrix from a 3x3 matrix by placing the original
    matrix in the top-left and its clockwise rotations in the other quadrants.

    This is solved by starting with a blank 6x6 matrix, placing the 3x3
    matrix in the top-left, and then repeatedly rotating the entire 6x6
    matrix counter-clockwise and re-placing the original 3x3 matrix.

    Args:
        matrix_3x3 (list of lists): The 3x3 matrix of digits.

    Returns:
        list of lists: The resulting 6x6 matrix.
    """
    # 1. Start with a blank 6x6 matrix (filled with 0s).
    matrix_6x6 = [[0 for _ in range(6)] for _ in range(6)]

    # 2. Place the original 3x3 matrix in the top-left corner.
    for r in range(3):
        for c in range(3):
            matrix_6x6[r][c] = matrix_3x3[r][c]

    # 3. Rotate the 6x6 matrix counter-clockwise and repeat the placement 3 times.
    for _ in range(3):
        # a. Rotate the entire 6x6 matrix counter-clockwise.
        matrix_6x6 = rotate_matrix_counter_clockwise(matrix_6x6)

        # b. Place the original 3x3 matrix in the top-left corner again.
        # This overwrites the values that were just rotated into that corner.
        for r in range(3):
            for c in range(3):
                matrix_6x6[r][c] = matrix_3x3[r][c]

    return matrix_6x6


###


p=lambda m,R=range(6):[[sum(m,[])[[(r%3*3+c%3),(6-c%3*3+r%3),(c%3*3+2-r%3),(6-r%3*3+2-c%3)][r//3*2+c//3]]for c in R]for r in R]

###
def p(m):
    def get_value(r, c):
        source_r, source_c = [(r%3,c%3),(2-c%3,r%3),(c%3,2-r%3),(2-r%3,2-c%3)][r//3*2+c//3]
        return m[source_r][source_c]
    return [[get_value(r, c) for c in range(6)] for r in range(6)]

###
def p(matrix):
    """
    Builds a 6x6 matrix by mapping each cell to a value in the original 3x3
    matrix using a concise coordinate transformation lookup.
    """
    N = len(matrix)

    # A map of quadrant coordinates to functions that perform the inverse rotation.
    # Each lambda takes local coordinates (r, c) and returns source coordinates.
    transforms = {
        # Quadrant (row, col) : lambda local_r, local_c: (source_r, source_c)
        (0, 0): lambda r, c: (r, c),                      # Top-Left (no rotation)
        (0, 1): lambda r, c: (N - 1 - c, r),             # Top-Right (inverse of 90°)
        (1, 0): lambda r, c: (c, N - 1 - r),             # Bottom-Left (inverse of 270°)
        (1, 1): lambda r, c: (N - 1 - r, N - 1 - c),     # Bottom-Right (inverse of 180°)
    }

    def get_value(r, c):
        """Calculates the source value for a target cell (r, c) in the 6x6 grid."""
        quadrant = (r // N, c // N)
        local_coords = (r % N, c % N)
        source_r, source_c = transforms[quadrant](*local_coords)
        return matrix[source_r][source_c]

    # Build the 6x6 matrix using a nested list comprehension
    return [[get_value(r, c) for c in range(2 * N)] for r in range(2 * N)]
