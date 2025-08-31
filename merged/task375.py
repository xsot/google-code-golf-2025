# combined (53 bytes, gold)
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g

### ovs (tied, 53 bytes)
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g

### xsot (66 bytes)
p=lambda m,i=0:exec("m[i][i]=m[i][n-(i:=i+1)]=0;"*(n:=len(m)))or m
##
p=lambda m,i=0:exec("m[i][n-1-i]=m[i][i]=0;i+=1;"*(n:=len(m)))or m
