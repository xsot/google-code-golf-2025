p=lambda g,i=-1:[[v|(v<g[(i:=i+1)//17%6][i%17%6])*r[5]for v in r]for r in g]

##

p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]
