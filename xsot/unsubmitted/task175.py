# none of these pass on the server
p=lambda m,R=range(21):[[eval("m[i][k:=j]"+"or m[k][i-j-~(k:=k-1)]"*5)for j in R]for i in R]

###
p=lambda m,R=range(21):[[eval("m[i][k:=j]"+"or m[k][i-j-~(k:=k-1)]"*5)for j in R]for i in R]
p=lambda m,R=range(1,22):[[eval("m[i-1][j-1]"+"or m[j:=j-1][i:=i-1]"*5)for j in R]for i in R]

p=lambda m,R=range(1,22):[[eval("m[i-1][j-1]"+"or m[j:=j-1][i:=i-1]"*5)for j in R]for i in R]
p=lambda m,R=range(21):[[eval("m[i][j]"+"or m[1+(j:=j-1)][1+(i:=i-1)]"*5)for j in R]for i in R]
p=lambda m,R=range(21):[[m[i][j]or m[j][i] or m[j-1][i-1]or m[j-2][i-2]or m[j-3][i-3]or m[j-4][i-4]for j in R]for i in R]

p=lambda m,R=range(21):[[m[i][j]or m[j][i]or m[j+1][i+1]or m[j-1][i-1]or m[j-2][i-2]or m[j-3][i-3]for j in R]for i in R]