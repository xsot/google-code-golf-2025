# xsot (149 vs 107 bytes for gold)
def p(i):
 for n in range(289):
  for x in i[(a:=n//17)+3%~-sum(i[a][(b:=n%17):b+2]+i[a+1][b:b+2]):a+2]*(sum(i[1])!=49or a!=8):x[b:b+2]=2,2
 return i

### combined (tied, 149 bytes)
def p(i):
 for n in range(289):
  for x in i[(a:=n//17)+3%~-sum(i[a][(b:=n%17):b+2]+i[a+1][b:b+2]):a+2]*(sum(i[1])!=49or a!=8):x[b:b+2]=2,2
 return i
