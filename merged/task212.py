# att (93 bytes, gold)
p=lambda i,k=18:~k*i or[[x.pop()or[0,*x][k%-2]%5&6-(5in x)for _ in i]for*x,in zip(*p(i,k-1))]

### joking (94 bytes)
p=lambda i,k=19:-k*i or[[x.pop()or[0,*x][k%2-1]%5&6-(5in x)for _ in i]for*x,in zip(*p(i,k-1))]


##
p=lambda i,k=39:-k*i or[[x[-b]or 5in x[:-b]and 2-x[~b]%5&1-x[(-b<9)-b]for b in range(-9,1)]for x in zip(*p(i,k-1))]
p=lambda i,k=9:-k*i or[*zip(*[[x.pop()or[0,*x][-1]%5&6-(5in x)for _ in i]for*x,in zip(*p(i,k-1))])]

### combined (117 bytes)
p=lambda i,k=39:-k*i or[[x[b]or 5in x[:b]and 2-x[b-1]%5&1-x[b+(b<9)]for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
