# joking (104 vs 99 bytes for gold)
p=lambda i:[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]for b in r]for a in r]for r in[range(19)]*5][4]


##
exec(f"p=lambda i:[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]{'for %s in range(19)]'*3%(*'ba_',)}[4]")
exec(f"p=lambda i:[i:=[[0{'|i[b][%sa]'*3}{'for %s in range(19)]'*3}[4]"%('a%2*(b<a<18-b)*b+2+0*',*'+~ba_'))

### mwi (106 bytes)
p=lambda i,r=range(19):[i:=[[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r]for _ in i][4]

### combined (107 bytes)
p=lambda i,k=4,r=range(19):-k*i or p([[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r],k-1)
