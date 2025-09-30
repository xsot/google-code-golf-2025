# joking (86 bytes, gold)
p=lambda i,r=range(9):[i[a][:4]+[i[a-a%3+1][b-b%3+5]*i[a%3][b%3]for b in r]for a in r]

### combined (88 bytes)
p=lambda i,r=range(9):[i[a][:4]+[i[a//3*3+1][b//3*3+5]*i[a%3][b%3]for b in r]for a in r]
