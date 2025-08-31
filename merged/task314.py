# combined (102 vs 96 bytes for gold)
p=lambda i,r=range(8):[[((x:=i[a])[b-5]>1)*x[b-3]|(i[a-5][b]>1)*i[a-3][b]or x[b]for b in r]for a in r]
