# ovs (71 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or~(2in w)*i%3

### joking (73 bytes)
p=lambda i,*w,r=[[0]*9]:i*0!=0and[*map(p,i,r+i,i[1:]+r,*w)]or~(2in w)*i%3

##
p=lambda i,r=[[0]*9]*9,*w:r and[*map(p,i,r,r[:1]+i,i[1:]+r,*w)]or~any(w)*i%3

### att (95 bytes)
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]

##
P=[[0]*9]
p=eval('lambda a:[[a[1][1]>>1-any(sum(a,())[1::2])'+'for*a,in map(zip,P+a,a,a[1:]+P)]'*2)

### combined (95 bytes)
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]

### xsot (167 bytes)
def p(m):
 M,N=len(m),len(m[0])
 return[[m[r][c]>0<all(1>m[i][j]for i,j in[(r,c+1),(r,c-1),(r+1,c),(r-1,c)]if M>i>-1<j<N)or m[r][c]for c in range(N)]for r in range(M)]
