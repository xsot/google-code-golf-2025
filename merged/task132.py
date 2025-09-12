# ovs (86 bytes, gold)
p=lambda i,v=0:[i:=[[v|(v:=v^sum({*A}&{*y}))for A in i]for y in zip(*i)]for _ in i][1]

### mwi (108 bytes)
p=lambda i:[i:=[[max({*i[a]}&{*y}|{*y[:a+1]}&{*y[a:]})for a in range(len(i))]for y in zip(*i)]for _ in i][3]

### combined (109 bytes)
p=lambda i,k=3:-k*i or p([[max({*i[a]}&{*y}|{*y[:a+1]}&{*y[a:]})for a in range(len(i))]for y in zip(*i)],k-1)
