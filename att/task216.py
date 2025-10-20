# ~3:30 locally
p=lambda a:max([-(c:=sum(b:=[b[x%17:x%21]for b in a[x%19:x%22]],a).count)(0),c(2),c(1),b]for x in range(8**6))[3]

## older
# slow
r=range(661);p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]
# fast
p=lambda a:max([d:=1,str(b:=[d for b in a[x%32:]if(d:=[c for c in b[x>>5:]if(d:=d*c)])]).count('2'),-x,b]for x in range(661))[3]