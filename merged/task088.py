# att (100 bytes, gold)
p=lambda a,n=44:a*(-3-n)or p([[d%~d&max(max(a))for d in c]for c in zip(*a[any(n*a[-1])-2::-1])],n-1)

### joking (104 bytes)
p=lambda i,k=79:[[v%~v&i[0][0]for v in r[1:-1]]for r in-k*i[1:-1]]or p([*zip(*i[any(i[-1])-2::-1])],k-1)

### ovs (107 bytes)
p=lambda i,k=79:[[v and i[0][0]for v in r[1:-1]]for r in-k*i[1:-1]]or p([*zip(*i[1-any(i[0]):])][::-1],k-1)

## this can probably shortened by doing the color replacement during the iteration, here is an attempt 2 bytes longer:
p=lambda i,k=3,t=0:-k*i[1:]or p([*zip(*[[v and t for v in c]for*c,in i if(t:=t or max(c))][k<3:][::-1])],k-1)

### combined (109 bytes)
p=lambda a,n=-3:n*a[1:-1]or p([a[1:],[[d and(b:=max(a[n%2]))for d in c]for c in zip(*a[:0:-1])]][e:=b>0],n+e)
