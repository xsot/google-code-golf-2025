# ovs (141 vs 137 bytes for gold)
def p(a):r=range(len(a));*_,B,C=sorted(map(a.index,a));W=max(a[B]);return[[W>>max(i-B,B-i,abs(a[B].index(W)-j))%(C-B)*9for j in r]for i in r]

### att (143 bytes)
def p(a):r=range(len(a));X,Y=[(x:=i,j)for i in r for j in r if a[i][j]][1];return[[a[X][Y]*(max(X-i,i-X,Y-j,j-Y)%(x-X)<1)for j in r]for i in r]

### combined (143 bytes)
def p(a):r=range(len(a));X,Y=[(x:=i,j)for i in r for j in r if a[i][j]][1];return[[a[X][Y]*(max(X-i,i-X,Y-j,j-Y)%(x-X)<1)for j in r]for i in r]
