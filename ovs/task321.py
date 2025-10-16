p=lambda m:[[r.pop(0)or r[4]|r[9]for _ in m]for r in m]

##
p=lambda g:[[max(r[a::5],key=bool)for a in(0,1,2,3)]for r in g]
