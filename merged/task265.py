# mwi (141 vs 104 bytes for gold)
def p(i):
 for n in range(289):
  if sum(i[a:=n//17][(b:=n%17):b+2]+i[a+1][b:b+2])<5<392!=a*sum(i[1]):i[a][b:b+2]=i[a+1][b:b+2]=2,2
 return i

## 142 bytes, no if
def p(i):
 for n in range(289):b=n%17;k=i[a:=n//17];j=i[a+1];e=(sum(k[b:b+2]+j[b:b+2])<5<392!=a*sum(i[1]))*2;k[b:b+e]=j[b:b+e]=[2]*e
 return i

### xsot (149 bytes)
def p(i):
 for n in range(289):
  for x in i[(a:=n//17)+3%~-sum(i[a][(b:=n%17):b+2]+i[a+1][b:b+2]):a+2]*(sum(i[1])!=49or a!=8):x[b:b+2]=2,2
 return i

### combined (149 bytes)
def p(i):
 for n in range(289):
  for x in i[(a:=n//17)+3%~-sum(i[a][(b:=n%17):b+2]+i[a+1][b:b+2]):a+2]*(sum(i[1])!=49or a!=8):x[b:b+2]=2,2
 return i
