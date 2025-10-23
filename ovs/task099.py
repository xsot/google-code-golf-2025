p=lambda g,r=range(10):[[g[y][x]or max(sum([R:=g[y-9],*g][y:y+5],R))*any(R[:x+1])*any(R[x:])for x in r]for y in r]
