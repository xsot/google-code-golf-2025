# combined (106 vs 92 bytes for gold)
p=lambda i:[l for n in{*sum(i,[])}if len(l:=[[y[0]for y in zip(x,*i)if n in y]for x in i if n in x])<6][0]

### ovs (115 bytes)
p=lambda g:min([(h:=lambda g,k=-99:k*g or h([*zip(*g[C not in g[0]:][::-1])],k+1))(g)for C in{*sum(g,[])}],key=len)
