# ovs (121 vs 129 bytes for gold)
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]

### joking+mwi (215 bytes)
p=lambda i,k=1,E=enumerate:-k*i or[[len({*x})>2and[l:=q[a]for q in zip(*i)if q.count(q[a])<4and(z:=[t for t in map(max,i)if t][0])!=q[a]]and[z,l][i[a][b]<1]or p([*zip(*i),],k-1)[b][a]for b,y in E(x)]for a,x in E(i)]
