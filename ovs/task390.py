p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=g[v:=k//4].count(2)>4and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)
##

p=lambda g:[g:=[*zip(*[g[a-sum(k for k in b'	'if g[a-k*8%15].count(2)>4)]for a in range(15)])]for _ in g][1]
p=lambda g,k=-1:k*g or p([*zip(*[[*[g[k-~k]for k in(1,2,-3,-4)if g[k].count(2)>4],r][0]for r in g if(g:=g[1:]+[r])])],k+1)
