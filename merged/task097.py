# ovs (93 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,*sum([[x,x[1:]+[i*4],[i*4]+x]for x in[i,*w]],[]))]or(i in w)*i

### att (94 bytes)
*z,p=[0]*20,eval('lambda a:[[sorted(sum(a,()))[23]'+'for*a,in map(zip,*[a]*5,a[1:]+z,z+a)]'*2)

##
*z,p=[0]*20,eval('lambda a:[[a[0][0]*any(sum(a,())[1:])'+'for*a,in map(zip,a,a[1:]+z,z+a)]'*2)

### joking (96 bytes)
p=lambda i,*w,r=[[0]*99]:i*0!=0and[*map(p,*sum([[x,x[1:]+r,r+x]for x in[i,*w]],[]))]or(i in w)*i

##
p=lambda i,r=[[0]*99]*99,*w:r and[*map(p,*sum([[x,r,x[1:]+r,r[:1]+x]for x in[i,*w]],[]))]or any(w)*i

### combined (115 bytes)
p=lambda i,e=enumerate:[[y*(sum(sum([z[b-(b>0):b+2]for z in i[a-(a>0):a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
