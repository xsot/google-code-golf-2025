# joking (109 bytes, gold)
p=lambda g,E=enumerate:[[max({*r[:j+1]}&{*r[j::3]}|{*c[:i]}&{*c[i::3]})for j,c in E(zip(*g))]for i,r in E(g)]

### ovs (127 bytes)
E=enumerate
p=lambda g:[[v or max(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]}|{0})for j,(v,*c)in E(zip(r,*g))]for i,r in E(g)]

### combined (127 bytes)
E=enumerate
p=lambda g:[[v or max(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]}|{0})for j,(v,*c)in E(zip(r,*g))]for i,r in E(g)]
