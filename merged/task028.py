# joking+mwi (70 vs 63 bytes for gold)
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']

### ovs (tied, 70 bytes)
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']

### att (81 bytes)
h=lambda a:[(d:=[max(a)])*10,c:=d+[0]*8+d]*2+[c]
p=lambda a:h(a[2])+h(a[7])[::-1]
