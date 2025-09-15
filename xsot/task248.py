def p(m,c=0,d=1):
 for r in m[::-1]:r[c]=1;c+=d;c%~-len(r)or(d:=-d)
 return m