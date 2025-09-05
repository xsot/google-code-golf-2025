# att (72 vs 2500 bytes for gold)
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]

### combined (tied, 72 bytes)
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]
