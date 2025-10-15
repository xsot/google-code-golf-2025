p=lambda i,*w,r=[[0]*99]:i*0!=0and[*map(p,*sum([[x,x[1:]+r,r+x]for x in[i,*w]],[]))]or(i in w)*i

##
p=lambda i,r=[[0]*99]*99,*w:r and[*map(p,*sum([[x,r,x[1:]+r,r[:1]+x]for x in[i,*w]],[]))]or any(w)*i