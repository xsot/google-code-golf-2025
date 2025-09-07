# joking (125 vs 102 bytes for gold)
p=lambda i,r=range(13):[[i[a][b]|5*(abs((y:=a-(n:=sum(i,[]).index(8))//13)-n%13-~b-(y>0)*2)<2-y%2>0!=y)for b in r]for a in r]

### mwi (152 bytes)
# 17 seconds, 152b
p=lambda i,r=range(13):[i:=[[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1]for _ in i][1]
## 3 seconds, 153b
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)

### combined (153 bytes)
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)
