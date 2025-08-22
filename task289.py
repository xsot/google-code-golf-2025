p=lambda m:eval("[[m "+"for m in m for _ in[*{*'%r'}][5:]]"%m*2)

###
p=lambda m:eval("[[m "+f"for m in m for _ in[0]*{len({*str(m)})-5}]"*2)
p=lambda m:eval("[[m "+"for m in m for _ in[0]*%d]"%(len({*str(m)})-5)*2)
p=lambda m:eval("[[m "+"for m in m for _ in[0]*%d]"%~-len({*sum(m,[])})*2)