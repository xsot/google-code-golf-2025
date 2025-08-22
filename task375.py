p=lambda m,i=0:exec("m[i][i]=m[i][n-(i:=i+1)]=0;"*(n:=len(m)))or m
##
p=lambda m,i=0:exec("m[i][n-1-i]=m[i][i]=0;i+=1;"*(n:=len(m)))or m