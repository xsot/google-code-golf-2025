p=lambda g:[[*map(max,*r)]for r in zip(g,g[6:])]

### xsot (54 bytes)
p=lambda m:[[*map(sum,zip(r,m.pop(6)))]for r in m[:5]]

##
p=lambda m:[[*map(sum,zip(r,m.pop(6)))]for r in m[:5]]
p=lambda m:m[6:]and[[*map(sum,zip(*m[::6]))]]+p(m[1:])
p=lambda m:[[*map(sum,zip(*m[r::6]))]for r in range(5)]
p=lambda m:[[x+y for x,y in zip(*m[r::6])]for r in range(5)]
p=lambda m:[[x+y for x,y in zip(m[r],m[r+6])]for r in range(5)]
p=lambda m:[[m[r][c]|m[r+6][c]for c in range(11)]for r in range(5)]
