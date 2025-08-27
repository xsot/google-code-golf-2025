p=lambda a,n=7,i=3:-n*a or a[:(b:=[*map(any,a)].index(1))]+[*zip(*p([*zip(*[[[c or~-i|sum(-d&2for d in b)//len(b)*2for c in b]*(i:=1)for b in a],a[b:]][n>3][::-1])],n-1))][::-1]

### ovs (266 bytes)
E=enumerate
def p(g):*t,=zip(*g);*f,=E(sum(g,[]));(y,*_,Y),(x,*_,X)=map(sorted,zip(*[divmod(i,len(t))for i,v in f if v]));return[[v or 2*any(x<=j<=X and y<=i<=Y and (sum(q)>1 or j in(x,X) or i in (y,Y)) for q in[l[x+1:X],t[j][y+1:Y]])for j,v in E(l)]for i,l in E(g)]
