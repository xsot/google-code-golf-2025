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