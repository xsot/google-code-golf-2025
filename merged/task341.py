# combined (139 vs 134 bytes for gold)
p=lambda i,k=1,r=range(10):-k*i or p([[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a-(a>0):a+2])*8for b in r]for a in r],k-1)
