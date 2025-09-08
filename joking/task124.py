p=lambda i,n=0,s=2:(r:=[(k//s*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+s%2,s^1)

##
p=lambda i,n=8:(r:=[(k//(t:=n//4)*(n%4)*[0]+i[k%t])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1)