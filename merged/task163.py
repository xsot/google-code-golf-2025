# mwi (136 bytes, gold)
R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]

### att (140 bytes)
R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j,b in e(r)]for i,r in e(a)]

### combined (143 bytes)
R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum({a[k+i%4][l+j%4]for k in R for l in R if 4==a[k+i//4][l+j//4]})for j,b in e(r)]for i,r in e(a)]
