# att (79 vs 75 bytes for gold)
p=eval('lambda a:[[9<sum(sum(a,()))'+'for*a,in map(zip,a,a[1:],a[2:])][::4]'*2)

### mwi (80 bytes)
r=0,4,8;p=lambda i:[[9<sum(sum(z[b:b+3])for z in i[a:a+3])for b in r]for a in r]

### combined (82 bytes)
p=lambda i,r=[0,4,8]:[[9<sum(sum(z[b:b+3])for z in i[a:a+3])for b in r]for a in r]

### xsot (83 bytes)
p=lambda m,a=[0,4,8]:[[sum(sum(m[r+i//4][c:c+3])for i in a)>7for c in a]for r in a]
##
p=lambda m,a=[0,4,8]:[[sum(sum(m[r+i][c:c+3])for i in[0,1,2])>7for c in a]for r in a]
p=lambda m,a=[0,4,8]:[[sum(m[r][c:c+3]+m[r+1][c:c+3]+m[r+2][c:c+3])>7for c in a]for r in a]
