# combined (153 vs 2500 bytes for gold)
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)
