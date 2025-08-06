p=lambda m:(m:=[l+l[::-1]for l in m])+m[::-1]
#
p=lambda m:m and(l:=[m[0]+m[0][::-1]])+p(m[1:])+l