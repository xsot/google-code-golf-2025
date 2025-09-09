# garry_moss (175 vs 167 bytes for gold)
def p(g):R=range(len(g));return[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),v*(~max(T)&1))for x in R for y in R if(v:=g[x][y])))and(D[0][0]<D[1][0])*D[0][1]for c in R]for r in R]

### joking (180 bytes)
p=lambda i,k=3,e=enumerate:-k*i or[[y|i[-1][i[a+b<(t:=len(x)-1)][-1]+b*2//t*i[-1][-1]+a*2//t*i[0][0]>=~max(a,b)%2]for b,y in e(x)]for a,x in e(zip(*p([*zip(*i[::-1])],k-1)))][::-1]

### combined (188 bytes)
p=lambda i,k=3,e=enumerate:-k*i or[[y|((a-~b>(t:=len(x)-1))*i[0][-1]+b*2//t*i[-1][-1]+a*2//t*i[0][0]<~max(a,b)%2)*i[-1][0]for b,y in e(x)]for a,x in e(zip(*p([*zip(*i[::-1])],k-1)))][::-1]
