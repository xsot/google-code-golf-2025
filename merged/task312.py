# joking (44 bytes, gold)
p=lambda a:[[e%~e&r[0]for e in r]for r in a]

##
p=lambda a:[[e and r[0]for e in r]for r in a]
p=lambda a:[[[0,*r][e>0]for e in r]for r in a]
p=lambda m:[[*map({5:l[0]}.get,l,l)]for l in m]
p=lambda a:[[c]+[c*e//5for e in r]for c,*r in a]

### att (45 bytes)
p=lambda a:[[e and r[0]for e in r]for r in a]

### ovs (45 bytes)
p=lambda g:[[v and r[0]for v in r]for r in g]

### combined (45 bytes)
p=lambda i:[[(y>0)*x[0]for y in x]for x in i]

### xsot (51 bytes)
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
##
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
p=lambda m:[[i:=l.pop(0),*map({5:i,0:0}.get,l)]for l in m]
p=lambda m:[[l[0],*map({5:l[0],0:0}.get,l[1:])]for l in m]
p=lambda m:[eval(str(l).replace('5',str(l[0])))for l in m]
