# combined (74 vs 67 bytes for gold)
p=lambda g:(t:=[a+b for*b,a in zip(*g[::-1],g)])+[e[::-1]for e in t[::-1]]

### xsot (92 bytes)
def p(M,m=[[0]*6]*6):
 for i in[0,1,2]*9:m[i][:3]=M[i];*m,=map(list,zip(*m[::-1]))
 return m
