p=lambda i,*w,r=[[0]*9]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or~(2in w)*i%3

##
p=lambda i,r=[[0]*9]*9,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or~any(w)*i%3