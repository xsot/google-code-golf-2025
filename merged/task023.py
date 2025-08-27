def p(g,*S):
 w=len(g[0])
 for c in-6&len(S)+4,5:
  for I in S:g[I//w][I%w]=c
  try:f=sum(g,[])*2;i=f.index(5);[{5}-{c}=={f[I]for I in s}!=g==p(g,i,*s)>1for s in[[w+i,1+i,w-~i],[i+1,i+2],[i+w,i+w*2]]]
  except:return g

### xsot (578 bytes)
def p(m):
 N,M=len(m),len(m[0])
 def f():
  a=sum(m,[])
  if 5 not in a:return 1
  i=a.index(5);r=i//M;c=i%M
  if r + 1 < N and c + 1 < M and m[r+1][c]==m[r][c+1]==m[r+1][c+1]==5:
   m[r][c] = m[r+1][c] = m[r][c+1] = m[r+1][c+1] = 8
   if f():return 1
   m[r][c] = m[r+1][c] = m[r][c+1] = m[r+1][c+1] = 5
  if c + 2 < M and m[r][c+1]==m[r][c+2]==5:
   m[r][c:c+3]=2,2,2
   if f():return 1
   m[r][c:c+3]=5,5,5
  if r + 2 < N and m[r+1][c]==m[r+2][c]==5:
   m[r][c] = m[r+1][c] = m[r+2][c] = 2
   if f():return 1
   m[r][c] = m[r+1][c] = m[r+2][c] = 5
  return 0
 if f():return m

###

import copy

def p(matrix):
    rows, cols = len(matrix), len(matrix[0])
    solution = copy.deepcopy(matrix)

    def find_first_uncovered():
        """Finds the row and column of the first '5'."""
        for r in range(rows):
            for c in range(cols):
                if solution[r][c] == 5:
                    return r, c
        return None, None # No 5s left, puzzle is solved

    def backtrack():
        r, c = find_first_uncovered()

        # Base Case: If no 5s are found, we have a complete solution.
        if r is None:
            return True

        # --- CHOICE 1: Try to place a 2x2 square of 8s ---
        if r + 1 < rows and c + 1 < cols and \
           solution[r+1][c] == 5 and solution[r][c+1] == 5 and solution[r+1][c+1] == 5:

            # Place the square
            solution[r][c] = solution[r+1][c] = solution[r][c+1] = solution[r+1][c+1] = 8
            if backtrack():
                return True
            # Backtrack
            solution[r][c] = solution[r+1][c] = solution[r][c+1] = solution[r+1][c+1] = 5

        # --- CHOICE 2: Try to place a 1x3 horizontal rectangle of 2s ---
        if c + 2 < cols and solution[r][c+1] == 5 and solution[r][c+2] == 5:

            # Place the rectangle
            solution[r][c] = solution[r][c+1] = solution[r][c+2] = 2
            if backtrack():
                return True
            # Backtrack
            solution[r][c] = solution[r][c+1] = solution[r][c+2] = 5

        # --- CHOICE 3: Try to place a 3x1 vertical rectangle of 2s ---
        if r + 2 < rows and solution[r+1][c] == 5 and solution[r+2][c] == 5:

            # Place the rectangle
            solution[r][c] = solution[r+1][c] = solution[r+2][c] = 2
            if backtrack():
                return True
            # Backtrack
            solution[r][c] = solution[r+1][c] = solution[r+2][c] = 5

        # If no placement at (r, c) leads to a solution, this path fails.
        return False

    if backtrack():
        return solution
