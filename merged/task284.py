# ovs (228 vs 220 bytes for gold)
def p(i):
 for E in[enumerate]*2:
  *i,=zip(*i);m=max(i)
  if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[([*(t-s-2)//2*[1],7,4,*[0]*4][min(t-b,b-s)]>>abs(a-i.index(m))&1)*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return i

### combined (238 bytes)
def p(i,k=1,E=enumerate):
 m=max(i)
 if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[(abs(a-i.index(m))in[*(t-s-2)//2*[[0]],[0,1,2],[2],*[[]]*9][min(t-b,b-s)])*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return-k*i or p([*zip(*i)],k-1)
