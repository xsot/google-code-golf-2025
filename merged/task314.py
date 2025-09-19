# joking (82 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,i[:3]+i,i[3:]+i,*w)]or max(w[0]&w[1],w[2]&w[3],i)

### mwi (97 bytes)
p=lambda i,r=range(8):[[max((x:=i[a])[b-5]&x[b-3],i[a-5][b]&i[a-3][b],x[b])for b in r]for a in r]
##
p=lambda i,e=enumerate:[[max(y[b-5]&y[b-3],i[a-5][b]&i[a-3][b],x)for b,x in e(y)]for a,y in e(i)]
p=lambda i,r=range(8):[[((x:=i[a])[b-5]>1)*x[b-3]|(i[a-5][b]>1)*i[a-3][b]or x[b]for b in r]for a in r]

### combined (102 bytes)
p=lambda i,r=range(8):[[((x:=i[a])[b-5]>1)*x[b-3]|(i[a-5][b]>1)*i[a-3][b]or x[b]for b in r]for a in r]
