# mwi (129 vs 2500 bytes for gold)
p=lambda i,n=0,s=2:[([0]*n*k+x)[:10]for k in range(5)for x in(i[:s]==[x[n:]+n*[0]for x in i[s:s*2]])*i[:s]][:10]or p(i,n+s%2,s^1)

### combined (130 bytes)
p=lambda i,n=0,s=2:i[:s]==[x[n:]+n*[0]for x in i[s:s*2]]and[([0]*n*k+x)[:10]for k in range(5)for x in i[:s]][:10]or p(i,n+s%2,s^1)
