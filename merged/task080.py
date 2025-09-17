# mwi (250 (300 unzipped) bytes, gold)
def p(g):E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in enumerate(g[::E])for j,V in enumerate(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in enumerate(b)]for a,b in enumerate(g)]for u in c if all(c.get(u+1j**P)for P,p in enumerate(g))][0]

### ovs (252 (272 unzipped) bytes)
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]

### combined (252 (272 unzipped) bytes)
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]
