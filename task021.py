p=lambda m:-~m.count(len(r:=m[0])*(a:=[*set(r)-{r[0]}]))*[-~r.count(*a)*r[:1]]
###
p=lambda m:-~m.count(len(r:=m[0])*(a:=[*set(r)-{b:=r[0]}]))*[-~r.count(*a)*[b]]
def p(m):*a,=set(r:=m[0])-{b:=r[0]};return[-~r.count(*a)*[b]]*-~m.count(a*len(r))
def p(m):a=min(set(r:=m[0])-{b:=r[0]});return[-~r.count(a)*[b]]*-~m.count([a]*len(r))
def p(m):a,b=sorted(set(r:=m[0]),key=r.count);return[-~r.count(a)*[b]]*-~m.count([a]*len(r))