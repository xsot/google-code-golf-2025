# ovs (208 vs 201 bytes for gold)
def p(i):
 for E in[enumerate]*2:m=max(i);*i,=zip(*len(l:=[n for n,y in E(m)if y])%2*i or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[-1])>>(a-i.index(m))**2&1)*m[l[X<0]]for b,_ in E(x)]for a,x in E(i)])
 return i

## same length:
p=lambda i:[i:=[*zip(*len(l:=[n for n,y in E(m)if y])%2*i or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[-1])>>(a-i.index(m))**2&1)*m[l[X<0]]for b,_ in E(x)]for a,x in E(i)])]for E in[enumerate]*2if[m:=max(i)]][1]

### joking (221 (529 unzipped) bytes)
# 222
def p(i):i=[*zip(*i)];[i:=[[([*(l[1]-l[0]-2)//2*[1],7,4,4,7,*(l[1]-l[0]-2)//2*[1],*7*[0]][l[1]-b]>>abs(a)&1)*max(i)[l[l[1]-b<b-l[0]]]for b,x in enumerate(x)]for a,x in enumerate(i,-a)]for a,x in enumerate(i)if max(i)==x!=len(l:=[b for b,x in enumerate(x)if x])==2];i=[*zip(*i)];[i:=[[([*(l[1]-l[0]-2)//2*[1],7,4,4,7,*(l[1]-l[0]-2)//2*[1],*7*[0]][l[1]-b]>>abs(a)&1)*max(i)[l[l[1]-b<b-l[0]]]for b,x in enumerate(x)]for a,x in enumerate(i,-a)]for a,x in enumerate(i)if max(i)==x!=len(l:=[b for b,x in enumerate(x)if x])==2];return i

##
def p(i):#['''#['*i,=zip(*i)','i=[*zip(*i)]']##;[i:=[[([*(l[1]-l[0]-#[2,3]##)//2*[1],7,4,4,7,*(l[1]-l[0]-#[prev_vals[-1]]##)//2*[1],#['0,0,0,0',*['*[0]*%d'%d for d in range(4,10)],*['*%d*[0]'%d for d in range(4,10)]]##][#['l[1]-b','b-l[0]']##]>>abs(a)&1)*max(i)[l[l[1]-b<b-l[0]]]for b,x in enumerate(x)]for a,x in enumerate(i,-a)]for a,x in enumerate(i)if max(i)==x!=len(l:=[b for b,x in enumerate(x)if x])==2];'''*2]##return i

## non-zip, 227
# probably more viable to shorten this
def p(i):
 for E in[enumerate]*2:
  *i,=zip(*i);m=max(i)
  if~len(l:=[n for n,y in E(m)if y])&1:s,t=l;i=[[([*(t-s-2)//2*[1],7,4,*[0]*4][min(t-b,b-s)]>>abs(a-i.index(m))&1)*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return i

### combined (238 bytes)
def p(i,k=1,E=enumerate):
 m=max(i)
 if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[(abs(a-i.index(m))in[*(t-s-2)//2*[[0]],[0,1,2],[2],*[[]]*9][min(t-b,b-s)])*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return-k*i or p([*zip(*i)],k-1)
