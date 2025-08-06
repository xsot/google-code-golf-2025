p=lambda m,R=range(6):[[max(3>r-k>-1<c-k<3and m[r-k][c-k]for k in R)for c in R]for r in R]

###
def expand_diagonals(matrix_3x3: list[list[int]]) -> list[list[int]]:
    """
    Expands a 3x3 matrix to a 6x6 matrix by repeating its non-zero
    digits diagonally towards the bottom-right.

    Args:
        matrix_3x3: A list of lists of digits representing a 3x3 matrix.
                    The diagonals are guaranteed to have at most one
                    non-zero digit.

    Returns:
        A new 6x6 matrix with the described diagonal expansion.
    """
    return [
        [
            # For each cell (r, c), find its source value by looking
            # diagonally up and to the left into the 3x3 matrix.
            next(
                (
                    matrix_3x3[r - k][c - k]
                    # Iterate k to check cells (r-k, c-k) as potential sources.
                    for k in range(min(r, c) + 1)
                    # The source must be within the 3x3 grid and be non-zero.
                    if r - k < 3 and c - k < 3 and matrix_3x3[r - k][c - k]
                ),
                0,  # If no non-zero source is found, the value is 0.
            )
            for c in range(6)
        ]
        for r in range(6)
    ]