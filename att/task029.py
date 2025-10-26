exec("p=lambda a,d=1:[i:="+'[b[1:-1]for*b,in zip(*'*2+"a)if d in b])if{d}<{*b}],0][d in sum(i,a)]or p(a,d+1)")

##
p=lambda a,n=1:[i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if n in b])if{n}<{*b}],0][n in sum(i,a)]or p(a,n+1)
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]