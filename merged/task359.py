# ovs (64 vs 2500 bytes for gold)
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]

### combined (tied, 64 bytes)
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]
