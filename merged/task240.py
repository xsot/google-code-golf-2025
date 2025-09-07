# mwi (106 vs 99 bytes for gold)
p=lambda i,r=range(19):[i:=[[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r]for _ in i][4]

### combined (107 bytes)
p=lambda i,k=4,r=range(19):-k*i or p([[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r],k-1)
