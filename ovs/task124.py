p=lambda i:i[9:]and i or p(i+[((w:=i[4]!=i[1])*[0for k in(1,2)if[0]*k+i[0]>i[2]]+i[w-3])[:10]])

##

p=lambda i,n=-1,s=3:(r:=[(k//2*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1,2)
