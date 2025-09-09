# garry derived
def p(p):
 t={(l,n)for l in range(len(p))for n in range(len(p[0]))if p[l][n]&2};d=lambda i,l:[i and(d(i[1:],l)or not l&i[0]and d(i[1:],l|i[0])),l][t<=l]
 for n in 2,3:
  if l:=d([l for d in range(len(p))for i in range(len(p[0]))if(l:={(l,n)for l in range(-n,n+1)for l,n in[(d+l,i),(d,i+l)]if p[l:]and-1<n<len(p[0])})if min(p[l][n]for l,n in l)&2],set()):
   for l,n in l-t:p[l][n]+=3
   return p