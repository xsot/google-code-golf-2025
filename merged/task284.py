# joking (205 vs 201 bytes for gold)
p=lambda i:[i:=[*zip(*len(l:=[n for n,y in E(m)if y])%2*i)]or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[1])>>a**2&1)*m[l[X<0]]for a,_ in E(i,-i.index(m))]for b,_ in E(m)]for E in[enumerate]*2if[m:=max(i)]][1]

## one byte longer
def p(i):
 for E in[enumerate]*2:m=max(i);*i,=zip(*len(l:=[n for n,y in E(m)if y])%2*i or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[1])>>a**2&1)*m[l[X<0]]for b,_ in E(m)]for a,_ in E(i,-i.index(m))])
 return i

### ovs (208 bytes)
def p(i):
 for E in[enumerate]*2:m=max(i);*i,=zip(*len(l:=[n for n,y in E(m)if y])%2*i or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[-1])>>(a-i.index(m))**2&1)*m[l[X<0]]for b,_ in E(x)]for a,x in E(i)])
 return i

## same length:
p=lambda i:[i:=[*zip(*len(l:=[n for n,y in E(m)if y])%2*i or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[-1])>>(a-i.index(m))**2&1)*m[l[X<0]]for b,_ in E(x)]for a,x in E(i)])]for E in[enumerate]*2if[m:=max(i)]][1]

### combined (238 bytes)
def p(i,k=1,E=enumerate):
 m=max(i)
 if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[(abs(a-i.index(m))in[*(t-s-2)//2*[[0]],[0,1,2],[2],*[[]]*9][min(t-b,b-s)])*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return-k*i or p([*zip(*i)],k-1)
