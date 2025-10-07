# att (61 vs 58 bytes for gold)
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]

### mwi (tied, 61 bytes)
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]

### ovs (tied, 61 bytes)
p=lambda g:[[v&V for v in l for V in L]for l in g for L in g]

### combined (tied, 61 bytes)
p=lambda i:[[y&t for y in x for t in s]for x in i for s in i]

### joking (63 bytes)
exec("p=lambda a:[[d&e "+"for %s in %s%s"*4%(*'db ec]ba ca]',))

## recursive
p=lambda a,c=0:a*0!=0and[p(s,t)for s in a for t in c or a]or a&c
p=lambda a,*c:[s&t if c else p(s,*t)for s in a for t in c or a]
p=lambda*a:[s*0!=0and p(s,t)or s&t for s in a[0]for t in a[-1]]
p=lambda*a:[s&t if a[1:]else p(s,t)for s in a[0]for t in a[-1]]

## doesn't work, splits up each list
p=lambda a,s=[]:s*0!=0and[*map(p,s or a,[a]*9)]or a&s

### xsot (71 bytes)
p=lambda m,R=range(9):[[m[r//3][c//3]&m[r%3][c%3]for c in R]for r in R]

##
p=lambda m,R=range(9):[[m[r//3][c//3]and m[r%3][c%3]for c in R]for r in R]
p=lambda m,R=range(9):[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in R]for r in R]
p=lambda m,R=range(9):[sum([m[r//3]*(m[r%3][c%3]>0)for c in R],[])for r in R]
p=lambda m:[[m[r//3][c//3]*(m[r%3][c%3]>0)for c in range(9)]for r in range(9)]
