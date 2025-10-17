# joking (67 bytes, gold)
p=lambda g:[g:=[V*-1*-1or v*sum(r)%6for V,v in zip(g,r)]for r in g]

### ovs (70 bytes)
p=lambda g,c=[0]*9:[c:=[V or v*sum(r)%6for V,v in zip(c,r)]for r in g]

### att (72 bytes)
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]

### combined (72 bytes)
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]

### xsot (80 bytes)
p=lambda m:(d:={})or[[r[i]and(d:={i:len(d)+1}|d)[i]for i in range(9)]for r in m]
##
def p(m):d={};return[[r[i]and(d:={i:len(d)+1}|d)[i]for i in range(9)]for r in m]
def p(m):d={};return[[r[i]and d.setdefault(i,len(d)+1)for i in range(9)]for r in m]
