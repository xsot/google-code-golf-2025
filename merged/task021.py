# att (64 vs 57 bytes for gold)
p=eval('lambda a:[[a '+'for a in-~min(map(a.count,a))*a[:1]]'*2)

### ovs (67 bytes)
H=lambda w:1+min(map(w.count,w))
p=lambda g:[g[0][:1]*H(g[0])]*H(g)

### xsot (78 bytes)
p=lambda m:-~m.count(len(r:=m[0])*(a:=[*set(r)-{r[0]}]))*[-~r.count(*a)*r[:1]]
###
p=lambda m:-~m.count(len(r:=m[0])*(a:=[min(r,key=r.count)]))*[-~r.count(*a)*r[:1]]
p=lambda m:-~m.count(len(r:=m[0])*(a:=[*set(r)-{r[0]}]))*[-~r.count(*a)*r[:1]]
p=lambda m:-~m.count(len(r:=m[0])*(a:=[*set(r)-{b:=r[0]}]))*[-~r.count(*a)*[b]]
def p(m):*a,=set(r:=m[0])-{b:=r[0]};return[-~r.count(*a)*[b]]*-~m.count(a*len(r))
def p(m):a=min(set(r:=m[0])-{b:=r[0]});return[-~r.count(a)*[b]]*-~m.count([a]*len(r))
def p(m):a,b=sorted(set(r:=m[0]),key=r.count);return[-~r.count(a)*[b]]*-~m.count([a]*len(r))
