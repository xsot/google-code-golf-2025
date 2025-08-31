# ovs (58 vs 56 bytes for gold)
p=lambda g:[[6-j%3&v%~5for j,v in enumerate(r)]for r in g]

### combined (tied, 58 bytes)
p=lambda i:[[8%~y&6-b%3for b,y in enumerate(x)]for x in i]

### att (59 bytes)
p=lambda a:[(i:=1)*[c|c>>1&(i:=-~i%3)for c in b]for b in a]
