p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or i or any(w[:2])*any(w[2:])

##
p=lambda i,*w:i or any(w[:2])*any(w[2:])if w[3:]else[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]