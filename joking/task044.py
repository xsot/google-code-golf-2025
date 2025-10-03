# zip fiddling
def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[i*(i==n)or 5for i,*a in zip(a,*i)if n in a]+[5]for a in i if n in a]or i;k=[t:=[5]*len(k[0])]+k+[t]
    if all(i+k in(10,n)for i,k in zip(i[a:]+i,k)for i,k in zip(i[b:]+i,k)):i=[[i*(i!=n)for i in i]for i in i];[5for i,i[b:b+len(k[0])]in zip(i[a:]+i,k)]
 return i