# joking+mwi (67 vs 64 bytes for gold)
p=lambda i:[[i[g:=len(i)//2][g+i[g].index(y)]for y in x]for x in i]

### att (69 bytes)
p=lambda a:[[(d:=a[l:=len(a)//2])[l+d.index(c)]for c in b]for b in a]

### ovs (92 bytes)
def p(g):f=sum(g,[]);C=sorted({*f},key=f.count);return[[C[~C.index(c)]for c in r]for r in g]
