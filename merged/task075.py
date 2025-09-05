# combined (88 vs 2500 bytes for gold)
p=lambda i,r=range(9):[i[a][:4]+[i[a//3*3+1][b//3*3+5]*i[a%3][b%3]for b in r]for a in r]
