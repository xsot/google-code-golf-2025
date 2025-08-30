# xsot (57 vs 55 bytes for gold)
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
###
p=lambda m:[[r.pop(0)or max(r[4::5])for _ in m]for r in m]
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in r[:4]]for r in m]
p=lambda m:[[r[i]or r[i+5]or r[i+10]for i in range(4)]for r in m]
p=lambda m:[[r[i]or r[i+5]or r[i+10]for i in[0,1,2,3]]for r in m]
p=lambda m:[[a or b or c for a,b,c in zip(r,r[5:],r[10:])]for r in m]

### ovs (63 bytes)
p=lambda g:[[max(r[a::5],key=bool)for a in(0,1,2,3)]for r in g]
