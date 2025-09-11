# mwi (116 vs 115 bytes for gold)
p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y:y+4],g[y-1]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

##
p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y//5*5:][:5],[]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

### ovs (149 bytes)
p=lambda i,k=19:-k*i or p([[-(y<e<0)or(y<0<1!=e!=-2)*e or y or-2*(e>1<k>14or-2==e)or-(k==19>1==e)for y,e in zip(x,[0]+x)]for*x,in zip(*i[::-1])],k-1)

### combined (150 bytes)
p=lambda i,k=19:-k*i or p([[-(y<e<0)or(y<0<1!=e!=-2)*e or y or-2*(e>1<k>14or-2==e)or-(k==19>1==e)for y,e in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
