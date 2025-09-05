# mwi (281 (376 unzipped) vs 279 bytes for gold)
def p(i):
 for n in{*sum(i,[])}:
  k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x];k=[t:=[5]*len(k[0])]+k+[t]
  for a in range(10):
   for b in range(10):
    if a+len(k)<11>b+len(k[0])>0<all((y==0)==(t!=5)for x,s in zip(i[a:],k)for y,t in zip(x[b:],s)):
     i=[[y*(y!=n)for y in x]for x in i]
     for l in k:i[a][b:b+len(k[0])]=l;a+=1
 return i

### combined (283 (360 unzipped) bytes)
def p(i,r=range(10)):
 for n in{*sum(i,[])}:
  k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x];f=len(k[0]);k=[t:=[5]*f]+k+[t]
  for a in r:
   for b in r:
    if a+len(k)<11>b+f>0<all((y==0)==(t!=5)for x,s in zip(i[a:],k)for y,t in zip(x[b:],s)):
     i=[[y*(y!=n)for y in x]for x in i]
     for l in k:i[a][b:b+f]=l;a+=1
 return i
