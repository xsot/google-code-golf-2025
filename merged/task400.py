# joking (68 vs 67 bytes for gold)
p=lambda g:[h[:5]for r in[*g]if(h:=g.pop()[::-1][[*r,1].index(1):])]

### ovs (70 bytes)
p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]

### combined (70 bytes)
p=lambda i:[t[::-1][s.index(1):][:5]for s,t in zip(i,i[::-1])if 1in s]

### xsot (81 bytes)
p=lambda m:[m[23-(i:=sum(m,[]).index(1))//24-r][~i%-24::-1][:5]for r in range(5)]
# almost identical to 242
