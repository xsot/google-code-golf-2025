# ovs (114 vs 112 bytes for gold)
p=lambda g,r=range(10):[[g[y][x]or max(sum([R:=g[y-9],*g][y:y+5],R))*any(R[:x+1])*any(R[x:])for x in r]for y in r]

### mwi (116 bytes)
p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y:y+4],g[y-1]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

##

p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y//5*5:][:5],[]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

### joking (119 bytes)
exec(("p=lambda g:[[g[y][x]or max(sum(g[y:y+4],g[y-1]))"+'*any(g[y-9][x::%s1])'*2+'for %s in range(10)]'*2)%(*'+-xy',))

### combined (150 bytes)
p=lambda i,k=19:-k*i or p([[-(y<e<0)or(y<0<1!=e!=-2)*e or y or-2*(e>1<k>14or-2==e)or-(k==19>1==e)for y,e in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
