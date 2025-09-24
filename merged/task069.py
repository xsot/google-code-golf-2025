# ovs (159 vs 151 bytes for gold)
def p(g):E=enumerate;*f,=E(sum(zip(*g*2),()));return[[sum(V*all((i+j*20-I+J,8)in f for J,V in f if V%8)for I,V in f if v==8!=V)for j,v in E(r)]for i,r in E(g)]

### mwi (207 bytes)
def p(a,i=-1):
 for i in(I:={i//10+i:v*(v!=8)for v in sum(a,[])if[i:=i+1]*v}):s={i};[s.add(y)for y in[*I]*6if{y+1,y-1,y+11,y-11}&s];a[i//11][i%11]=I[[s for s in I if I[s]][sorted(s).index(i)]]-I[i]
 return a

### combined (209 bytes)
def p(a,i=-1):
 for i in(I:={i//10+i:v*(v!=8)for v in sum(a,[])if[i:=i+1]*v}):s={i};[s.add(y)for y in[*I]*6if{y,y+1,y-1,y+11,y-11}&s];a[i//11][i%11]=I[[s for s in I if I[s]][sorted(s).index(i)]]-I[i]
 return a

### att (244 (251 unzipped) bytes)
def p(a):
	f=lambda b:[c for*c,in zip(*b)if{*c}-{0,8}];s=f(f(a));n=len(s[0])
	for i in range(99):
		j=i%10;i//=10;t=[c[j:j+n]for c in a[i:i+len(s)]]
		for c,d in zip(s,a[i:]*(t in[s,[[d and 8for d in c]for c in s]])):d[j:j+n]=c*(t!=s)or[0]*n
	return a
