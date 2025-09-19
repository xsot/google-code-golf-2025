p=lambda i:[i:=[[(y==5)*c[c[1]>0]or y for*c,y in zip([0]+x,*i,x)][::-1]for x in i]for x in i][9]

## some recursive experiments
p=lambda i,*c:(i==5)*c[c[1]>0]or i if c else[i:=[[*map(p,x,[0]+x,*i)][::-1]for x in i]for x in i][9]
p=lambda i,k=10,*c:((i==5)*(c[0]or k)if c else k and p([[*map(p,x,[0]+x,*i)][::-1]for x in i],k-1))or i