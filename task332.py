p=lambda m:[eval("[x:=r.pop(0),3][x*~len(r)%2],"*len(r))for r in m]
##
p=lambda m:[eval("len(r)*(x:=r.pop(0))%2*3or x,"*len(r))for r in m]
p=lambda m:[eval("[x:=r.pop(0),3][x*~len(r)%2],"*len(r))for r in m]
p=lambda m:[eval("[x:=r.pop(0),3][~len(r)&(x>0)],"*len(r))for r in m]
p=lambda m:[eval("3*(len(r)&((x:=r.pop(0))>0))or x,"*len(r))for r in m]
p=lambda m:[[3*((r[j]>0)&len(r[j:]))or r[j]for j in range(len(r))]for r in m]
p=lambda m:[[3*(len(r)+j&(r[j]>0))or r[j]for j in range(len(r))]for r in m]