p=lambda g:[([4,0]*8)[(m:=max(g)).index(max(m))%2:][:len(g)]]*-~(i:=g.index(m))+g[i:-1]
