# att (52 vs 2500 bytes for gold)
p=eval('lambda a:[[a '+"for a in a for _ in'  ']"*2)

### xsot (tied, 52 bytes)
p=lambda m:eval("[[m "+"for m in m for _ in'00']"*2)

##
p=lambda m:eval("[[m "+"for m in m for _ in[0]*2]"*2)
exec("p=lambda m:[[e "+"for %s in %s for _ in[0]*2]"*2%(*"errm",))
p=lambda m:[[e for e in r for _ in[0]*2]for r in m for _ in[0]*2]
p=lambda m,x=[()]*2:[[e for e in r for()in x]for r in m for()in x]
p=lambda m:[((r+[0]+r)*len(r))[::len(r)+1]for r in m for _ in[0]*2]

### combined (tied, 52 bytes)
p=lambda i:[sum(zip(x,x),())for x in i for _ in".."]

### ovs (59 bytes)
r=lambda w:sum([[x]*2for x in w],[])
p=lambda g:r(map(r,g))
