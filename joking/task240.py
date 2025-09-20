p=lambda i:[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]for b in r]for a in r]for r in[range(19)]*5][4]


##
exec(f"p=lambda i:[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]{'for %s in range(19)]'*3%(*'ba_',)}[4]")