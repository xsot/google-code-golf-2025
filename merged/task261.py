# att (47 bytes, gold)
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]

### combined (tied, 47 bytes)
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]

### ovs (48 bytes)
p=lambda g:[[v>>2for v in r]for r in[g.pop()]+g]

### xsot (48 bytes)
p=lambda m:eval(str([m.pop()]+m).replace(*'82'))
