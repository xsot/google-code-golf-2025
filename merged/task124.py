# ovs (95 bytes, gold)
p=lambda i:i[9:]and i or p(i+[((w:=i[4]!=i[1])*[0for k in(1,2)if[0]*k+i[0]>i[2]]+i[w-3])[:10]])

##

p=lambda i,n=-1,s=3:(r:=[(k//2*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1,2)

### joking (100 bytes)
p=lambda i,n=0,s=2:(r:=[(k//s*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+s%2,s^1)

##
p=lambda i,n=8:(r:=[(k//(t:=n//4)*(n%4)*[0]+i[k%t])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1)

### mwi (129 bytes)
p=lambda i,n=0,s=2:[([0]*n*k+x)[:10]for k in range(5)for x in(i[:s]==[x[n:]+n*[0]for x in i[s:s*2]])*i[:s]][:10]or p(i,n+s%2,s^1)

### combined (130 bytes)
p=lambda i,n=0,s=2:i[:s]==[x[n:]+n*[0]for x in i[s:s*2]]and[([0]*n*k+x)[:10]for k in range(5)for x in i[:s]][:10]or p(i,n+s%2,s^1)
