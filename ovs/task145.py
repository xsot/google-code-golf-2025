p=lambda x,k=79,v=9:-k*x or p([[(max(a,b or(v:=v+1))*(k>0)or max(h:={*map(C:=(f:=sum(x,[])).count,{*f}-{2})})==C(b)or(C(b)==min(h))*8,b)[b==2]for a,b in zip([0]+r,r)]for*r,in zip(*x[::-1])],k-1)

## this (barely?) exceeds recursion limit. passes on my testing notebook:

p=lambda x,k=3:-k*x or p([[(max(a,b or(k:=k+4))*(k>0)or max(h:={*map(C:=(f:=sum(x,[])).count,{*f}-{2})})==C(b)or(C(b)==min(h))*8,b)[b==2]for a,b in zip([0]+r,r)]for*r,in zip(*x[::-1])],k-1)
