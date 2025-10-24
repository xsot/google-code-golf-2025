# ovs (103 bytes, gold)
p=lambda g,R=[]:g and p(g[:-1],w:=[g[-1][x]or(1in R[x:]>[1])*max(sum(g[-2:],R))for x in range(10)])+[w]

##
p=lambda g:[g:=[[r[x]or(1in g[0][x:]>[1])*max(g[8]+r+g[0])for x in range(10)]]+g[:9]for r in g[::-1]][9]

### mwi (116 bytes)
p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y:y+4],g[y-1]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

##

p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y//5*5:][:5],[]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]

### joking (119 bytes)
exec(("p=lambda g:[[g[y][x]or max(sum(g[y:y+4],g[y-1]))"+'*any(g[y-9][x::%s1])'*2+'for %s in range(10)]'*2)%(*'+-xy',))

### combined (150 bytes)
p=lambda i,k=19:-k*i or p([[-(y<e<0)or(y<0<1!=e!=-2)*e or y or-2*(e>1<k>14or-2==e)or-(k==19>1==e)for y,e in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
