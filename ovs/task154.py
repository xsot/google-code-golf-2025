p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=g[v:=k//4].count(2)>4and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)

##
p=lambda g:[g:=[*zip(*[g[a-sum(k*(g[a-k*8%15].count(2)>4)for k in b'	')]for a in range(15)])]for _ in g][1]
p=lambda g,k=29:-k*g or p([*zip(*g[v:=k//2].count(2)>4and g[:v-3]+[g[v-x]for x in b'\r']+g[v+4:]or g)],k-1)
