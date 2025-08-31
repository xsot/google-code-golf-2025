# ovs (127 vs 109 bytes for gold)
E=enumerate
p=lambda g:[[v or max(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]}|{0})for j,(v,*c)in E(zip(r,*g))]for i,r in E(g)]
