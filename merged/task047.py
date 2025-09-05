# ovs (55 vs 2500 bytes for gold)
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]

### combined (tied, 55 bytes)
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
