# ovs (148 vs 141 bytes for gold)
p=lambda g,*w:[[-v%12&6or(any(r[:j])*any(r[j:])|c)*8for j,v in enumerate(r)]for r in g if(w:=[r]*any(r)+[*w],c:=2in r!=r[0]!=w[-1][0]!=8in w.pop())]

### combined (169 bytes)
p=lambda i,l=[0],t=0:[[-y%12&6or(max(x[b:])*max(x[:b+1])>-l[0])*8for b,y in enumerate(x)]for x in i if(l:=l[(t:=t+(i[0]!=x[0])+(i[-1]!=(i:=x)[-1]))>4:]+[8in x]*(2in x))]
