# joking (73 vs 71 bytes for gold)
p=lambda g,t=[],s=0:g*0!=0and[*map(p,g,(t+g)[:6]*3,[g[5]]*17)]or(t>g)*s|g

### ovs (76 bytes)
p=lambda g,i=-1:[[v|(v<g[(i:=i+1)//17%6][i%17%6])*r[5]for v in r]for r in g]

##

p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]

### combined (77 bytes)
p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]

### att (79 bytes)
r=range(17)
p=lambda a:[[a[i][j]or a[i%6][j%6]and a[5][5]for j in r]for i in r]
