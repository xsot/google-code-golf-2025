# joking (97 bytes, gold)
import re;p=lambda i,*I:eval(re.sub("0, 0, 0(.{55})?"*3," 1,1,1\%d"*3%(1,2,3),str(I or p(i,*i))))

## alts
import re;p=lambda i,*I,r=[1]*3:eval(re.sub("0, 0, 0(.{55})??"*3,r"*r\1*r\2*r",str(I or p(i,*i))))

### ovs (tied, 97 bytes)
import re;p=lambda i,*I:eval(re.sub("0, 0, 0(.{55})?"*3,"*[1]*3\%d"*3%(1,2,3),str(I or p(i,*i))))

### att (98 bytes)
import re
p=lambda i:eval(eval('re.sub("0, 0, 0(.{55})?"*3,"*(1,)*3\%d"*3%(1,2,3),'*2+f'"{i}"))'))

### mwi (101 bytes)
import re;p=lambda i:[i:=eval(re.sub("0, 0, 0(.{55})?"*3,"1,1,1\%d "*3%(1,2,3),str(i)))for _ in i][2]

### combined (107 bytes)
import re;p=lambda i,k=2:-k*i or p(eval(re.sub("0, 0, 0(.{55})?"*3,r"1,1,1\1 1,1,1\2 1,1,1\3",str(i))),k-1)

### xsot (161 bytes)
def p(m,R=range):
 for r in R(len(m)-2):
  for c in R(len(m[0])-2):
   if sum(sum(m[r+i][c:c+3])for i in R(3))<1:
    for i in R(3):m[r+i][c:c+3]=[1]*3
 return m

##
def fill_zero_region(matrix: list[list[int]]) -> list[list[int]]:
    """
    Finds a 3x3 region of zeroes in a 2D matrix and fills it with ones.

    Args:
        matrix: A list of lists of digits representing the 2D matrix.

    Returns:
        The modified matrix.
    """
    # Iterate through each possible top-left corner (r, c) of a 3x3 region
    for r in range(len(matrix) - 2):
        for c in range(len(matrix[0]) - 2):
            # Check if the 3x3 region is all zeroes by summing its elements.
            # If the sum is 0, all 9 elements must be 0.
            if sum(matrix[r+i][c+j] for i in range(3) for j in range(3)) == 0:
                # Fill the identified 3x3 region with ones
                for i in range(3):
                    for j in range(3):
                        matrix[r+i][c+j] = 1
    return matrix
