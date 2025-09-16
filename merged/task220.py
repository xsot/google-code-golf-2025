# ovs (91 vs 87 bytes for gold)
p=lambda i:[*eval("map(lambda*x,s=0:[-(s*2^s-7)%7>>y|(s:=y)for y in x][::-1],*"*4+"i))))")]

##

E=enumerate
p=lambda g:[[v or max(v*95%9for r in g[i+i%~i:i+2]for v in[0,*r][j:j+3])for j,v in E(l)]for i,l in E(g)]

### joking (93 bytes)
p=lambda i:[*eval("map(lambda*x,s=0:[[-(s*2^s-7)%7,s:=y][y>0]for y in x][::-1],*"*4+"i))))")]

##
p=lambda i,k=3:-k*i or[[y or-(s*2^s-7)%7for y,s in zip(x,[0,*x])]for x in zip(*p(i,k-1)[::-1])]

## the transformations are suspiciously either half or double, maybe usable?
p=lambda i,k=3:-k*i or[[y or s*2>>11%-~s%3for y,s in zip(x,[0,*x])]for x in zip(*p(i,k-1)[::-1])]

### combined (113 bytes)
p=lambda i,e=enumerate:[[y or max(max(s[b-(b>0):b+2])for s in i[a-(a>0):a+2])*5%9for b,y in e(x)]for a,x in e(i)]
