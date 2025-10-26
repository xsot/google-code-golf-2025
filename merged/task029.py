# att (110 vs 108 bytes for gold)
exec("p=lambda a,d=1:[i:="+'[b[1:-1]for*b,in zip(*'*2+"a)if d in b])if{d}<{*b}],0][d in sum(i,a)]or p(a,d+1)")

##
p=lambda a,n=1:[i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if n in b])if{n}<{*b}],0][n in sum(i,a)]or p(a,n+1)
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]

### joking (117 bytes)
exec("p=lambda a:min([d in sum(i:="+'[b[1:-1]for*b,in zip(*'*2+"a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]")

### combined (118 bytes)
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]

### ovs (131 bytes)
p=lambda g,c=0:[[*bytes(r).split(b'%c'%c)[1]]for r in g*(sum(1&~5>>r.count(c)for r in[*g,*zip(*g)])==4)if r.count(c)==2]or p(g,c+1)
