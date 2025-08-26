p=lambda m:[[3>>c+l.pop(4)for c in l[:3]]for l in m]
# p=lambda m:[[(not c+l.pop(4))*3for c in l[:3]]for l in m]
# p=lambda m:[[3-3*any(l[c::4])for c in[0,1,2]]for l in m]
# p=lambda m:[[3-3*any(m[r][c::4])for c in range(3)]for r in range(4)]
# p=lambda m:[[[3,0][any(m[r][c::4])]for c in range(3)]for r in range(4)]

### ovs (tied, {ovs_score} bytes)
p=lambda g:[[3>>a+r.pop(0)for a in r[4:]]for r in g]
