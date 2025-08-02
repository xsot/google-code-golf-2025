def p(m,E=enumerate):
 (a,b),(c,d)=[(r,c)for r,l in E(m)for c,v in E(l)if v]
 for i,j in[(0,0),(-1,0),(1,0),(0,-1),(0,1)]:m[(a+c)//2+i][(b+d)//2+j]=3
 return m