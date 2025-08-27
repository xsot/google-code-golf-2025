R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum({a[k+i%4][l+j%4]for k in R for l in R if 4==a[k+i//4][l+j//4]})for j,b in e(r)]for i,r in e(a)]