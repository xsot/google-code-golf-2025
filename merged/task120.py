# joking (78 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or[8,i]["0"in str(w)]

##
p=lambda i,*w,P=[[0]*20]:i*0!=0and[*map(p,i,P+i,i[1:]+P,*w)]or[8,i]["0"in str(w)]
p=lambda i,P=[[0]*20]*20,*w:P and[*map(p,i,P,P[:1]+i,i[1:]+P,*w)]or[8,i][0in w]

### ovs (80 bytes)
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or[8,i][w!=(i or 1,)*4]

##
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or(8-i)%8*(w==(i,)*4)+i

### combined (102 bytes)
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]
