# joking+mwi (220 (235 unzipped) vs 204 bytes for gold)
def p(i,n=4,r=range(10)):
 for a in r:
  for b in r:
   i[b]+=0,;i+=i[0],
   if all(all(x[b:b+n])for x in i[a:a+n]):return[[max(i[x][y],i[a+n+b+~y][b-a+x],i[a-b+y][b+n+a+~x],i[2*a+n+~x][2*b+n+~y])for y in r]for x in r]
 return p(i,n-1)
