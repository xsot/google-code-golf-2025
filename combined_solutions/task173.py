def p(g):
 e=enumerate;o=[(s,y,x)for y,r in e(g)for x,c in e(r)if any(s:=sum([r[x:x+3]for r in g[y:y+3]],[]))*s==s[::-1]and s[8:]]
 for a,y,x in o:
  for A,Y,X in o:
   for y,r in e(a*(len({*a})==3*any(all(a[y]in[r,V]for y,r in e(A))for V in{*a}))):g[Y+y//3][X+y%3]=r
 return g