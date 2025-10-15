p=lambda i,P=[[0]*20]*20,*w:P and[*map(p,i,P,P[:1]+i,i[1:]+P,*w)]or[8,i][0in w]

##
p=lambda i,*w,P=[[0]*20]:i*0!=0and[*map(p,i,P+i,i[1:]+P,*w)]or[8,i]["0"in"%s"%w]