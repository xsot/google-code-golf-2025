p=lambda m:[[*map(dict([*zip(m[1],r)][::-1]).get,m[1])]for r in m]
##
p=lambda m:[[*map(dict([*zip(m[1],r)][::-1]).get,m[1])]for r in m]
p=lambda m:[[dict([*zip(m[1],r)][::-1])[i]for i in m[1]]for r in m]
p=lambda m:[[dict(zip(m[1][::-1],r[::-1]))[i]for i in m[1]]for r in m]