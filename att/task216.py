r=range(661)
p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]
# slow bruteforce

## fast
p=lambda a:max([d:=1,str(b:=[d for b in a[x%32:]if(d:=[c for c in b[x>>5:]if(d:=d*c)])]).count('2'),-x,b]for x in range(661))[3]