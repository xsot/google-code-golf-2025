def p(m):
 M,N=len(m),len(m[0])
 return[[m[r][c]>0<all(1>m[i][j]for i,j in[(r,c+1),(r,c-1),(r+1,c),(r-1,c)]if M>i>-1<j<N)or m[r][c]for c in range(N)]for r in range(M)]