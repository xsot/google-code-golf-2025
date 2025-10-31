# att (113 vs 111 bytes for gold)
# ~3:30 locally
p=lambda a:max([-(c:=sum(b:=[b[x%17:x%21]for b in a[x%19:x%22]],a).count)(0),c(2),c(1),b]for x in range(8**6))[3]

## older
# slow
r=range(661);p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]
# fast
p=lambda a:max([d:=1,str(b:=[d for b in a[x%32:]if(d:=[c for c in b[x>>5:]if(d:=d*c)])]).count('2'),-x,b]for x in range(661))[3]

### mwi (119 bytes)
# exact copy of ovs/task365.py, just changed grid size
# way slower though, grid is 20x20 instead of 10x10

# 119 bytes, approx 8 minutes
exec(f'p=lambda i:max((-{"str(s:=[x[a:b]for x in i[c:d]]).count(%r),"*3}s){"for %s in range(21)"*4})[3]'%(*"021abcd",))

## 121 bytes, approx 6 minutes
exec(f'p=lambda i:max((-{"sum(s:=[x[a:b]for x in i[c:d]],s).count(%s),"*3}s){"for %s in range(21)"*4})[3]'%(*"021abcd",))

### combined (125 bytes)
r=range(661)
p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]

### xsot (182 bytes)
def p(m):
 z=0,;a=sum(m,[])
 for i in range(400):y=i//20;x=i%20;z=max(z,(sum(z:=[l[x:x+[*a[i:],0].index(0)]for l in m[y:y+[*a[i::20],0].index(0)]],[]).count(2),-x,-y,z))
 return z[3]

# like 396 but easier

##
def p(m):
 z=0,;a=sum(m,[])
 for i in range(400):y=i//20;x=i%20;z=max(z,(sum(z:=[l[x:x+[*a[i:],0].index(0)]for l in m[y:y+[*a[i::20],0].index(0)]],[]).count(2),-x,-y,z))
 return z[3]

def p(m):
 z=0,
 for i in range(400):
  Y=y=i%20;X=x=i//20
  while-~X<20>0<m[y][X+1]:X+=1
  while-~Y<20>0<m[Y+1][x]:Y+=1;z=max(z,(sum(a:=[l[x:X+1]for l in m[y:Y+1]],[]).count(2),-x,-y,a))
 return z[3]
