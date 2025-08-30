# att (64 vs 63 bytes for gold)
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)

### joking+mwi (tied, 64 bytes)
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)

### xsot (tied, 64 bytes)
p=lambda m:eval("[[m "+"for m in m for _ in[*{*'%r'}][5:]]"%m*2)
##
p=lambda m:eval("[[m "+f"for m in m for _ in{[*{*str(m)}][5:]}]"*2)
p=lambda m:eval("[[m "+f"for m in m for _ in[0]*{len({*str(m)})-5}]"*2)
p=lambda m:eval("[[m "+"for m in m for _ in[0]*~-len({*%r})]"%sum(m,[])*2)

### ovs (74 bytes)
p=lambda g:(r:=lambda x:[v for v in x for _ in{*sum(g,[])}-{0}])(map(r,g))
