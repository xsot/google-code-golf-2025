# joking (136 vs 132 bytes for gold)
p=lambda i:[i:=[[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a+a%~a:a+2])*8for b in r]for a in r]for r in[range(10)]*2][1]

### mwi (137 bytes)
p=lambda i,r=range(10):[i:=[[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a+a%~a:a+2])*8for b in r]for a in r]for _ in i][1]

### ovs (138 bytes)
p=lambda i,k=1,r=range(10):-k*i or p([[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a+a%~a:a+2])*8for b in r]for a in r],k-1)

### combined (139 bytes)
p=lambda i,k=1,r=range(10):-k*i or p([[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a-(a>0):a+2])*8for b in r]for a in r],k-1)
