# mwi (229 (238 unzipped) vs 218 bytes for gold)
p=lambda i,k=3:-k*i or p([[(y<1>k)*([*{*sum(i,[])}-{*sum([*zip(*i[b-(b>0):b+2])][a-(a>0):a+2],()),5},0]*2)[2]+(sum(x[b+1:])%5>0<sum(x[:b])%5>x[b-1]+x[b+1]==0<x[b-2]+x[b+2])*5or y for b,y in enumerate(x)]for a,x in enumerate(zip(*i))],k-1)

### combined (230 (234 unzipped) bytes)
p=lambda i,k=3,e=enumerate:-k*i or p([[(y<1>k)*([*{*sum(i,[])}-{*sum([*zip(*i[b-(b>0):b+2])][a-(a>0):a+2],()),5},0]*2)[2]+(sum(x[b+1:])%5>0<sum(x[:b])%5>x[b-1]+x[b+1]==0<x[b-2]+x[b+2])*5or y for b,y in e(x)]for a,x in e(zip(*i))],k-1)
