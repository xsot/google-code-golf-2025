p=lambda m:[[3-3*any(m[r][c::4])for c in range(3)]for r in range(4)]
# p=lambda m:[[3-3*any(m[r][c::4])for c in range(3)]for r in range(4)]
# p=lambda m:[[[3,0][any(m[r][c::4])]for c in range(3)]for r in range(4)]
# p=lambda m:[[[3,0][(m[r][c]>0)|(m[r][c+4]>0)]for c in range(3)]for r in range(4)]