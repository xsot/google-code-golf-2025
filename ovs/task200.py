p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,i%7,c,i%6]*3)[:10]for i in b'6********M']

##

p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]
