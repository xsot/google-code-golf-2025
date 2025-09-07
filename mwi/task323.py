# 17 seconds, 152b
p=lambda i,r=range(13):[i:=[[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1]for _ in i][1]
## 3 seconds, 153b
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)