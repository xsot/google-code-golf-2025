def p(i):e=range(len(i));return[[max((k:=i[t]+[0]*29)[b+t-a]|k[b-t+a]for t in e)for b in e]for a in e]

##

p=eval('lambda i:list(list(max((k:=i[t]+[0]*29)[b+t-a]|k[b-t+a]'+"for %s in range(len(i)))"*3%(*'tba',))
