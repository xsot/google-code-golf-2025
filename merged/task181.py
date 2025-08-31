# att (67 bytes, gold)
def p(a):
	for b in a[:3]:c=6>>a[3][3];b[c:c+3]=b[5:2:-1]
	return a

### ovs (69 bytes)
p=lambda g:[(r[g[3][3]*2:6]+r[5:2:-1]+r[3:])[:9]for r in g[:3]]+g[3:]

### xsot (74 bytes)
p=lambda m:[[l[:6]+(x:=l[5:2:-1]),x+l[3:]][m[3][3]>0]for l in m[:3]]+m[3:]
##
p=lambda m:[[l[:6]+(x:=l[3:6][::-1]),x+l[3:]][m[3][3]>0]for l in m[:3]]+m[3:]
p=lambda m:[[[0]*3+(x:=l[3:6])+(y:=x[::-1]),y+x+[0]*3][m[3][3]>0]for l in m[:3]]+m[3:]
p=lambda m:[[[0]*3+(x:=l[3:6])+x[::-1],x[::-1]+x+[0]*3][m[3][3]>0]for l in m[:3]]+m[3:]
