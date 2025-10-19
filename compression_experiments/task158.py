def p(r):
 x,i=max((len({*str(o:=[x[l:l+3]for x in r[x:x+3]])}),o)for x in range(len(r))for l in range(len(r[-1])))
 for o in range(len(r[-1])):
  for x in range(len(r)-o*3):
   for l in range(len(r[-1])-o*3):
    for a in range(len(r[-1])):
     for a in range(o*3*all(r[x+a][l+n]==i[a//o][n//o]or r[x+a][l+n]==r[-1][-1]!=i[a//o][n//o]==max({*i[1]}-{r[-1][-1]})for a in range(o*3)for n in range(o*3))):
      for n in range(o*3):r[x+a][l+n]=i[a//o][n//o]
     i=*zip(*i[::-1]),
 return r