# combined (215 vs 129 bytes for gold)
p=lambda i,k=1,E=enumerate:-k*i or[[len({*x})>2and[l:=q[a]for q in zip(*i)if q.count(q[a])<4and(z:=[t for t in map(max,i)if t][0])!=q[a]]and[z,l][i[a][b]<1]or p([*zip(*i),],k-1)[b][a]for b,y in E(x)]for a,x in E(i)]
