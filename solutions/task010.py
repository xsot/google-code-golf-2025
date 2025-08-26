p=lambda g,c=[0]*9:[c:=[V or v%2*-~max(c)for V,v in zip(c,r)]for r in g]

### xsot (80 bytes)
p=lambda m:(d:={})or[[r[i]and(d:={i:len(d)+1}|d)[i]for i in range(9)]for r in m]
##
def p(m):d={};return[[r[i]and(d:={i:len(d)+1}|d)[i]for i in range(9)]for r in m]
def p(m):d={};return[[r[i]and d.setdefault(i,len(d)+1)for i in range(9)]for r in m]
