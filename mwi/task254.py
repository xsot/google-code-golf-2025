p=lambda i,r=[0]*9:[r:=[y or s>0and((x<i[8])is y)*2+1-any(r)for s,y in zip(x,r)]for x in i]

##
def p(i):k=*zip(*i),;return[[y and(s==max(k))+2*(s==sorted({*k})[1])for y,s in zip(x,k)]for x in i]