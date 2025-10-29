# att (104 vs 102 bytes for gold)
p=lambda a,B=0:[[v|5*((b:=abs(B+(B:=B-3)//39*2+str(a).find('8')))>~b%76in b'KHE"')for v in r]for r in a]

### ovs (107 bytes)
p=lambda a,B=3:[[v|5*((b:=abs((B:=B-3)+str(a).find('8')))>~b%76in b'KHE"')for v in r]for r in a if[B:=B-2]]

##
p=lambda a,B=3:[[v|5*(~max(9,abs((B:=B-3)+str(a).find('8')))%76in b'KHE"')for v in r]for r in a if[B:=B-2]]

### joking (125 bytes)
p=lambda i,r=range(13):[[i[a][b]|5*(abs((y:=a-(n:=sum(i,[]).index(8))//13)-n%13-~b-(y>0)*2)<2-y%2>0!=y)for b in r]for a in r]

### mwi (152 bytes)
# 17 seconds, 152b
p=lambda i,r=range(13):[i:=[[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1]for _ in i][1]
## 3 seconds, 153b
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)

### combined (153 bytes)
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)
