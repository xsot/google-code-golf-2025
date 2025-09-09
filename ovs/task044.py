def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x]or i;k=[t:=[5]*len(k[0])]+k+[t]
    if a+len(k)<11*all((y<1)^(t==5)for i,k in zip(i[a:],k)for y,t in zip(i[b:],k))>b+len(k[0]):i=[[y*(y!=n)for y in x]for x in i];[5for r,r[b:b+len(k[0])]in zip(i[a:],k)]
 return i
