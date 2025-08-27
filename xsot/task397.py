# uses exec scoping bug to avoid copying r
p=lambda m,k=0:exec('r=k//9;c=k%9;exec("m[r+2][c:c+2]=3,3;r+=1;"*len(a:={*m[r][c:c+2]+m[r+1][c:c+2]})*(not{0,3}&a));k+=1;'*81)or m

##
def p(m):k=0;exec('r=k//9;c=k%9;i=r+2;exec("m[i][c:c+2]=3,3;i+=1;"*len(a:={*m[r][c:c+2]+m[r+1][c:c+2]})*(not{0,3}&a));k+=1;'*81);return m

def p(m):
    """
    Finds 2x2 non-zero, non-overlapping submatrices in a 10x10 matrix and
    fills a rectangle below each with the number 3.

    For each submatrix, N is the number of distinct digits in it. The rectangle
    to be filled is 2 columns wide by N rows high.

    Args:
        matrix: A 10x10 list of lists of digits.

    Returns:
        The transformed 10x10 matrix.
    """
    for r in range(9):
        c = 0
        while c < 9:
            a = {*m[r][c:c+2],*m[r+1][c:c+2]}
            if not {0,3} & a:
                N = len(a)
                for i in range(N):
                    m[r+2+i][c:c+2] = 3,3
            c += 1
    return m