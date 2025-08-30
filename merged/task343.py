# combined (112 vs 65 bytes for gold)
p=lambda i,n=2:(k:=[(x[:n]*9)[:15]for x in i])*all(x[:(j:=i[-1].index(0))]==m[:j]for x,m in zip(i,k))or p(i,n+1)
