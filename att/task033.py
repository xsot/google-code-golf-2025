r=range(17)
p=lambda a:[[a[i][j]or a[i%6][j%6]and a[5][5]for j in r]for i in r]