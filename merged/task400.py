p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]

### xsot (81 bytes)
p=lambda m:[m[23-(i:=sum(m,[]).index(1))//24-r][~i%-24::-1][:5]for r in range(5)]
# almost identical to 242
