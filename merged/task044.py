# ovs (222 (461 unzipped) vs 195 bytes for gold)
def p(i):f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(512<<J for J in range(100)if f[J]==c))in bin(w<<100)for J in i][::-1];f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(512<<J for J in range(100)if f[J]==c))in bin(w<<100)for J in i][::-1];return i

## 226/250
def p(i):
 for J in 0,0:f=sum(i,[]);w=sum((f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]})<<J+1for J in range(50));i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum((f[J]==c)<<J+9for J in range(100)))in bin(w<<99)for J in i][::-1]
 return i

## 230/254
def p(i):
 for I in-1,-1:f=sum(i,[]);w={J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]}};i=[[J^c*(w>{I:=I+1}or J==c)for J in J]for c in{*f}if{J-min(w)+f.index(c)for J in w}=={J for J in range(100)if f[J]==c}for J in i][::-1]
 return i

### joking (232 (361 unzipped) bytes)
# zip fiddling
def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[i*(i==n)or 5for i,*a in zip(a,*i)if n in a]+[5]for a in i if n in a]or i;k=[[5]*len(k[0])]+k+[[5]*len(k[0])]
    if all(i+k in(10,n)for i,k in zip(i[a:]+i,k)for i,k in zip(i[b:]+i,k)):i=[[i-i*(i==n)for i in i]for i in i];[5for i,i[b:b+len(k[0])]in zip(i[a:]+i,k)]
 return i


##
def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[i*(i==n)or 5for i,*a in zip(a,*i)if n in a]+[5]for a in i if n in a]or i;k=[[5]*len(k[0])]+k+[[5]*len(k[0])]
    if all(i+k in(#['10,n','n,10']##)for i,k in zip(i[a:]+i,k)for i,k in zip(i[b:]+i,k)):i=[[#['i*(i!=n)','i-i*(i==n)']##for i in i]for i in i];[#[*range(10)]##for i,i[b:b+len(k[0])]in zip(i[a:]+i,k)]
 return i

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
