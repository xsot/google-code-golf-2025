# ovs (244 (348 unzipped) vs 239 bytes for gold)
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

### mwi (280 (376 unzipped) bytes)
def p(i):
 for n in{*sum(i,[])}:
  k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x];k=[t:=[5]*len(k[0])]+k+[t]
  for a in range(10):
   for b in range(10):
    if a+len(k)<11>b+len(k[0])>0<all((y==0)==(t!=5)for x,s in zip(i[a:],k)for y,t in zip(x[b:],s)):
     i=[[y*(y!=n)for y in x]for x in i]
     for l in k:i[a][b:b+len(k[0])]=l;a+=1
 return i

### combined (282 (360 unzipped) bytes)
def p(i,r=range(10)):
 for n in{*sum(i,[])}:
  k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x];f=len(k[0]);k=[t:=[5]*f]+k+[t]
  for a in r:
   for b in r:
    if a+len(k)<11>b+f>0<all((y==0)==(t!=5)for x,s in zip(i[a:],k)for y,t in zip(x[b:],s)):
     i=[[y*(y!=n)for y in x]for x in i]
     for l in k:i[a][b:b+f]=l;a+=1
 return i
