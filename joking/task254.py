# probably can be improved further?
p=lambda i,r=[0]*9:[r:=[y or s>0and((x<i[-1])is y)*2+1-any(r)for s,y in zip(x,r)]for x in i]

##
def p(i):k=*zip(*i),;return[[x.pop(0)>>(s!=max(k))+2*(s!=sorted({*k})[1])for s in k]for x in i]
p=lambda i,r=[]:[r:=[y&3or s>0and((x<i[-1])is y)*2+1-any(r)for s,y in zip(x,r+x)]for x in i]