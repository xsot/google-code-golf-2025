# ovs (124 vs 118 bytes for gold)
p=lambda g,*w:[[-v%12&6|(c:=c^(8in r*v))*8>>v for v in r]for r in g if[c:=any(r)and(w:=[r,*w])[0][0]!=g[4][0]!=8in w.pop()]]

### joking (147 bytes)
p=lambda g,w=[]:[[-v%12&6or(any(r[:j])*any(r[j:])|c)*8for j,v in enumerate(r)]for r in g if(w:=[r]*any(r)+w,c:=2in r!=r[0]!=w[-1][0]!=8in w.pop())]

##
p=lambda g,w=[]:[[-v%12&6or(2in{sum(r[:j]),sum(r[j:])}!=8in w[~sum(r[0]!=x[0]for x in w)])*8for j,v in enumerate(r)]for r in g if[w:=w+[r]*any(r)]]

### combined (169 bytes)
p=lambda i,l=[0],t=0:[[-y%12&6or(max(x[b:])*max(x[:b+1])>-l[0])*8for b,y in enumerate(x)]for x in i if(l:=l[(t:=t+(i[0]!=x[0])+(i[-1]!=(i:=x)[-1]))>4:]+[8in x]*(2in x))]
