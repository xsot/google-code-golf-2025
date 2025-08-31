# att (41 vs 40 bytes for gold)
p=lambda a:[3*[1//len({*b})*5]for b in a]

### combined (tied, 41 bytes)
p=lambda g:[3*[1//len({*A})*5]for A in g]

### ovs (tied, 41 bytes)
p=lambda g:[3*[1//len({*r})*5]for r in g]

### xsot (tied, 41 bytes)
p=lambda m:[3*[1//len({*r})*5]for r in m]

##
p=lambda m:[3*[5*(len({*r})<2)]for r in m]
