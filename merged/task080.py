# compression_experiments (231 (301 unzipped) bytes, gold)
def p(f):n=f.index(min(f,key=set))+1;e={u*1j+o:f for u,f in enumerate(f[::n])for o,f in enumerate(f[::n])};return[[[f or[e[t:=u//n*1j+o//n],*[e[a+t-r]for r in e if(e[r]==e[a])*2>abs(t-r)]][-1]for o,f in enumerate(f)]for u,f in enumerate(f)]for a in e if all(e.get(a+1j**u)for u,f in enumerate(f))][-1]

### joking (232 (301 unzipped) bytes)
# zip fiddling
def p(g):E=g.index(min(g,key=set))+1;c={j*1j+i:g for j,g in enumerate(g[::E])for i,g in enumerate(g[::E])};return[[[g or[c[k:=j//E*1j+i//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for i,g in enumerate(g)]for j,g in enumerate(g)]for u in c if all(c.get(u+1j**j)for j,g in enumerate(g))][-1]

### mwi (250 (300 unzipped) bytes)
def p(g):E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in enumerate(g[::E])for j,V in enumerate(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in enumerate(b)]for a,b in enumerate(g)]for u in c if all(c.get(u+1j**P)for P,p in enumerate(g))][0]

### ovs (252 (272 unzipped) bytes)
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]

### combined (252 (272 unzipped) bytes)
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]
