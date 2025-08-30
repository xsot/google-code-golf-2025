def p(g):
 e=enumerate;t=sum(g,[]);t=max({*t}-{0},key=t.count);a=[g]
 for _ in a*6:
  for b in[[*zip(*b)]for b in a if str(t)in str(b)]+(a:=[]):
   a+=[[]]
   for r in b:a+=[any(r)and[*a.pop(),r]or[]]
 for s in a:
  for z in'range'*2:
   s=[s[::-1],[*zip(*s[::-1])]][z<'r'];h,w=len(s),len(s[0])
   for y,r in e(g[:1-h]):
    for x,c in e(r[:1-w]):
     for Y,R in e((u:=1)*s*all((u:=u and c!=t)*0+a in[c,t]for y,r in zip(s,g[y:y+h])for a,c in zip(y,r[x:x+w]))):
      for X,C in e(R):g[y+Y][x+X]=C*u+10
 return[[c%10 for c in r]for r in g]