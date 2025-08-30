# att (154 vs 148 bytes for gold)
A=any
p=lambda g,k=-3:k*g or p([[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1],k+1)

### att (177 bytes)
p=lambda a,n=7,i=3:-n*a or a[:(b:=[*map(any,a)].index(1))]+[*zip(*p([*zip(*[[[c or~-i|sum(-d&2for d in b)//len(b)*2for c in b]*(i:=1)for b in a],a[b:]][n>3][::-1])],n-1))][::-1]
