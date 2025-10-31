# joking (64 vs 63 bytes for gold)
p=lambda i:[(h[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15]for h in i]

## pattern size is either 3 or 4, reversing or not
p=lambda i:[*zip(*((h:=[*zip(*i)])[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15])]
p=lambda i:[(x[:8-2*((r:=[*zip(*i)][:6])in[r[:3]*2,r[::-1]])]*3)[:15]for x in i]
p=lambda i:[(x[:8-2*all(l[:6]in[l[:3]*2,l[5::-1]]for l in i)]*3)[:15]for x in i]

### combined (112 bytes)
p=lambda i,n=2:(k:=[(x[:n]*9)[:15]for x in i])*all(x[:(j:=i[-1].index(0))]==m[:j]for x,m in zip(i,k))or p(i,n+1)
