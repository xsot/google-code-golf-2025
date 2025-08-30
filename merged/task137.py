# att (143 bytes, gold)
def p(a):r=range(len(a));X,Y=[(x:=i,j)for i in r for j in r if a[i][j]][1];return[[a[X][Y]*(max(X-i,i-X,Y-j,j-Y)%(x-X)<1)for j in r]for i in r]
