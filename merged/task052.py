# att (41 vs 40 bytes for gold)
p=lambda a:[3*[1//len({*b})*5]for b in a]

### mwi (tied, 41 bytes)
p=lambda a:[3*[5*(b==b[:1]*3)]for b in a]

##

### ovs (tied, 41 bytes)
p=lambda g:[3*[1//len({*r})*5]for r in g]

### xsot (tied, 41 bytes)
p=lambda m:[3*[1//len({*r})*5]for r in m]

##
p=lambda m:[3*[5*(len({*r})<2)]for r in m]

### combined (tied, 41 bytes)
p=lambda g:[3*[1//len({*A})*5]for A in g]
