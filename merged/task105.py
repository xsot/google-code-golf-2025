# ovs (139 vs 126 bytes for gold)
p=lambda g:[g:=[*map(lambda*r,j=0:[r[j:=j-1]or(1in[r*(m:=[*map(any,g)])[j],sorted(r)[-4]*m[j:]][1in m[:j]])*2for _ in r],*g)]for _ in g][3]

### joking (146 bytes)
p=lambda g:[g:=[[v or A([r*(m:=[*map(A,g)])[j],sorted(r)[-4]*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for A in[any]*4][3]

### mwi (153 bytes)
A=any;p=lambda g:[g:=[[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for _ in g][3]

### combined (154 bytes)
A=any
p=lambda g,k=-3:k*g or p([[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1],k+1)

### att (177 bytes)
p=lambda a,n=7,i=3:-n*a or a[:(b:=[*map(any,a)].index(1))]+[*zip(*p([*zip(*[[[c or~-i|sum(-d&2for d in b)//len(b)*2for c in b]*(i:=1)for b in a],a[b:]][n>3][::-1])],n-1))][::-1]
