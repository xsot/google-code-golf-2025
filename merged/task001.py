# att (61 bytes, gold)
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]

### ovs (tied, 61 bytes)
p=lambda g:[[v&V for v in l for V in L]for l in g for L in g]

### xsot (71 bytes)
p=lambda m,R=range(9):[[m[r//3][c//3]&m[r%3][c%3]for c in R]for r in R]

##
p=lambda m,R=range(9):[[m[r//3][c//3]and m[r%3][c%3]for c in R]for r in R]
p=lambda m,R=range(9):[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in R]for r in R]
p=lambda m,R=range(9):[sum([m[r//3]*(m[r%3][c%3]>0)for c in R],[])for r in R]
p=lambda m:[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in range(9)]for r in range(9)]
