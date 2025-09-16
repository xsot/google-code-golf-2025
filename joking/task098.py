p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i,*w)]or i^min(w)

##
p=lambda i:[[y^min(t)for*t,y in zip(*w,[0]+s,s[1:]+[0],s)]for*w,s in zip(i[:1]+i,i[1:]+i,i)]
