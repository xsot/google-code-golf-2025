# mwi (101 vs 96 bytes for gold)
import re;p=lambda i:[i:=eval(re.sub("0, 0, 0(.{55})?"*3,"1,1,1\%d "*3%(1,2,3),str(i)))for _ in i][2]

### ovs (102 bytes)
import re;p=lambda i,k=2:-k*i or p(eval(re.sub("0, 0, 0(.{55})?"*3,"1,1,1\%d "*3%(1,2,3),str(i))),k-1)

### combined (107 bytes)
import re;p=lambda i,k=2:-k*i or p(eval(re.sub("0, 0, 0(.{55})?"*3,r"1,1,1\1 1,1,1\2 1,1,1\3",str(i))),k-1)

### att (132 bytes)
r=range(324)
def p(a):
	for i in r:
		b=a[i%18:][:3];i//=18;z=any(max([*zip(*b)][i:i+3]))
		for k in r:b[k%5%3][i+k%3]**=z
	return a

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
