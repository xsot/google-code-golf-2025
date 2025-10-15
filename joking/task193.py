p=lambda i,*w,r=['0'*25]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or(w.count(i)>1)*i

##
p=lambda i,r=[[0]*25]*25,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or(sum(w)>i)*i