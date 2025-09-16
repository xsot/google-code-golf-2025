# joking (79 vs 97 bytes for gold)
p=lambda i,P=[[0]*20]*20,*w:P and[*map(p,i,P,P[:1]+i,i[1:]+P,*w)]or[8,i][0in w]

### ovs (102 bytes)
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]

### combined (102 bytes)
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]
