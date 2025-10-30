# att (101 bytes, gold)
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]

### combined (tied, 101 bytes)
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]

### joking (102 bytes)
p=lambda a:[sorted([sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)),c]for c in range(10))[8][1:]]

### xsot (209 (213 unzipped) bytes)
def p(m,E=enumerate):d=min(a:=sum(m,[]),key=a.count);return[max([[sum(l[min(c):max(c)+1].count(d)for l in m[min(r):max(r)+1]),i]for i in{*a}-{d}for r,c in[zip(*[(r,c)for r,l in E(m)for c,v in E(l)if v==i])]])[1:]]

###
p=lambda m,E=enumerate:(d:=min(a:=sum(m,[]),key=a.count))and[max(s:=[[sum(l[min(c):max(c)+1].count(d)for l in m[min(r):max(r)+1]),i]for i in{*a}-{d}for r,c in[zip(*[(r,c)for r,l in E(m)for c,v in E(l)if v==i])]])[1:]]

def p(m,E=enumerate):
 s=[]
 for i in{*(a:=sum(m,[]))}-{d:=min(a,key=a.count)}:r,c=zip(*[(r,c)for r,l in E(m)for c,v in E(l)if v==i]);s+=[sum(l[min(c):max(c)+1].count(d)for l in m[min(r):max(r)+1]),i],
 return[max(s)[1:]]
