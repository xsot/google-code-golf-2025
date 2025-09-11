# ovs (174 vs 151 bytes for gold)
# very slow (~200s locally)
def p(g):f=str(g+[E:=enumerate]*9);return[[v==8and int([K for k,K in E(f)if{'8'}=={f[32*i+2+j*3-k+h]for h,H in E(f)if{K,H}<{*'12345679'}}][0])for j,v in E(r)]for i,r in E(g)]

## faster solutions:

def p(g):f=str(g+[E:=enumerate]*9);W=[i for i,v in E(f)if v in'12345679'];return[[v==8and int([f[k]for k in W if{'8'}=={f[32*i+2+j*3-k+h]for h in W}][0])for j,v in E(r)]for i,r in E(g)]


def p(a,i=-1):
 for i in(I:={i//10+i:v*(v!=8)for v in sum(a,[])if[i:=i+1]*v}):s={i};[s.add(y)for y in[*I]*6if{y,y+1,y-1,y+11,y-11}&s];a[i//11][i%11]=I[[s for s in I if I[s]][sorted(s).index(i)]]-I[i]
 return a

## golf of other solution, 234:
def p(a):
 s=a;n,N=[len(s:=[r for*r,in zip(*s)if{*r}-{0,8}])for _ in'  ']
 for i in range(99):
  j=i%10;A=a[i//10:];t=[c[j:j+n]for c in A[:N]]
  for c,d in zip(s,A*(N+n==sum(map(any,(*t,*zip(*t)))))):d[j:j+n]=c*(t!=s)or[0]*n
 return a

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
