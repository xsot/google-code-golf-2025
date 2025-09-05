# att (91 vs 2500 bytes for gold)
p=lambda a:[*map(f:=lambda*b,i=len(a)//2:[c and b[i]for c in b[:i]+b[i-1::-1]],*map(f,*a))]

### combined (tied, 91 bytes)
def p(i):t=len(i)//2;return[[y and x[t]for y in x[:t]+x[t-1::-1]]for x in i[:t]+i[t-1::-1]]
