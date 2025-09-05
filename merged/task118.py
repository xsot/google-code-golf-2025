# ovs (314 (415 unzipped) vs 282 bytes for gold)
def p(g,F=0):
 for W in 3,3,2:
  for i in range(h:=len(g)):
   for j in range(w:=len(g[0])):
    X=[(i+k*d,j+k*D)for k in range(W+1)for d,D in((0,1),(0,-1),(1,0),(-1,0))];V=[not h>I>-1<J<w or g[I][J]for I,J in X];N=sum([r[max(0,j+~W):j+W+2]for r in g[max(0,i+~W):i+W+2]],[])
    for I,J in{*X*all(V)*(2in V[W%2*-4:]or F)*(V[3:].count(2)==N.count(2)>1<8>max(N))}:
     if h>I>-1<J<w:F=g[I][J]=2+g[I][J]%2*6
 return g

### mwi (329 (420 unzipped) bytes)
def p(i,n=2):
 s=*range(-n,0),*range(1,n+1);z=*zip(s,z:=[0]*9),*zip(z,[*s,0]);f=eval(str(i))
 for x in range(30):
  for y in range(len(i[0])):
   for a,b in zip((min(t:=[1-(len(i[0])>y+b>-1<x+a<len(i))or i[x+a][y+b]for a,b in z])*(n+1<t.count(2)//3*~t[:n*2].count(2)*~t[n*2:-1].count(2)or n==t[0]==t[3]or n>2==t[6]==t[8]))*z,t):f[x+1%b*a[0]][y+1%b*a[1]]=~b&9
 return"2"in str(f)and p(i,n+1)or eval(str(f).replace(*"92"))

### combined (331 (412 unzipped) bytes)
def p(i,n=2,R=range):
 s=*R(-n,0),*R(1,n+1);z=*zip(s,z:=[0]*9),*zip(z,[*s,0]);f=eval(str(i))
 for x in R(30):
  for y in R(len(i[0])):
   for a,b in zip((min(t:=[1-(len(i[0])>y+b>-1<x+a<len(i))or i[x+a][y+b]for a,b in z])*(n+1<t.count(2)//3*~t[:n*2].count(2)*~t[n*2:-1].count(2)or n==t[0]==t[3]or n>2==t[6]==t[8]))*z,t):f[x+1%b*a[0]][y+1%b*a[1]]=~b&9
 return"2"in str(f)and p(i,n+1)or eval(str(f).replace(*"92"))
