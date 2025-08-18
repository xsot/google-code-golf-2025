p=lambda m,s=[0]*3:[s:=[*map(max,s,r)]for r in m]
##
p=lambda m,r=[0]*3:m and[s:=[*map(max,m[0],r)]]+p(m[1:],s)
p=lambda m,r=[0]*3:m and[s:=[*map(sum,zip(m.pop(0),r))]]+p(m,s)
p=lambda m,r=[0]*3:m and[s:=[*map(sum,zip(m[0],r))]]+p(m[1:],s)