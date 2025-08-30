# att (65 vs 62 bytes for gold)
p=lambda a:[[max({*r}-{2})or(2in c)*2for c in zip(*a)]for r in a]

### ovs (69 bytes)
p=lambda g:[[[*{1,3}&{*r},*{2}&{*c},0][0]for c in zip(*g)]for r in g]
