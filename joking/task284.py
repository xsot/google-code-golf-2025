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