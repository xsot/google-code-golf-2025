p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or[8,i]["0"in str(w)]

##
p=lambda i,*w,P=[[0]*20]:i*0!=0and[*map(p,i,P+i,i[1:]+P,*w)]or[8,i]["0"in str(w)]
p=lambda i,P=[[0]*20]*20,*w:P and[*map(p,i,P,P[:1]+i,i[1:]+P,*w)]or[8,i][0in w]