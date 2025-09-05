# joking (122 vs 99 bytes for gold)
# ovs' solution
# this task is (almost) identical to task 390
p=lambda g,k=-1:k*g or p([*zip(*[[*[g[k-~k]for k in(1,2,-3,-4)if g[k].count(2)>4],r][0]for r in g if(g:=g[1:]+[r])])],k+1)

### combined (133 bytes)
p=lambda i,k=3:-k*i or p([[*[*zip(*i[::-1])][(1<abs(h:=(r:=[*map(max,*i)]).index(2)-l)<4==r.count(2))*2*h+l]]for l in range(15)],k-1)
