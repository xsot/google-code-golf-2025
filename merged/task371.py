# ovs (109 vs 2500 bytes for gold)
def p(a):
 for i in[l:=len(a[0]),-l,1,0,-1]:b=sum(a,[]).index;i+=b(1,b(1)+1)+b(1)>>1;a[i//l][i%l]=3
 return a

### combined (114 bytes)
def p(a):
	b=sum(a,[]).index;d=b(1,b(1)+1)+b(1)>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a

### att (115 bytes)
def p(a):
	b=sum(a,[]).index;c=b(1);d=b(1,c+1)+c>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a

### xsot (155 bytes)
def p(m,E=enumerate):
 (a,b),(c,d)=[(r,c)for r,l in E(m)for c,v in E(l)if v]
 for i,j in[(0,0),(-2,0),(2,0),(0,-2),(0,2)]:m[a+c+i>>1][b+d+j>>1]=3
 return m

##
def p(m,E=enumerate):
 (a,b),(c,d)=[(r,c)for r,l in E(m)for c,v in E(l)if v]
 for i,j in[(0,0),(-1,0),(1,0),(0,-1),(0,1)]:m[(a+c)//2+i][(b+d)//2+j]=3
 return m
