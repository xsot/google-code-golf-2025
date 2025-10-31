# combined (85 vs 83 bytes for gold)
p=lambda i,k=39:-k*i or p([*zip(*eval(str(i).replace(*"10"))[any(i[-1])-2::-1])],k-1)

### att (86 bytes)
p=lambda a,n=-23:n*a or p([[d*(d>1)for d in c]for c in zip(*a[a<[[0]*9]:])][::-1],n+1)

### ovs (125 bytes)
def p(g):g=[[v*(v!=max(f:=sum(g,[]),key=f.count))for v in r]for r in g];exec("g[:]=zip(*g[any(g[0])<1:][::-1]);"*40);return g
