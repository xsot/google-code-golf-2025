p=lambda g:[[v and r[0]for v in r]for r in g]

### xsot (51 bytes)
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
##
p=lambda m:[[(c==5)*l[0]or c for c in l]for l in m]
p=lambda m:[[i:=l.pop(0),*map({5:i,0:0}.get,l)]for l in m]
p=lambda m:[[l[0],*map({5:l[0],0:0}.get,l[1:])]for l in m]
p=lambda m:[eval(str(l).replace('5',str(l[0])))for l in m]
