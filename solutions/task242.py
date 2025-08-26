p=lambda g:[r[::-1][r.index(0):][:3]for r in g if 0in r]

### xsot (81 bytes)
p=lambda m:[m[15-(i:=sum(m,[]).index(0))//16-r][~i%-16::-1][:3]for r in range(3)]
# p=lambda m:[m[15-(i:=sum(m,[]).index(0))//16-r][::-1][i%16:][:3]for r in range(3)]
# p=lambda m,R=range(3):[m[15-(i:=sum(m,[]).index(0))//16-r][::-1][i%16:i%16+3]for r in R]
# p=lambda m,R=range(3):[[m[15-(i:=sum(m,[]).index(0))//16-r][15-i%16-c]for c in R]for r in R]
