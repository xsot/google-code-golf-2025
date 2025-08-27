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