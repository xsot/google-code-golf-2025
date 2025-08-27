p=lambda a:[r+r[::-1]for r in a+a[::-1]]

### ovs (tied, 40 bytes)
p=lambda g:[r+r[::-1]for r in g+g[::-1]]

### xsot (tied, 40 bytes)
p=lambda m:[l+l[::-1]for l in m+m[::-1]]
##
p=lambda m:(m:=[l+l[::-1]for l in m])+m[::-1]
p=lambda m:m and(l:=[m[0]+m[0][::-1]])+p(m[1:])+l
