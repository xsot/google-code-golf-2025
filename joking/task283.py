p=lambda i,*w,r=[[0]*10]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or-i%8*w.count(5)%5

##
p=lambda i,r=[[0]*25]*25,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or sum(w)%8*i//8