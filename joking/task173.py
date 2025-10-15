p=lambda n:[1for l,s in enumerate(n)for d,s in enumerate(s)for y,s in enumerate(n)for t,s in enumerate(s)if((r:=[n[y-f//3][t-f%3]for f,s in enumerate(n[:9])])==r[::-1])*sum(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(s==n[l-f//3][d-f%3]for f,s in enumerate(r))>7)for f,n[l-f//3][d-f%3]in enumerate(r)]and n

##
p=lambda n:[#[*range(10)]##for l,s in enumerate(n)for d,s in enumerate(s)for y,s in enumerate(n)for t,s in enumerate(s)if((r:=[n[y-f//3][t-f%3]for f,s in enumerate(n[:9])])==r[::-1])*sum(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(s==n[l-f//3][d-f%3]for f,s in enumerate(r))>7)for f,n[l-f//3][d-f%3]in enumerate(r)]#['and ','*0+']##n
p=lambda n:[n for l,s in enumerate(n)for d,s in enumerate(s)for y,s in enumerate(n)for t,s in enumerate(s)if((r:=[n[y-f//3][t-f%3]for f,s in enumerate(n[:9])])==r[::-1])*sum(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(s==n[l-f//3][d-f%3]for f,s in enumerate(r))>7)for f,n[l-f//3][d-f%3]in enumerate(r)][#[*range(10)]##]

## range versions
p=lambda n:[exec(((r:=[n[y-f//3][t-f%3]for f in range(9)])==r[::-1])*any(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(n[l-f//3][d-f%3]==r[f]for f in range(9))>7)*'for f in range(9):n[l-f//3][d-f%3]=r[f]')for l in range(len(n))for y in range(len(n))for d in range(len(n[0]))for t in range(len(n[0]))]*0+n
p=lambda n:[exec('for f in range(9):n[l-f//3][d-f%3]=r[f]')for l in range(len(n))for y in range(len(n))for d in range(len(n[0]))for t in range(len(n[0]))if((r:=[n[y-f//3][t-f%3]for f in range(9)])==r[::-1])*any(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(n[l-f//3][d-f%3]==r[f]for f in range(9))>7)]*0+n