import re
p=lambda g:[g:=eval(re.sub("([^2(]{9}2[^2)]{9})",r"*[\1][::-1]","%s"%[*zip(*g)]))for _ in g][1]

##
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=g[v:=k//4][5:7]==(2,2)and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=min(g[v:=k//4][5:7])%5and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:={*g[v:=k//4][5:7]}=={2}and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)