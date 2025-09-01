R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]