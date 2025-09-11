p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y:y+4],g[y-1]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

##

p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y//5*5:][:5],[]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]