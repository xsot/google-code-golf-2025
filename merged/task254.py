# mwi (91 vs 84 bytes for gold)
p=lambda i,r=[0]*9:[r:=[y or s>0and((x<i[8])is y)*2+1-any(r)for s,y in zip(x,r)]for x in i]

##
p=lambda i,r=[0]*9:[[*map(int,r:=[y or((x<i[8])+max(r))*s%3.7for s,y in zip(x,r)]),]for x in i]

def p(i):k=*zip(*i),;return[[y and(s==max(k))+2*(s==sorted({*k})[1])for y,s in zip(x,k)]for x in i]

### joking (92 bytes)
# probably can be improved further?
p=lambda i,r=[0]*9:[r:=[y or s>0and((x<i[-1])is y)*2+1-any(r)for s,y in zip(x,r)]for x in i]

##
def p(i):k=*zip(*i),;return[[x.pop(0)>>(s!=max(k))+2*(s!=sorted({*k})[1])for s in k]for x in i]
p=lambda i,r=[]:[r:=[y&3or s>0and((x<i[-1])is y)*2+1-any(r)for s,y in zip(x,r+x)]for x in i]

### ovs (93 bytes)
def p(i):k=*zip(*i),;return[[x.pop(0)>>(s<max(k))+2*(s>sorted({*k})[1])for s in k]for x in i]

### combined (103 bytes)
def p(i):k=*map(sum,zip(*i)),;return[[y and s//max(k)+min({*k}-{0})//s*2for y,s in zip(x,k)]for x in i]
