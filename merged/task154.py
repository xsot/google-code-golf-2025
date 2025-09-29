# ovs (110 vs 99 bytes for gold)
p=lambda g:[g:=[*zip(*[g[a-sum(k*(g[a-k*8%15].count(2)>4)for k in b'	')]for a in range(15)])]for _ in g][1]

### joking (114 bytes)
# this task is (almost) identical to task 390
p=lambda g,k=-1:k*g or p([*zip(*[g[a+sum(k*2for k in(2,3,-2,-3)if(g*2)[a+k].count(2)>4)]for a in range(15)])],k+1)

## ovs' solution
p=lambda g,k=-1:k*g or p([*zip(*[g[~sum(~k*2for k in(1,2,-3,-4)if g[k].count(2)>4)]for r in g if(g:=g[1:]+[r])])],k+1)

### combined (133 bytes)
p=lambda i,k=3:-k*i or p([[*[*zip(*i[::-1])][(1<abs(h:=(r:=[*map(max,*i)]).index(2)-l)<4==r.count(2))*2*h+l]]for l in range(15)],k-1)
