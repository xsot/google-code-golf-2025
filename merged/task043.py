# att (57 vs 2500 bytes for gold)
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]

### combined (tied, 57 bytes)
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]

### xsot (58 bytes)
p=lambda m:[[x|y*r[9]%23for x,y in zip(r,m[0])]for r in m]
##
p=lambda m:[[x|y*r[9]%23for x,y in zip(r,m[0])]for r in m]
p=lambda m:[[x or y*r[9]%23for x,y in zip(r,m[0])]for r in m]
p=lambda m:m[:1]+[[x*r[9]%23for x in m[0][:9]]+r[9:]for r in m[1:]]
p=lambda m:m[:1]+[[x*r[9]and 2for x in m[0][:9]]+r[9:]for r in m[1:]]
# x y r[9] out
# 0 * 0    0
# 0 0 *    0
# 5 5 0    5
# 5 0 5    5
# 0 5 5    2

### ovs (60 bytes)
p=lambda g:[[v+c*r[-1]//12for c,v in zip(g[0],r)]for r in g]
