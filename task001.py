p=lambda m,R=range(9):[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in R]for r in R]
# p=lambda m:[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in range(9)]for r in range(9)]