# att (45 vs 44 bytes for gold)
p=lambda a:[[e and r[0]for e in r]for r in a]

### combined (tied, 45 bytes)
p=lambda i:[[(y>0)*x[0]for y in x]for x in i]

### ovs (tied, 45 bytes)
p=lambda g:[[v and r[0]for v in r]for r in g]

### xsot (51 bytes)
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
##
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
p=lambda m:[[i:=l.pop(0),*map({5:i,0:0}.get,l)]for l in m]
p=lambda m:[[l[0],*map({5:l[0],0:0}.get,l[1:])]for l in m]
p=lambda m:[eval(str(l).replace('5',str(l[0])))for l in m]
