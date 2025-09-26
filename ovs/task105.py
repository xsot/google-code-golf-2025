A=any;p=lambda g:[g:=[[v or A([r*(m:=[*map(A,g)])[j],sorted(r)[-4]*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for _ in g][3]

##

p=lambda g:[g:=[[v or[any(r)*any(g[j]),sorted(r)[-4]>0!='1'in'%s'%g[j:]]['1'in'%s'%g[:j]]*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for _ in g][3]
