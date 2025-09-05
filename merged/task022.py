# mwi (98 vs 2500 bytes for gold)
p=lambda i:[[*map(max,*[s[t:t+3]for t in range(144)if(s:=sum(i*2,i))[t+x]==5])]for x in[12,1,-10]]

### combined (99 bytes)
p=lambda i:[[*map(max,*[s[t:t+3]for t in range(144)if(s:=sum(i*2,i))[t-x]==5])]for x in[-12,-1,10]]

### ovs (101 bytes)
R=-1,0,1
p=lambda g:[[max(f[I+i*11+j]for I in range(121)if(f:=sum(g,[]))[I]==5)for j in R]for i in R]

### xsot (103 bytes)
p=lambda m:[[max(a[i+r+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in[-1,0,1]]for r in[-11,0,11]]
##
p=lambda m:[[max(a[i+r+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in[-1,0,1]]for r in[-11,0,11]]
p=lambda m,R=[-1,0,1]:[[max(a[i+r*11+c]for i in range(121)if(a:=sum(m,[]))[i]==5)for c in R]for r in R]
p=lambda m,R=[-1,0,1]:[[max(m[y+r][x+c]for i in range(121)if m[y:=i//11][x:=i%11]==5)for c in R]for r in R]
p=lambda m:[[max(m[y+r][x+c]for x in range(11)for y in range(11)if m[y][x]==5)for c in[-1,0,1]]for r in[-1,0,1]]
