# mwi (105 vs 98 bytes for gold)
import re
p=lambda g:[g:=eval(re.sub("([^2(]{9}2[^2)]{9})",r"*[\1][::-1]","%s"%[*zip(*g)]))for _ in g][1]

##
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=g[v:=k//4][5:7]==(2,2)and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=min(g[v:=k//4][5:7])%5and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:={*g[v:=k//4][5:7]}=={2}and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)

### ovs (109 bytes)
p=lambda g,k=59:-k*g or p([*zip(*g[:-(h:=g[v:=k//4].count(2)>4and k%4|1)+v]+g[v-h:v-~h][::-1]+g[v-~h:])],k-1)

##
p=lambda g:[g:=[*zip(*[g[a-sum(k*(g[a-k*8%15].count(2)>4)for k in b'	')]for a in range(15)])]for _ in g][1]
p=lambda g,k=29:-k*g or p([*zip(*g[v:=k//2].count(2)>4and g[:v-3]+[g[v-x]for x in b'\r']+g[v+4:]or g)],k-1)

### joking (114 bytes)
# this task is (almost) identical to task 390
p=lambda g,k=-1:k*g or p([*zip(*[g[a+sum(k*2for k in(2,3,-2,-3)if(g*2)[a+k].count(2)>4)]for a in range(15)])],k+1)

## ovs' solution
p=lambda g,k=-1:k*g or p([*zip(*[g[~sum(~k*2for k in(1,2,-3,-4)if g[k].count(2)>4)]for r in g if(g:=g[1:]+[r])])],k+1)

### combined (133 bytes)
p=lambda i,k=3:-k*i or p([[*[*zip(*i[::-1])][(1<abs(h:=(r:=[*map(max,*i)]).index(2)-l)<4==r.count(2))*2*h+l]]for l in range(15)],k-1)
