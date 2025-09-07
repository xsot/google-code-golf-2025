p=lambda i:[[*map(max,*[s[t:t+3]for t in range(132)if(s:=sum(i*2,[]))[t-x]==5])]for x in b'mx\n']

##

R=-1,0,1
p=lambda g:[[max(f[I+i*11+j]for I in range(121)if(f:=sum(g,[]))[I]==5)for j in R]for i in R]
