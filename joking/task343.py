
p=lambda i:[*zip(*((h:=[*zip(*i)])[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15])]

## pattern size is either 3 or 4, reversing or not
p=lambda i:[(x[:8-2*((r:=[*zip(*i)][:6])in[r[:3]*2,r[::-1]])]*3)[:15]for x in i]
p=lambda i:[(x[:8-2*all(l[:6]in[l[:3]*2,l[5::-1]]for l in i)]*3)[:15]for x in i]