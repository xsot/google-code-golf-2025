# att (101 vs 91 bytes for gold)
R=-1,0,1
p=lambda g:[[max(f[I+i*11+j]for I in range(121)if(f:=sum(g,[]))[I]==5)for j in R]for i in R]

### xsot (103 bytes)
p=lambda m:[[max(a[i+r+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in[-1,0,1]]for r in[-11,0,11]]
##
p=lambda m:[[max(a[i+r+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in[-1,0,1]]for r in[-11,0,11]]
p=lambda m,R=[-1,0,1]:[[max(a[i+r*11+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in R]for r in R]
p=lambda m,R=[-1,0,1]:[[max(m[y+r][x+c]for i in range(121)if m[y:=i//11][x:=i%11]==5)for c in R]for r in R]
p=lambda m:[[max(m[y+r][x+c]for x in range(11)for y in range(11)if m[y][x]==5)for c in[-1,0,1]]for r in[-1,0,1]]
