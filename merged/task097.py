# ovs (95 bytes, gold)
*r,p=[0]*99,lambda i,*w:i*0!=0and[*map(p,*sum([[x,x[1:]+r,r+x]for x in[i,*w]],[]))]or(i in w)*i

### joking (96 bytes)
p=lambda i,*w,r=[[0]*99]:i*0!=0and[*map(p,*sum([[x,x[1:]+r,r+x]for x in[i,*w]],[]))]or(i in w)*i

##
p=lambda i,r=[[0]*99]*99,*w:r and[*map(p,*sum([[x,r,x[1:]+r,r[:1]+x]for x in[i,*w]],[]))]or any(w)*i

### combined (115 bytes)
p=lambda i,e=enumerate:[[y*(sum(sum([z[b-(b>0):b+2]for z in i[a-(a>0):a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
