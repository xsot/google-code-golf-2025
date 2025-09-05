# combined (62 vs 2500 bytes for gold)
p=lambda i:[[3%-~sum(x)or(2in y)*2for y in zip(*i)]for x in i]

### att (65 bytes)
p=lambda a:[[max({*r}-{2})or(2in c)*2for c in zip(*a)]for r in a]

### ovs (69 bytes)
p=lambda g:[[[*{1,3}&{*r},*{2}&{*c},0][0]for c in zip(*g)]for r in g]
