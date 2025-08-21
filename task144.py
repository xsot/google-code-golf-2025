p=lambda m:[[3>>c+d for c,d in zip(*r)]for r in zip(m,m[5:])]
##
p=lambda m:[[3>>c+d for c,d in zip(m.pop(5),r)]for r in m[:4]]
p=lambda m:[[3-3*any(c)for c in zip(*r)]for r in zip(m,m[5:])]
p=lambda m:m[5:]and[[3-3*any(c)for c in zip(*m[::5])]]+p(m[1:])
p=lambda m:m[5:]and[[3-3*any(c)for c in zip(m.pop(0),m[4])]]+p(m)