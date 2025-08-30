# joking+mwi (70 vs ??? bytes for gold)
p=lambda i:[t[::-1][s.index(1):][:5]for s,t in zip(i,i[::-1])if 1in s]

### ovs (tied, 70 bytes)
p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]

### xsot (81 bytes)
p=lambda m:[m[23-(i:=sum(m,[]).index(1))//24-r][~i%-24::-1][:5]for r in range(5)]
# almost identical to 242
