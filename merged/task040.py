# ovs (69 bytes, gold)
p=lambda i,c=50:[[y%~y&i[(c:=c-1)>>9][~c//5%-2]for y in x]for x in i]

##
p=lambda g,k=-1:k*g or p([[[v,g[0][q]][v>0in g[0]]for v in r]for*r,q in zip(*g,[0]*5+[9]*5)],k+1)

### joking (70 bytes)
p=lambda i,c=9:[[y%~y&i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]

##
p=lambda i,E=enumerate:[[y and i[-(a>4)][-(b>4)]for b,y in E(x)]for a,x in E(i)]
p=lambda i,r=range(10):[[i[a][b]and i[-(a>4)][-(b>4)]for b in r]for a in r]
p=lambda i,c=9:[[(y>0)*i[-((c:=c+1)>59)][-(c%10>4)]for y in x]for x in i]
p=lambda i,c=9:[[(y>0)*i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]

### combined (97 bytes)
p=lambda i,k=1:-k*i or p([[x[y]and min(i[-(4<y)])or x[y]for y in range(10)]for x in zip(*i)],k-1)
