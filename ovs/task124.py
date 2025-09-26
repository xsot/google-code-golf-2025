p=lambda i,n=-1,s=3:(r:=[(k//2*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1,2)
