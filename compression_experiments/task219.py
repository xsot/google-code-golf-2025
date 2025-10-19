def p(i):
 t=r=f=0
 while i[f:]:
  if i[f]>i[0]:t=t or f;r=r or i[f:].index(i[0]);i[f-1:f+r]=[n for o in(0,-1,1,2)for d in(t-1,t)if 7not in sum(n:=[[i%7-2%~e for e,i in zip(e,i[:o%4%3]+i[o<0:]+[0])]for e,i in zip(i[f-1:f+r],i[d:])],[])][0];f+=r
  f+=1
 return i