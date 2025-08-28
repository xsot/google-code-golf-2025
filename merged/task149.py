p=lambda m,a=[0,4,8]:[[sum(sum(m[r+i//4][c:c+3])for i in a)>7for c in a]for r in a]
##
p=lambda m,a=[0,4,8]:[[sum(sum(m[r+i][c:c+3])for i in[0,1,2])>7for c in a]for r in a]
p=lambda m,a=[0,4,8]:[[sum(m[r][c:c+3]+m[r+1][c:c+3]+m[r+2][c:c+3])>7for c in a]for r in a]