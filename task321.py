p=lambda m:[[r.pop(0)or max(r[4::5])for _ in m]for r in m]
###
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in r[:4]]for r in m]
p=lambda m:[[r[i]or r[i+5]or r[i+10]for i in range(4)]for r in m]
p=lambda m:[[r[i]or r[i+5]or r[i+10]for i in[0,1,2,3]]for r in m]
p=lambda m:[[a or b or c for a,b,c in zip(r,r[5:],r[10:])]for r in m]