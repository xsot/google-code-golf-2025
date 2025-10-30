# joking (130 bytes, gold)
exec("p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]"+'for %s in range(0,11,%s)%s'*4%(*'k4 l4)j1]i1]',))

### mwi (136 bytes)
R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]

### att (140 bytes)
R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j,b in e(r)]for i,r in e(a)]

##
# 136=current best
R=0,4,8;e=range(11);p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]

s='for*%c,in map(zip,*zip(*[iter([s]+%c)]*4))'*2+'][5:]';p=eval("lambda a:[[5*('\\''in'%r'%e)or int(f'{e}0'[str(d).find('4')])"+s*2%(*'dbecbaca',))
p=eval("lambda a,b=0:[p(c,d)"+"for*%c,in map(zip,[a[2]]+a,a[3:],a[7:])if(a:=b or a)"*2%(*'cd',)+"][5:]or('5'in'%s'%b)*5or int(f'{b}0'[str(a).find('4')])")
p=lambda a,b=[]:[p(c,d)for*c,in map(zip,[a[2]]+a,a[3:],a[7:])for*d,in map(zip,[a[2]]+b+a,(b+a)[3:],(b+a)[7:11])][5:]or('5'in'%s'%b)*5or int(f'{b}0'[str(a).find('4')])

### combined (143 bytes)
R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum({a[k+i%4][l+j%4]for k in R for l in R if 4==a[k+i//4][l+j//4]})for j,b in e(r)]for i,r in e(a)]
