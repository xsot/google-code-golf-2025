p=lambda g,w=[]:[[-v%12&6or(any(r[:j])*any(r[j:])|c)*8for j,v in enumerate(r)]for r in g if(w:=[r]*any(r)+w,c:=2in r!=r[0]!=w[-1][0]!=8in w.pop())]

##
p=lambda g,w=[]:[[-v%12&6or(2in{sum(r[:j]),sum(r[j:])}!=8in w[~sum(r[0]!=x[0]for x in w)])*8for j,v in enumerate(r)]for r in g if[w:=w+[r]*any(r)]]