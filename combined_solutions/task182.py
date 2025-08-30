def p(i,r=range(17)):
 z=[z[1:-1]for a in r for b in r if{*(z:=[x[b:b+6]for x in i[a:a+7]])[0]+z[-1]}=={5}][0]
 for a in r:
  for b in r:
   for n in range(5*all(f==(g>0)for s,t in zip(i[a:],z)for f,g in zip(s[b:],t[1:]))):i[a+n][b:b+5]=z[n][1:]
 return i