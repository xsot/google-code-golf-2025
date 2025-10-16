# joking (74 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,[i*4]+i,i[1:]+[i*4],*w)]or(i^1in w)+7&i*9

##
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or(i^1in w)+7&i*9

### combined (78 bytes)
p=lambda i,k=3:-k*i or[*zip(*eval(str(p(i,k-1)[::-1]).replace("2, 3","0,8")))]
