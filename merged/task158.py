# xsot (269 (488 unzipped) bytes, gold)
def p(g):
 s,t=max((len({*str(a:=[R[x:x+3]for R in g[y:y+3]])}),a)for y in range(len(g))for x in range(len(g[1])))
 for s in range(len(g[1])):
  for y in range(len(g))[:-s*3]:
   for x in range(len(g[1]))[:-s*3]:
    for z in range(len(g[1])):
     t=*zip(*t[::-1]),
     for Y in range(s*3*all(g[y+Y][x+X]==t[Y//s][X//s]or g[y+Y][x+X]==g[1][-1]!=t[Y//s][X//s]==max({*t[1]}-{g[1][-1]})for Y in range(s*3)for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g

### mwi (306 (471 unzipped) bytes)
def p(g):
 o=g[0][-1];s,t=max((len({*sum(a:=[R[x:x+3]for R in g[y:y+3]],[])}),a)for y in range(len(g))for x in range(len(g[0])))
 for s in(1,2,3):
  for y in range(len(g)+1-3*s):
   for x in range(len(g[0])+1-3*s):
    for z in'range'*2:
     t=(t,[*zip(*t)])[z<'r'][::-1]
     for Y in range(s*3*all((a:=g[y+Y][x+X])==(b:=t[Y//s][X//s])or(a==o)*(b==max({*t[1]}-{o}))for Y in range(s*3) for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g

### combined (320 (441 unzipped) bytes)
def p(g):
 o=g[0][-1];e=enumerate;_,t=max((len({*sum(a:=[R[x:x+3]for R in g[y:y+3]],[])}),a)for y,r in e(g)for x,c in e(r))
 for s in[1,2,3]:
  for y,r in e(g[:1-3*s]):
   for x,c in e(r[:1-3*s]):
    for z in'range'*2:
     t=[t,[*zip(*t)]][z<'r'][::-1];R=range(s*3)
     if all((a:=g[y+Y][x+X])==(b:=t[Y//s][X//s])or(a==o)*(b==max({*t[1]}-{o}))for Y in R for X in R):
      for Y in R:
       for X in R:g[y+Y][x+X]=t[Y//s][X//s]
 return g

### garry_moss (323 (510 unzipped) bytes)
def p(n):o=max(n[0],key=n[0].count);f,=[r for a in(n,n[::-1])for g in range(len(n)-2)for h in range(len(n[0])-2)if len(set(r:=[a[g+p//3][h+p%3]for p in range(9)]))>3>0<o!=r[0]!=r[8]!=o];[(t:=lambda d=o,b=o,c=o,*z:[d]*u+[b]*u+[c]*u)(t(f[0]),t(),t(c=f[8]))!=[a[g+p][h:[h+3*u*s,None][h+3*u*s<0]:s]for p in range(3*u)]or exec('for p in range(3*u):a[g+p][h:[h+3*u*s,None][h+3*u*s<0]:s]=t(*f[p//u*3:])')for u in range(4)for s in(1,-1)for g in range(len(n)-3*u+1)for h in range(len(n[0]))for a in(n,n[::-1])];return n
