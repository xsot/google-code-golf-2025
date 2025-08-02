def p(m,R=range):
 d,b,_=sorted(set(a:=sum(m,[])),key=a.count);r,c=len(m),len(m[0]);z=0,
 for i in R(r*c):
  Y=y=i%r;X=x=i//r
  while-~Y<r!=m[Y+1][x]==b:Y+=1
  while-~X<c!=m[y][X+1]==b:X+=1;z=max(z,(sum(sum(a:=[[d*(e>0)for e in m[i][x:X+1]]for i in R(y,Y+1)],[]))//d,a))
 return z[1]

########
def p(m):
    """
    Finds the hollow rectangular box of 2s that contains the most 1s.

    The function iterates through a matrix to identify non-overlapping boxes
    formed by the digit b. For each box, it counts the number of 1s inside
    it and returns the box (as a new matrix) that has the highest count.

    Args:
        matrix: A list of lists of integers (0, 1, or b) representing the matrix.

    Returns:
        A new list of lists representing the box with the most 1s.
        If no boxes are found, or in case of a tie, it returns the first
        box found with the maximum count. Returns an empty list if the
        input matrix is empty or no boxes are present.
    """
    a = sum(m,[])
    d,b,_ = sorted(set(a), key=a.count)

    rows, cols = len(m), len(m[0])
    max_dots = -1

    for r1 in range(rows):
        for c1 in range(cols):
            # Assume this is the top left corner
            # Move along the top and left edges until we reach the bottom right corner
            r2, c2 = r1, c1
            while c2 + 1 < cols and m[r1][c2 + 1] == b:
                c2 += 1
            while r2 + 1 < rows and m[r2 + 1][c1] == b:
                r2 += 1

            # potential answer
            a = [[d*(e>0)for e in m[i][c1:c2+1]]for i in range(r1, r2+1)]

            dots = sum(sum(a,[]))//d

            if dots > max_dots:
                max_dots = dots
                result_box = a

    return result_box