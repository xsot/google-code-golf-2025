p=lambda g:[R[::-1][r.index(3):][:5]for r,R in zip(g,g[::-1])if 3in r]

### xsot (81 bytes)
p=lambda m:[m[15-(i:=sum(m,[]).index(3))//16-r][~i%-16::-1][:5]for r in range(5)]
# almost identical to 242
