# joking+mwi (55 bytes, gold)
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]

### ovs (tied, 55 bytes)
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
