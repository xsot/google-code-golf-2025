# att (57 bytes, gold)
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]

### combined (tied, 57 bytes)
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]

### xsot (62 bytes)
p=lambda m:[[v==5and sum({*sum(m,[])})-5for v in l]for l in m]

##
p=lambda m:[[sum({*sum(m,[])})-5-v*(v!=5)for v in l]for l in m]
p=lambda m:[[(v==5)*max({*m[0]+m[1]}-{5})for v in l]for l in m]
p=lambda m:[[(v==5)*max({*sum(m,[])}-{5})for v in l]for l in m]
p=lambda m:[[v==5and max({*sum(m,[])}-{5})for v in l]for l in m]
p=lambda m:[[(e:=max({*sum(m,[])}-{5}))*(e!=v)for v in l]for l in m]
p=lambda m:[[(e:=max(set(sum(m,[]))-{5}))*(e!=v)for v in l]for l in m]
p=lambda m:[[((e:=max(set(sum(m,[]))-{5}))!=v)*e for v in l]for l in m]
p=lambda m:[[*map({(e:=max(set(sum(m,[]))-{5})):0,5:e}.get,l)]for l in m]
p=lambda m:eval(str(m).translate({(e:=48+max(set(sum(m,[]))-{5})):48,53:e}))

### ovs (63 bytes)
p=lambda g:[[max({*sum(g,[])}-{5})*(v==5)for v in r]for r in g]
