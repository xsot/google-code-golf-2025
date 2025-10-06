exec("p=lambda g:[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*f[y])"+'for %s,f in enumerate(g)%s'*4%(*'y x','if f[y]))[0][1]*(D[0]<D[1][:1])',*'c]r]'))


##
exec("p=lambda g:[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*v)"+'for %s in range(len(g))%s'*4%(*'x y','if(v:=g[x][y])))and(D[0][0]<D[1][0])*D[0][1]',*'c]r]'))

## garry derived
def p(g):R=range(len(g));return[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*v)for x in R for y in R if(v:=g[x][y])))and(D[0][0]<D[1][0])*D[0][1]for c in R]for r in R]
##
p=lambda g,E=enumerate:[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*v)for x,s in E(g)for y,v in E(s)if v))and(D[0][0]<D[1][0])*D[0][1]for c,_ in E(x)]for r,x in E(g)]
p=lambda i,k=3,e=enumerate:-k*i or[[y|i[-1][i[a+b<(t:=len(x)-1)][-1]+b*2//t*i[-1][-1]+a*2//t*i[0][0]>=~max(a,b)%2]for b,y in e(x)]for a,x in e(zip(*p([*zip(*i[::-1])],k-1)))][::-1]