def p(o):
 e=n=i=0
 while o[i:]:
  if o[i]>o[0]:e=e or i;n=n or o[i:].index(o[0]);o[i-1:i+n]=[f for r in(0,-1,1,2)for t in(e-1,e)if 7not in sum(f:=[[o%7-2%~h for h,o in zip(h,o[:r%4%3]+o[r<0:]+[0])]for h,o in zip(o[i-1:i+n],o[t:])],[])][0];i+=n
  i+=1
 return o