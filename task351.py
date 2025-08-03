p=lambda m:[m[15-(i:=sum(m,[]).index(3))//16-r][~i%-16::-1][:5]for r in range(5)]
# almost identical to 242