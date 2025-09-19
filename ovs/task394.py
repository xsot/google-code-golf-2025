p=lambda i:[[x[:2*(n:=122%len(i))][b-n]for b,y in enumerate(x)if y<1]for x in i if 0in x]
