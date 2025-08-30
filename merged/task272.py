# att (95 vs 89 bytes for gold)
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]

##
P=[[0]*9]
p=eval('lambda a:[[a[1][1]>>1-any(sum(a,())[1::2])'+'for*a,in map(zip,P+a,a,a[1:]+P)]'*2)

### combined (tied, 95 bytes)
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]

### ovs (101 bytes)
P=[[0]*9]
p=lambda g:[[v>>1-any(c)for*c,v in zip(*X,[0]+r,r[1:]+[0],r)]for*X,r in zip(P+g,g[1:]+P,g)]

### xsot (167 bytes)
def p(m):
 M,N=len(m),len(m[0])
 return[[m[r][c]>0<all(1>m[i][j]for i,j in[(r,c+1),(r,c-1),(r+1,c),(r-1,c)]if M>i>-1<j<N)or m[r][c]for c in range(N)]for r in range(M)]
