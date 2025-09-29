# ovs (145 bytes, gold)
p=lambda i,a=-38:[[v-(str(i)[(a:=a+3)::35][:3]=='444')*(sum(t:=[*map(sum,i)])//sum(t[:t.index(0,1)]*2)+2^a//126)for v in r]for r in i if[a:=a+2]]

##

p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else y|(y-{0}and e-{0}or{0})if k else sum(x<len(y)for x in{*map(len,sum(i,[]))})**2%12%7for y,e in zip(x,[{0}]+x)]for*x,in zip(*i[::-1])],k-1)

### joking (156 bytes)
p=lambda i,r=range(10),S=sum:[[i[a][b]-S(S(t[b-1:b+2])for t in i[a-1:a+2])//36*(S(t:=[*map(S,i)])//S(t[:(h:=t.index(0,1))]*2)+2^(h<a))for b in r]for a in r]

### mwi (180 bytes)
# subtract from each cell
# if all 4 adjacent cells are non-zero
# and the y coord isnt on the first or last row.
# to check which color, we set t to the index of the empty row separating the yellow rectangles
# and check whether there are more yellow squares above it or below it
p=lambda g,r=range(10):[[g[y][x]-all(g[y-z%11][x-z//11]for z in b"	c")*(y%9>0)*(2|((y>(t:=g[1:].index(min(g))+1))!=(sum(sum(g[t:],[]))>sum(sum(g[:t],[])))))for x in r]for y in r]

### combined (199 bytes)
p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else(y|(y-{0}and e-{0}or{0}))if k else sorted({*map(len,sum(i,[]))}).index(len(y))**2%12%7for y,e in zip(x,[{*()},*x])]for x in zip(*i[::-1])],k-1)
