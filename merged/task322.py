# mwi (48 vs 45 bytes for gold)
p=lambda a:[[*map(max,*a[:n]*2)]for n in(1,2,3)]

### att (49 bytes)
p=lambda a,b=[0]*9:[b:=[*map(max,b,r)]for r in a]

### ovs (49 bytes)
p=lambda g,c=[0]*3:[c:=[*map(max,c,r)]for r in g]

### xsot (49 bytes)
p=lambda m,s=[0]*3:[s:=[*map(max,s,r)]for r in m]
##
p=lambda m,r=[0]*3:m and[s:=[*map(max,m[0],r)]]+p(m[1:],s)
p=lambda m,r=[0]*3:m and[s:=[*map(sum,zip(m.pop(0),r))]]+p(m,s)
p=lambda m,r=[0]*3:m and[s:=[*map(sum,zip(m[0],r))]]+p(m[1:],s)

### combined (49 bytes)
p=lambda a,b=[0]*9:[b:=[*map(max,b,r)]for r in a]
