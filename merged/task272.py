# att (101 vs 89 bytes for gold)
P=[[0]*9]
p=lambda g:[[v>>1-any(c)for*c,v in zip(*X,[0]+r,r[1:]+[0],r)]for*X,r in zip(P+g,g[1:]+P,g)]

### xsot (167 bytes)
def p(m):
 M,N=len(m),len(m[0])
 return[[m[r][c]>0<all(1>m[i][j]for i,j in[(r,c+1),(r,c-1),(r+1,c),(r-1,c)]if M>i>-1<j<N)or m[r][c]for c in range(N)]for r in range(M)]
