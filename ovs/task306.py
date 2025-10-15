p=lambda i:[i:=[*zip(*map(max,i,i[10:]+i[9:]+i))][::-1]for _ in i][7]
