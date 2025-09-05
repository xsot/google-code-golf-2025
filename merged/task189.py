# joking (111 bytes, gold)
p=lambda i,r=range(6):[[i[a-6+(s:=i[6][0]%3)*3][b-6+(t:=i[0][6]%3)*3]/3*i[a//3-s][b//3-t]for b in r]for a in r]

### combined (140 bytes)
p=lambda i,e=enumerate:i[0][2]&i[2][0]>7and[[y and i[a//3][b//3]for b,y in e(x[3:])]for a,x in e(i[3:])]or[*zip(*p([*zip(*i[::-1])]))][::-1]
