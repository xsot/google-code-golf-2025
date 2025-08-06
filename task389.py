p=lambda m:[[((e:=max(set(sum(m,[]))-{5}))!=v)*e for v in l]for l in m]
##
p=lambda m:[[*map({(e:=max(set(sum(m,[]))-{5})):0,5:e}.get,l)]for l in m]
p=lambda m:eval(str(m).translate({(e:=48+max(set(sum(m,[]))-{5})):48,53:e}))