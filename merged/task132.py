# combined (109 vs 86 bytes for gold)
p=lambda i,k=3:-k*i or p([[max({*i[a]}&{*y}|{*y[:a+1]}&{*y[a:]})for a in range(len(i))]for y in zip(*i)],k-1)
