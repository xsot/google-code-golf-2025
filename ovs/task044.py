def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x]or i;k=[t:=[5]*len(k[0])]+k+[t]
    if all(i+k in(10,n)for i,k in zip(i[a:]+i,k)for i,k in zip(i[b:]+i,k)):i=[[y*(y!=n)for y in x]for x in i];[5for r,r[b:b+len(k[0])]in zip(i[a:],k)]
 return i


## 278/309

def p(i,q=999):
 b=q//100;a=q//10%10;n=q%10;k=[[5,*[[5,y][y==n]for y,*s in zip(x,*i)if n in s],5]for x in i if n in x]or i;F=len(k[0]);k=[t:=[5]*F,*k,t]
 if all({*zip(i[b:]+i,k)}<={(0,n),(5,5)}for i,k in zip(i[a:]+i,k)):i=eval(str(i).replace(*f'{n}0'));[5for r,r[b:b+F]in zip(i[a:],k)]
 return-q*i or p(i,q-1)
