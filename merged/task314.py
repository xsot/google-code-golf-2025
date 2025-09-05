# mwi (97 vs 2500 bytes for gold)
p=lambda i,r=range(8):[[max((x:=i[a])[b-5]&x[b-3],i[a-5][b]&i[a-3][b],x[b])for b in r]for a in r]
##
p=lambda i,e=enumerate:[[max(y[b-5]&y[b-3],i[a-5][b]&i[a-3][b],x)for b,x in e(y)]for a,y in e(i)]
p=lambda i,r=range(8):[[((x:=i[a])[b-5]>1)*x[b-3]|(i[a-5][b]>1)*i[a-3][b]or x[b]for b in r]for a in r]

### combined (102 bytes)
p=lambda i,r=range(8):[[((x:=i[a])[b-5]>1)*x[b-3]|(i[a-5][b]>1)*i[a-3][b]or x[b]for b in r]for a in r]
