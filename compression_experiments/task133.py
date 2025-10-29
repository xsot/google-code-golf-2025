def p(t):
 *r,d={n*66+l:(t)for n,t in enumerate(t)for l,t in enumerate(t)if t},
 for n in d:i={n};r=[f for f in r if f==f-{n-66,n-1}or i.update(f)]+[i]
 for f in r:
  for n in f:
   for i in f:
    e=f
    for e in 1//len([u for u in e if d[n]==d[u]])*r:
     for o in f-{i}:
      for u in[u for u in e if d[n]==d[u]==d[i]]:u+=(len([u for u in e if d[n]==d[u]==d[i]])^6)%6*(o-i);t[u//66][u%66],={d[u]for u in e}-{d[n]}
 return t