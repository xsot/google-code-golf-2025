def p(M,m=[[0]*6]*6):
 for i in[0,1,2]*9:m[i][:3]=M[i];*m,=map(list,zip(*m[::-1]))
 return m