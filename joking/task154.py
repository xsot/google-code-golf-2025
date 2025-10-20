import re
p=lambda g,*G:eval(re.sub("([^2(]{9}2[^2]{9})",r"*[\1][::-1]","%s"%[*zip(*G or p(g,*g))]))

## this task is (almost) identical to task 390
p=lambda g,k=-1:k*g or p([*zip(*[g[a+sum(k*2for k in(2,3,-2,-3)if(g*2)[a+k].count(2)>4)]for a in range(15)])],k+1)

## ovs' solution
p=lambda g,k=-1:k*g or p([*zip(*[g[~sum(~k*2for k in(1,2,-3,-4)if g[k].count(2)>4)]for r in g if(g:=g[1:]+[r])])],k+1)