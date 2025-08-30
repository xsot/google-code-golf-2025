# att (64 vs 63 bytes for gold)
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)

### xsot (tied, 64 bytes)
p=lambda m:eval("[[m "+"for m in m for _ in[*{*'%r'}][5:]]"%m*2)

###
p=lambda m:eval("[[m "+f"for m in m for _ in[0]*{len({*str(m)})-5}]"*2)
p=lambda m:eval("[[m "+"for m in m for _ in[0]*%d]"%(len({*str(m)})-5)*2)
p=lambda m:eval("[[m "+"for m in m for _ in[0]*%d]"%~-len({*sum(m,[])})*2)

### ovs (82 bytes)
def p(g):c={*sum(g,[])}-{0};return[[v for v in r for _ in c]for r in g for _ in c]
