# task 1: 61 bytes, gold, https://arcprize.org/play?task=007bbfb7
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]
# task 2: 93 vs 90 bytes for gold, https://arcprize.org/play?task=00d62c1b
p=lambda a,n=-62:[*map(lambda*b,d=0:[(d:=c%(d+4)+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]
# task 3: 60 vs 58 bytes for gold, https://arcprize.org/play?task=017c7c7b
p=lambda g:[[v*2for v in l]for l in g+g[g[:2]!=g[4:]:][2:5]]
# task 4: 86 vs 80 bytes for gold, https://arcprize.org/play?task=025d127b
import re
p=lambda i:eval(re.sub(r"(([^0])(, .)+), 0(?=.*\2.*\].*\2)",r"0,\1",str(i)))
# task 5: 219 (290 unzipped) vs 206 bytes for gold, https://arcprize.org/play?task=045e512c
p=lambda g:(R:=max([{(i,j)for i in range(21)[I:I+3]for j in range(21)[J:J+3]if g[i][j]}for I in range(21)for J in range(21)],key=len),[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in(-4,0,4)for D in(-4,0,4)for k in range(21)[1:]for c in R)for x in range(21)]for y in range(21)])[1]
# task 6: 51 bytes, gold, https://arcprize.org/play?task=0520fde7
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
# task 7: 67 vs 65 bytes for gold, https://arcprize.org/play?task=05269061
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]
# task 8: 94 vs 89 bytes for gold, https://arcprize.org/play?task=05f2a901
p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]
# task 9: 127 vs 109 bytes for gold, https://arcprize.org/play?task=06df4c85
E=enumerate
p=lambda g:[[v or max(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]}|{0})for j,(v,*c)in E(zip(r,*g))]for i,r in E(g)]
# task 10: 72 vs 68 bytes for gold, https://arcprize.org/play?task=08ed6ac7
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]
# task 11: 125 vs 121 bytes for gold, https://arcprize.org/play?task=09629e4f
v=[[5]*11]*9
p=eval(f"lambda a:[a {'for*a,in map(zip,a,a,a,v,*[a[1:]]*3,v,*[a[2:]]*3)'*2}if(c:=sum(a,()).count)(5)<c(0)][0]")
# task 12: 133 vs 129 bytes for gold, https://arcprize.org/play?task=0962bcdd
import re;p=lambda i,k=7:-k*i or p(eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0,",r"\1\2\4\3,0,\2+",str([*zip(*i[::-1])]))),k-1)
# task 13: 169 vs 140 bytes for gold, https://arcprize.org/play?task=0a938d79
def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]
# task 14: 76 vs 70 bytes for gold, https://arcprize.org/play?task=0b148d64
p=lambda i:[[y[0]for y in zip(x,*i)if len({*y})>2]for x in i if len({*x})>2]
# task 15: 107 vs 98 bytes for gold, https://arcprize.org/play?task=0ca9ddb6
p=lambda i,k=3,r=range(9):-k*i or p([[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7for b in r]for a in r],k-1)
# task 16: 46 vs 43 bytes for gold, https://arcprize.org/play?task=0d3d703e
p=lambda m:[[b'AA	'[i]for i in m[0]]]*3
# task 17: 120 vs 109 bytes for gold, https://arcprize.org/play?task=0dfd9992
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
# task 18: 323 (390 unzipped) bytes, gold, https://arcprize.org/play?task=0e206a2e
def p(g):
 def p(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[p((x-j-a//4*(x-j).real*2)*1j**a+O,G[x])==p(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((A-j-a//4*(A-j).real*2)*1j**a+O)}for A in s)for x in s]
 return g
# task 19: 126 vs 119 bytes for gold, https://arcprize.org/play?task=10fcaaa3
E=enumerate
p=lambda g:[[v or 8*any([*[*g*2,[0]*9][y+d%5-1]*2,0][x+d%3-1]for d in b'-/29')for x,v in E(l*2)]for y,l in E(g*2)]
# task 20: 173 vs 157 bytes for gold, https://arcprize.org/play?task=11852cab
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]
# task 21: 62 vs 57 bytes for gold, https://arcprize.org/play?task=1190e5a7
p=lambda i,*n:[x for x in zip(*n or p(i,*i))if i!=(i:=x)][::2]
# task 22: 98 vs 91 bytes for gold, https://arcprize.org/play?task=137eaa0f
p=lambda i:[[*map(max,*[s[t:t+3]for t in range(144)if(s:=sum(i*2,i))[t+x]==5])]for x in[12,1,-10]]
# task 23: 216 vs 203 bytes for gold, https://arcprize.org/play?task=150deff5
import re
p=lambda i:i*("5"not in(s:=str(i)))or max([p(eval(r))for l in[("5, 5, 5","2,2,2"),(f"5(.{ {len(i[0])*3}}.)?"*3,r"2\1 2\2 2\3"),(f"5, 5(.{ {len(i[0])*3-2}})5, 5",r"8,8\1 8,8")]if(r:=re.sub(*l,s,1))!=s]+[[]])
# task 24: 62 bytes, gold, https://arcprize.org/play?task=178fcbfb
p=lambda i:[[3%-~sum(x)or(2in y)*2for y in zip(*i)]for x in i]
# task 25: 153 vs 132 bytes for gold, https://arcprize.org/play?task=1a07d186
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)
# task 26: 52 bytes, gold, https://arcprize.org/play?task=1b2d62fb
p=lambda a:[[8>>i+b.pop(0)for i in b[4:]]for b in a]
# task 27: 104 vs 103 bytes for gold, https://arcprize.org/play?task=1b60fb0c
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]
# task 28: 70 vs 63 bytes for gold, https://arcprize.org/play?task=1bfc4729
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']
# task 29: 118 vs 115 bytes for gold, https://arcprize.org/play?task=1c786137
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]
# task 30: 97 bytes, gold, https://arcprize.org/play?task=1caeab9d
p=lambda i:[[c*x[(H:=h.index)(1)-(j:=j-1)-H(c)]for c in h]for x in i if(h:=[*map(max,*i)],j:=11)]
# task 31: 45 bytes, gold, https://arcprize.org/play?task=1cf80156
p=lambda a,*n:[*filter(any,zip(*n or p(*a)))]
# task 32: 39 bytes, gold, https://arcprize.org/play?task=1e0a9b12
p=lambda a:[*zip(*map(sorted,zip(*a)))]
# task 33: 77 bytes, gold, https://arcprize.org/play?task=1e32b0e9
p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]
# task 34: 178 vs 146 bytes for gold, https://arcprize.org/play?task=1f0c79e5
p=lambda i,k=27:-k*i or p([[(u==2>1>s+t)*2or(s*t*y>1or 2in[s,t]*u)*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0,*x],f,[0,*f])]for*x,f in zip(*i,[[0]*9,*zip(*i)])][::-1],k-1)
# task 35: 87 vs 86 bytes for gold, https://arcprize.org/play?task=1f642eb9
p=lambda i,k=3:-k*i or[[x[0**k<=(k:=y)^8]or y for y in x]for x in zip(*p(i,k-1)[::-1])]
# task 36: 98 vs 90 bytes for gold, https://arcprize.org/play?task=1f85a75f
p=lambda i:max(l for n in range(10)if len(l:=(f:=lambda g:[x for x in zip(*g)if n in x])(f(i)))<6)
# task 37: 109 vs 107 bytes for gold, https://arcprize.org/play?task=1f876c06
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]
# task 38: 51 bytes, gold, https://arcprize.org/play?task=1fad071e
p=lambda g:[(str(g).count('1, 1')*[1]+[0]*9)[:9:2]]
# task 39: 65 vs 60 bytes for gold, https://arcprize.org/play?task=2013d3e2
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]
# task 40: 71 vs 69 bytes for gold, https://arcprize.org/play?task=2204b7a8
p=lambda i,c=9:[[(y>0)*i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]
# task 41: 49 bytes, gold, https://arcprize.org/play?task=22168020
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]
# task 42: 169 vs 148 bytes for gold, https://arcprize.org/play?task=22233c11
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]
# task 43: 57 bytes, gold, https://arcprize.org/play?task=2281f1f4
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]
# task 44: 281 (376 unzipped) bytes, gold, https://arcprize.org/play?task=228f6490
def p(i):
 for n in{*sum(i,[])}:
  k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x];k=[t:=[5]*len(k[0])]+k+[t]
  for a in range(10):
   for b in range(10):
    if a+len(k)<11>b+len(k[0])>0<all((y==0)==(t!=5)for x,s in zip(i[a:],k)for y,t in zip(x[b:],s)):
     i=[[y*(y!=n)for y in x]for x in i]
     for l in k:i[a][b:b+len(k[0])]=l;a+=1
 return i
# task 45: 45 bytes, gold, https://arcprize.org/play?task=22eb0ac0
p=lambda g:[10*r[:r[0]==r[9]]or r for r in g]
# task 46: 176 bytes, gold, https://arcprize.org/play?task=234bbc79
p=lambda i,n=0:[*zip(*[[y and max({*p,*x,*q}-{5})for y in x[n%3:]+x[:n%3]]for*x,p,q in zip(*i,[[],*zip(*i)],[*zip(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]
# task 47: 55 bytes, gold, https://arcprize.org/play?task=23581191
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
# task 48: 120 vs 92 bytes for gold, https://arcprize.org/play?task=239be575
p=lambda m,i=99,s="":-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+s,"1"+s,1)))][::-1],i-1,", 1")
# task 49: 87 vs 81 bytes for gold, https://arcprize.org/play?task=23b5c85d
p=lambda a:[b.count(e)*[e]for b in a if(e:=min(set(d:=sum(a,[]))-{0},key=d.count))in b]
# task 50: 96 vs 86 bytes for gold, https://arcprize.org/play?task=253bf280
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]
# task 51: 126 vs 115 bytes for gold, https://arcprize.org/play?task=25d487eb
p=lambda i,k=3:-k*i or[(l:=0)or[y+0*(l:=l|(1>a<y!=b)*b)or l for a,b,y in zip([0,1,*x],[0,*x],x)]for x in zip(*p(i,k-1))][::-1]
# task 52: 41 vs 40 bytes for gold, https://arcprize.org/play?task=25d8a9c8
p=lambda a:[3*[1//len({*b})*5]for b in a]
# task 53: 21 bytes, gold, https://arcprize.org/play?task=25ff71a9
p=lambda a:(a+a)[2:5]
# task 54: 308 (377 unzipped) bytes, gold, https://arcprize.org/play?task=264363fd
def p(g):
 f=sum(g,[]);*C,_,B=sorted({*f},key=f.count);M={(i,j):v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={(i,j)for i,j in M for I,J in M if(I-i)**2+(J-j)**2==1}
 for i,j in{*M}-T:
  for I,J in T:
   y,x=zip(*T);d=I-sum(y)//len(y);D=J-sum(x)//len(x);g[I][J]=B;F=1;u=d+i;U=D+j
   while(g[u][U]^B)*F:g[u][U]=M[I,J];u+=int(d/2);U+=int(D/2);F-=-2<d|D<2
 return g
# task 55: 100 vs 84 bytes for gold, https://arcprize.org/play?task=272f95fa
p=lambda i,z=0:[[z:=z+1-((c:=0)in x)]and[-c+(c:=c+y)or b"020463010"[z*3+c%7]%8for y in x]for x in i]
# task 56: 40 bytes, gold, https://arcprize.org/play?task=27a28665
p=lambda i:[[0**i[0][0]+0**i[0][2]*3^2]]
# task 57: 49 bytes, gold, https://arcprize.org/play?task=28bf18c6
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]
# task 58: 127 vs 103 bytes for gold, https://arcprize.org/play?task=28e73c20
p=lambda i,k=42:[[y+(len(x)-k>=0==y+s<=a==k//4*2)*3for y,s in zip(x,[0,*x])]for a,x in enumerate(zip(*-k*i or p(i,k-1)))][::-1]
# task 59: 191 vs 156 bytes for gold, https://arcprize.org/play?task=29623171
def p(g):f=sum(g,[]);C=[sum(R[i%11&~3:][:4].count(0)for R in g[i//11&~3:][:4])for i in range(121)];return[[v*(v==5)or(C[i]==min(C))*max({*f}-{5})for i,v in r]for r in zip(*[enumerate(f)]*11)]
# task 60: 48 bytes, gold, https://arcprize.org/play?task=29c11459
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]
# task 61: 63 bytes, gold, https://arcprize.org/play?task=29ec7d0e
p=lambda i,r=range(18):[[y*x%max(i[~0])+1for y in r]for x in r]
# task 62: 143 bytes, gold, https://arcprize.org/play?task=2bcee788
p=lambda i:{*i[s:=str(i).index(", 2")//31]+i[s+1]}-{2,3}and[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]or i[:s]+(i*2)[9+s::-1]
# task 63: 78 vs 77 bytes for gold, https://arcprize.org/play?task=2bee17df
p=lambda g:[[v or 3-3*any(min(c,r[1:-1]))for _,*c,_,v in zip(*g,r)]for r in g]
# task 64: 152 bytes, gold, https://arcprize.org/play?task=2c608aff
p=lambda a,n=-3:n*a or[[d:=[e:=b.pop(),d][g[2]!=d>0<e!=g[1]in b]for _ in[*b]]for*b,in zip(*p(a,n+1))if[d:=0,g:=sorted(set(c:=sum(a,a[5])),key=c.count)]]
# task 65: 104 vs 101 bytes for gold, https://arcprize.org/play?task=2dc579da
p=lambda i:[p:=len(i)//2+1]and[[min(y,key=y.count)for y in zip(x,t,x[p:],t[p:])]for x,t in zip(i,i[p:])]
# task 66: 289 (327 unzipped) bytes, gold, https://arcprize.org/play?task=2dd70a9a
def p(g):
 M={A*1j+B:D for A,C in enumerate(g)for B,D in enumerate(C)};A,C=[y for y in M if M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
 for*V,y,A,C,G in S:
  if(y in M)*16>G|C+13>1>(M[y]==2!=exec("for y in V:g[int(y.imag)][int(y.real)]=3")):F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for D in[A][F:]or[A*1j,A/1j]*G]
 return g
# task 67: 33 bytes, gold, https://arcprize.org/play?task=2dee498d
p=lambda a:[b[:len(a)]for b in a]
# task 68: 119 vs 116 bytes for gold, https://arcprize.org/play?task=31aa019c
s='for*a,in map(zip,[s]+a,a,a,a[1:]+[s])]'
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+s*2)
# task 69: 209 vs 153 bytes for gold, https://arcprize.org/play?task=321b1fc6
def p(a,i=-1):
 for i in(I:={i//10+i:v*(v!=8)for v in sum(a,[])if[i:=i+1]*v}):s={i};[s.add(y)for y in[*I]*6if{y,y+1,y-1,y+11,y-11}&s];a[i//11][i%11]=I[[s for s in I if I[s]][sorted(s).index(i)]]-I[i]
 return a
# task 70: 82 vs 78 bytes for gold, https://arcprize.org/play?task=32597951
p=lambda i:[[(c[0]+7in{*x}&{*c,hash(c)%1070})*2+c[0]for c in zip(x,*i)]for x in i]
# task 71: 195 vs 119 bytes for gold, https://arcprize.org/play?task=3345333e
def p(g,k=0):C=[*{}.fromkeys(sum(g,[]))][1];e=[[C*(c and C in((r+[0]*99)[k-k%2*2-x],c))for x,c in enumerate(r)]for r in g];return e*all(z[k//2-5:k//2]==z[k//2+1-k%2:][4::-1]for z in e)or p(g,k+1)
# task 72: 61 vs 54 bytes for gold, https://arcprize.org/play?task=3428a4f5
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]
# task 73: 46 bytes, gold, https://arcprize.org/play?task=3618c87e
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]
# task 74: 81 vs 79 bytes for gold, https://arcprize.org/play?task=3631a71a
p=lambda i,k=2:-k*i or p([[*map(min,a,[9,9]+a[::-1],c)]for*c,a in zip(*i,i)],k-1)
# task 75: 88 vs 86 bytes for gold, https://arcprize.org/play?task=363442ee
p=lambda i,r=range(9):[i[a][:4]+[i[a//3*3+1][b//3*3+5]*i[a%3][b%3]for b in r]for a in r]
# task 76: 303 (355 unzipped) bytes, gold, https://arcprize.org/play?task=36d67576
E=enumerate
def p(g):
 G={j+i*1j:v^2for i,r in E(g)for j,v in E(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a in range(8):
  for I in G:P=min(J:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=J.get)-I;g=g*any(13%-~J[y]^G.get(y-P,1)for y in J)or[[J.get(i*1j+j+P,v^2)^2for j,v in E(r)]for i,r in E(g)]
 return g
# task 77: 152 vs 126 bytes for gold, https://arcprize.org/play?task=36fdfd69
p=lambda i,k=39:-k*i or p([[((c:=y.count)(2)+c(4)>=2!=y[0])*4or y[0]for y in zip(x,[0,*x],[*x[1:],0],t)]for*x,t in zip(*i,[[0]*99,*zip(*i)])][::-1],k-1)
# task 78: 61 vs 60 bytes for gold, https://arcprize.org/play?task=3906de3d
p=lambda i:[*zip(*[sorted(x,key=0 .__eq__)for x in zip(*i)])]
# task 79: 123 bytes, gold, https://arcprize.org/play?task=39a8645d
p=lambda i:max(t:=[h for a in range(144)if all(map(any,(h:=[x[a//12:][:3]for x in i[a%12:][:3]])+[*zip(*h)]))],key=t.count)
# task 80: 253 (272 unzipped) bytes, gold, https://arcprize.org/play?task=39e1d7f9
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]
# task 81: 95 bytes, gold, https://arcprize.org/play?task=3aa6fb7a
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]
# task 82: 50 bytes, gold, https://arcprize.org/play?task=3ac3eb23
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3
# task 83: 40 bytes, gold, https://arcprize.org/play?task=3af2c5a8
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 84: 64 vs 62 bytes for gold, https://arcprize.org/play?task=3bd67248
def p(i,x=1):i[-1][x]=4;i[~x][x]=2;return i[:~x]and p(i,x+1)or i
# task 85: 56 vs 50 bytes for gold, https://arcprize.org/play?task=3bdb4ada
p=lambda i:[i:=[f:=y*(x!=i or f<y)for y in x]for x in i]
# task 86: 251 vs 192 bytes for gold, https://arcprize.org/play?task=3befdf3e
import re
p=lambda i,k=3:-k*[[(y!=0)*max({*(g:=sum(i,i[0]))}-{y or min(g,key=g.count),''})for y in x]for x in i]or p(eval(re.sub(r"(([1-9]), ((?!\2)(\d), (\4, \2, 0|\2)|\2, \2(, \2, 0)?), (0|''))",f"*[x or''for x in[\\1]]",str([*zip(*i[::-1])]))),k-1)
# task 87: 36 bytes, gold, https://arcprize.org/play?task=3c9b0459
p=lambda a:[b[::-1]for b in a[::-1]]
# task 88: 109 vs 101 bytes for gold, https://arcprize.org/play?task=3de23699
p=lambda a,n=-3:n*a[1:-1]or p([a[1:],[[d and(b:=max(a[n%2]))for d in c]for c in zip(*a[:0:-1])]][e:=b>0],n+e)
# task 89: 259 (284 unzipped) bytes, gold, https://arcprize.org/play?task=3e980e27
L=lambda i,j,s:any(0<(i-I)**2+(j-J)**2<3for I,J in s)
def p(g):
 for i,j in(M:={(A,x):F for A,r in enumerate(g)for x,F in enumerate(r)if F}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i,j]==M[I]!=L(i,j,M)<L(*y,s):s|={y};g[y[0]-I[0]+i][(I[1]-y[1])*(-1)**M[I]+j]=M[y]
 return g
# task 90: 197 vs 159 bytes for gold, https://arcprize.org/play?task=3eda0437
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]
# task 91: 63 bytes, gold, https://arcprize.org/play?task=3f7978a0
p=lambda a,n=46:a*~n or p([*zip(*a[(5in a[n%2-2])-2::-1])],n-1)
# task 92: 99 vs 87 bytes for gold, https://arcprize.org/play?task=40853293
p=lambda i,*n:[[y or max({*x[b:],0}&{*x[:b],0})for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
# task 93: 105 vs 101 bytes for gold, https://arcprize.org/play?task=4093f84a
import re
p=lambda g,k=11:-k*g or p(eval(re.sub(r"[^50],([, 0]+)5",r"\1 5,5",str([*zip(*g[::-1])]))),k-1)
# task 94: 137 vs 122 bytes for gold, https://arcprize.org/play?task=41e4d17e
p=lambda i,k=1:-k*i or p([[(y>7>x.count(1)<3==sum([*zip(*i)][a-1:a+2],x).count(1)%5)*6or y for y in x]for a,x in enumerate(zip(*i))],k-1)
# task 95: 81 vs 77 bytes for gold, https://arcprize.org/play?task=4258a5f9
p=lambda i,k=3:-k*i or[*map(lambda*x,z=0:[z%4|(z:=y)for y in x],*p(i,k-1)[::-1])]
# task 96: 325 (373 unzipped) bytes, gold, https://arcprize.org/play?task=4290ef0e
def p(g,*S):
 for c in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i for i,v in enumerate(r)if v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for x in r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
 R=range(w:=max(S)[0]);return[[([C for W,G,C in S if G<(M:=sorted(abs(w//2-v)for v in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for j in R]for i in R]
# task 97: 115 vs 108 bytes for gold, https://arcprize.org/play?task=42a50994
p=lambda i,e=enumerate:[[y*(sum(sum([z[b-(b>0):b+2]for z in i[a-(a>0):a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
# task 98: 101 vs 88 bytes for gold, https://arcprize.org/play?task=4347f46a
E=enumerate
p=lambda g:[[v*(0in[*r[j-1:j+2],*[*zip(*g)][j][i-1:i+2]])for j,v in E(r)]for i,r in E(g)]
# task 99: 150 vs 131 bytes for gold, https://arcprize.org/play?task=444801d8
p=lambda i,k=19:-k*i or p([[-(y<e<0)or(y<0<1!=e!=-2)*e or y or-2*(e>1<k>14or-2==e)or-(k==19>1==e)for y,e in zip(x,[0,*x])]for x in zip(*i[::-1])],k-1)
# task 100: 88 bytes, gold, https://arcprize.org/play?task=445eab21
p=lambda a:[[max(range(1,10),key=[sum({*b}&{*c})for c in zip(*a)for b in a].count)]*2]*2
# task 101: 282 (338 unzipped) bytes, gold, https://arcprize.org/play?task=447fd412
def p(g):
 T=1,20;V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==C}for C in range(5)];[s.add(I)for I in[*M]*2for i in m|s if abs(I-i)in T]
 for i in M-s:
  A=min(len({*range(i-2*k,i+3*k,k)}&M)for k in T);N={i}-v and{i-A*(min(s)-max(s))}&M;v|=N
  for k in N and{i-A*(min(s)-I)for I in m}&V:g[k//20][k%20]=1
 return g
# task 102: 170 vs 150 bytes for gold, https://arcprize.org/play?task=44d8ac46
import re
p=lambda i,k=20:-k*i or p(eval(re.sub(f'({(h:=(5,)*-~(n:=k%5))}.{(s:={34-n*3})}(?={(r:=f"5, [^5]{ {n*3}}5.{s}")*n}{h})({r})*5)(, 0)+',"\\1"+",2"*n,str(i))),k-1)
# task 103: 29 bytes, gold, https://arcprize.org/play?task=44f52bb0
p=lambda a:[[a==a[::-1]or 7]]
# task 104: 92 vs 84 bytes for gold, https://arcprize.org/play?task=4522001f
p=lambda g,R=range(9):[[3*((7%~g[2][1]^A)%9//4==(7%~g[1][2]^B)%9//4<2)for B in R]for A in R]
# task 105: 154 vs 148 bytes for gold, https://arcprize.org/play?task=4612dd53
A=any
p=lambda g,k=-3:k*g or p([[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1],k+1)
# task 106: 75 vs 67 bytes for gold, https://arcprize.org/play?task=46442a0e
p=lambda i:(s:=[a+x for a,*x in zip(i,*i[::-1])])+[x[::-1]for x in s[::-1]]
# task 107: 176 vs 170 bytes for gold, https://arcprize.org/play?task=469497ad
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>>(x-y)%z|g[(t+s)%5::4].count(f)>>(x-~y)%z)&2for y in r]for x in r]
# task 108: 58 vs 56 bytes for gold, https://arcprize.org/play?task=46f33fce
p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)
# task 109: 91 vs 81 bytes for gold, https://arcprize.org/play?task=47c1f68c
p=lambda a:[*map(f:=lambda*b,i=len(a)//2:[c and b[i]for c in b[:i]+b[i-1::-1]],*map(f,*a))]
# task 110: 132 vs 109 bytes for gold, https://arcprize.org/play?task=484b58aa
p=lambda a,i=1:9<sum(b[i:]==b[:-i]for b in zip(*a))and[[c:=[*map(max,*a[j%i::i])],c[9:]+c[-9:]][0in c]for j in range(29)]or p(a,i+1)
# task 111: 61 vs 60 bytes for gold, https://arcprize.org/play?task=48d8fb45
p=lambda g:[(f:=sum(g,[]))[f.index(5)+d:][:3]for d in b'	']
# task 112: 112 vs 109 bytes for gold, https://arcprize.org/play?task=4938f0c2
p=lambda i,k=1:-k*i or p([[y or(x*2)[[*map(max,i)].index(3)*2-b+1]for b,y in enumerate(x)]for x in zip(*i)],k-1)
# task 113: 25 bytes, gold, https://arcprize.org/play?task=496994bd
p=lambda a:a[:5]+a[4::-1]
# task 114: 65 bytes, gold, https://arcprize.org/play?task=49d1d64f
p=lambda g:[[0,*g[0],0],*[r[:1]+r+r[-1:]for r in g],[0,*g[-1],0]]
# task 115: 54 bytes, gold, https://arcprize.org/play?task=4be741c5
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]
# task 116: 20 bytes, gold, https://arcprize.org/play?task=4c4377d9
p=lambda a:a[::-1]+a
# task 117: 172 vs 157 bytes for gold, https://arcprize.org/play?task=4c5c2cf0
p=lambda i,k=1:-k*i or p([[*map(max,x,[*x,*(s:=sum(i,[]))][s.index(max(s,key=lambda n:[x.count(n)for x in i if n in x]==[2,1,2]))//len(i)*2+2::-1]+s)]for x in zip(*i)],k-1)
# task 118: 314 (415 unzipped) bytes, gold, https://arcprize.org/play?task=50846271
def p(g,F=0):
 for W in 3,3,2:
  for i in range(h:=len(g)):
   for j in range(w:=len(g[0])):
    X=[(i+k*d,j+k*D)for k in range(W+1)for d,D in((0,1),(0,-1),(1,0),(-1,0))];V=[not h>I>-1<J<w or g[I][J]for I,J in X];N=sum([r[max(0,j+~W):j+W+2]for r in g[max(0,i+~W):i+W+2]],[])
    for I,J in{*X*all(V)*(2in V[W%2*-4:]or F)*(V[3:].count(2)==N.count(2)>1<8>max(N))}:
     if h>I>-1<J<w:F=g[I][J]=2+g[I][J]%2*6
 return g
# task 119: 127 vs 106 bytes for gold, https://arcprize.org/play?task=508bd3b6
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)
# task 120: 102 vs 98 bytes for gold, https://arcprize.org/play?task=50cb2852
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]
# task 121: 96 vs 90 bytes for gold, https://arcprize.org/play?task=5117e062
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)
# task 122: 94 vs 88 bytes for gold, https://arcprize.org/play?task=5168d44c
p=lambda i:sum(map(max,i))<8and[[x[0]%2*3,x[1]%2*3,*x[:-2]]for x in i]or[*zip(*p([*zip(*i)]))]
# task 123: 76 vs 75 bytes for gold, https://arcprize.org/play?task=539a4f51
R=range(10)
p=lambda g:[[g[0][max(i,j)%(5-0**g[0][4])]for j in R]for i in R]
# task 124: 129 vs 123 bytes for gold, https://arcprize.org/play?task=53b68214
p=lambda i,n=0,s=2:[([0]*n*k+x)[:10]for k in range(5)for x in(i[:s]==[x[n:]+n*[0]for x in i[s:s*2]])*i[:s]][:10]or p(i,n+s%2,s^1)
# task 125: 141 vs 126 bytes for gold, https://arcprize.org/play?task=543a7ed5
p=lambda i,k=15,r=range(15):-k*i or p([[(y:=i[~b][a])*(y&4>0)or(3<i[~b][a-1]&i[-b][a]<7)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)
# task 126: 57 vs 54 bytes for gold, https://arcprize.org/play?task=54d82841
p=lambda a:a[:-1]+[[4*(sum(c)<2*max(c))for c in zip(*a)]]
# task 127: 82 vs 65 bytes for gold, https://arcprize.org/play?task=54d9e175
p=lambda i,E=enumerate:[[5+(y<5)*i[a&12|1][b&12|1]for b,y in E(x)]for a,x in E(i)]
# task 128: 64 bytes, gold, https://arcprize.org/play?task=5521c0d9
p=lambda i:[*zip(*[x[(j:=-x.count(0)):]+x[:j]for x in zip(*i)])]
# task 129: 47 bytes, gold, https://arcprize.org/play?task=5582e5ca
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3
# task 130: 65 bytes, gold, https://arcprize.org/play?task=5614dbcf
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]
# task 131: 126 bytes, gold, https://arcprize.org/play?task=56dc2b01
p=lambda a,n=-3:n*a or p([[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))],n+1)
# task 132: 109 vs 86 bytes for gold, https://arcprize.org/play?task=56ff96f3
p=lambda i,k=3:-k*i or p([[max({*i[a]}&{*y}|{*y[:a+1]}&{*y[a:]})for a in range(len(i))]for y in zip(*i)],k-1)
# task 133: 298 (389 unzipped) bytes, gold, https://arcprize.org/play?task=57aa92db
def p(g):
 *C,M={i*90+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g},
 for A in M:
  G={A}
  for D in*C,:
   if{A-90,A-1}&D:C.remove(D);G|=D
  C+=G,
 for A in C:
  for D in A:
   for G in A:
    for I in 1//sum(M[k]==M[D]for k in A)*C:
     for Q in{G}^A:
      for V in(E:=[k for k in I if M[D]==M[k]==M[G]]):V+=(len(E)^6)%6*(Q-G);g[V//90][V%90],={*map(M.get,I)}-{M[D]}
 return g
# task 134: 209 vs 186 bytes for gold, https://arcprize.org/play?task=5ad4f10b
p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in str(x)!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)
# task 135: 32 bytes, gold, https://arcprize.org/play?task=5bd6f4ac
p=lambda a:[b[6:]for b in a[:3]]
# task 136: 113 vs 105 bytes for gold, https://arcprize.org/play?task=5c0a986e
import re
p=lambda m,S=re.sub:eval(eval('S("(?<=(2.{34}){2})0","2",S("0(?=(.{34}1){2})","1",'*9+f'"{m}"'+'))'*9))
# task 137: 143 bytes, gold, https://arcprize.org/play?task=5c2c9af4
def p(a):r=range(len(a));X,Y=[(x:=i,j)for i in r for j in r if a[i][j]][1];return[[a[X][Y]*(max(X-i,i-X,Y-j,j-Y)%(x-X)<1)for j in r]for i in r]
# task 138: 104 bytes, gold, https://arcprize.org/play?task=5daaa586
p=lambda a,n=35:-n*a or p([*map(lambda*b,d=0:[d:=c|d*(d==b[0]>n-3)for c in b[::-1]],*a[0in a[0]:])],n-1)
# task 139: 100 vs 94 bytes for gold, https://arcprize.org/play?task=60b61512
p=lambda i,k=11,r=range(9):-k*i or p([[i[~b][a]or i[-b][a]*i[~b][a-1]%3*7for b in r]for a in r],k-1)
# task 140: 36 bytes, gold, https://arcprize.org/play?task=6150a2bd
p=lambda a:[b[::-1]for b in a[::-1]]
# task 141: 106 vs 94 bytes for gold, https://arcprize.org/play?task=623ea044
p=lambda i,e=enumerate:[[max((k:=z+[0]*99)[t+b-a]|k[a+b-t]for t,z in e(i))for b,y in e(x)]for a,x in e(i)]
# task 142: 40 bytes, gold, https://arcprize.org/play?task=62c24649
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 143: 187 vs 158 bytes for gold, https://arcprize.org/play?task=63613498
p=lambda i,n=1:(s:=[[[y>0for*s,y in zip(*i,x)if n in s]for x in i if n in x]for n in range(10)]).count(s[n]or 1)>1<=n not in i[0][:3]+i[1][:3]and eval(str(i).replace(*f"{n}5"))or p(i,n+1)
# task 144: 59 vs 53 bytes for gold, https://arcprize.org/play?task=6430c8c4
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]
# task 145: 199 bytes, gold, https://arcprize.org/play?task=6455b5f5
p=lambda i,k=79,t=0:-k*i or p([[{*0**y*[t:=t+1]}if k>78else[y|(y and e),2*0**(h:=len(y))+(min(s:={*map(len,sum(i,[]))}-{0})==h)*8+h//max(s)][k<1]for y,e in zip(x,x[:1]+x)]for x in zip(*i[::-1])],k-1)
# task 146: 58 bytes, gold, https://arcprize.org/play?task=662c240a
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
# task 147: 87 vs 84 bytes for gold, https://arcprize.org/play?task=67385a82
p=lambda i,k=3:-k*i or[(s:=0)or[-y%~s%8+(s:=y)for y in x]for x in zip(*p(i,k-1))][::-1]
# task 148: 169 vs 141 bytes for gold, https://arcprize.org/play?task=673ef223
p=lambda i,l=[0],t=0:[[-y%12&6or(max(x[b:])*max(x[:b+1])>-l[0])*8for b,y in enumerate(x)]for x in i if(l:=l[(t:=t+(i[0]!=x[0])+(i[-1]!=(i:=x)[-1]))>4:]+[8in x]*(2in x))]
# task 149: 79 vs 75 bytes for gold, https://arcprize.org/play?task=6773b310
p=eval('lambda a:[[9<sum(sum(a,()))'+'for*a,in map(zip,a,a[1:],a[2:])][::4]'*2)
# task 150: 30 bytes, gold, https://arcprize.org/play?task=67a3c6ac
p=lambda g:[r[::-1]for r in g]
# task 151: 108 bytes, gold, https://arcprize.org/play?task=67a423a3
def p(g):
 x=y=0
 for _ in g:x+=1>g[0][x];y+=0in g[y]
 for N in b"":g[y+N//3-6][x+N%3-1]=4
 return g
# task 152: 40 bytes, gold, https://arcprize.org/play?task=67e8384a
p=lambda a:[r+r[::-1]for r in a+a[::-1]]
# task 153: 184 vs 141 bytes for gold, https://arcprize.org/play?task=681b3aeb
def p(g,R=range):u=[[(r*2)[x:x+3]for r in(g*2)[y:y+3]]for x in R(10)for y in R(10)];return[t for a in u for b in u if"0"not in str(t:=[[a[y][x]^b[y][x]for x in R(3)]for y in R(3)])][0]
# task 154: 133 vs 100 bytes for gold, https://arcprize.org/play?task=6855a6e4
p=lambda i,k=3:-k*i or p([[*[*zip(*i[::-1])][(1<abs(h:=(r:=[*map(max,*i)]).index(2)-l)<4==r.count(2))*2*h+l]]for l in range(15)],k-1)
# task 155: 18 bytes, gold, https://arcprize.org/play?task=68b16354
p=lambda a:a[::-1]
# task 156: 199 vs 152 bytes for gold, https://arcprize.org/play?task=694f12f3
p=lambda i,k=79,t=0:-k*i or p([[{*y*[t:=t+1]}if k>78else(y|(y-{0}and e-{0}or{0}))if k else sorted({*map(len,sum(i,[]))}).index(len(y))**2%12%7for y,e in zip(x,[{*()},*x])]for x in zip(*i[::-1])],k-1)
# task 157: 339 (409 unzipped) vs 291 bytes for gold, https://arcprize.org/play?task=6a1e5592
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   A in p or len(A)==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+len(A),p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*len(A)):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(b'\n'+A+b'\n')]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=b'\n'+bytes(K)+b'\n';S={*K.split(b'\n')};Q(0,{});return g
# task 158: 306 (471 unzipped) bytes, gold, https://arcprize.org/play?task=6aa20dc0
def p(g):
 o=g[0][-1];s,t=max((len({*sum(a:=[R[x:x+3]for R in g[y:y+3]],[])}),a)for y in range(len(g))for x in range(len(g[0])))
 for s in(1,2,3):
  for y in range(len(g)+1-3*s):
   for x in range(len(g[0])+1-3*s):
    for z in'range'*2:
     t=(t,[*zip(*t)])[z<'r'][::-1]
     for Y in range(s*3*all((a:=g[y+Y][x+X])==(b:=t[Y//s][X//s])or(a==o)*(b==max({*t[1]}-{o}))for Y in range(s*3) for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g
# task 159: 185 vs 139 bytes for gold, https://arcprize.org/play?task=6b9890af
def p(i,e=enumerate):l,m=[[[y[0]for y in zip(x,*i)if{*y}&n]for x in i if{*x}&n]for n in[{2},{1,*range(3,10)}]];s=len(l)//3;return[[y or m[~-a//s][~-b//s]for b,y in e(x)]for a,x in e(l)]
# task 160: 115 bytes, gold, https://arcprize.org/play?task=6c434453
import re;p=lambda i,*n:eval(re.sub("1, 1, 1(.{26}), 0, 1(.{26}), 1,",r"0,2,0\1*2,2,2\2*0,2,0*",str(n or p(i,*i))))
# task 161: 105 vs 82 bytes for gold, https://arcprize.org/play?task=6cdd2623
p=lambda m:[[sum(({x}&{y}|{i}&{j})&{min(a:=sum(m,[]),key=a.count)})for i,*_,j in zip(*m)]for x,*_,y in m]
# task 162: 107 vs 96 bytes for gold, https://arcprize.org/play?task=6cf79266
import re;p=lambda i,k=2:-k*i or p(eval(re.sub("0, 0, 0(.{55})?"*3,r"1,1,1\1 1,1,1\2 1,1,1\3",str(i))),k-1)
# task 163: 136 bytes, gold, https://arcprize.org/play?task=6d0160f0
R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]
# task 164: 32 bytes, gold, https://arcprize.org/play?task=6d0aefbc
p=lambda a:[b+b[::-1]for b in a]
# task 165: 169 vs 136 bytes for gold, https://arcprize.org/play?task=6d58a25d
def p(i):s,b=sorted({*sum(i,[])}-{0},key=lambda n:(f"{n}, "*3in str(i))*-n^7);return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]
# task 166: 65 vs 61 bytes for gold, https://arcprize.org/play?task=6d75e8bb
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]
# task 167: 85 vs 72 bytes for gold, https://arcprize.org/play?task=6e02f1e3
p=lambda i:[b:=[[0,0,5],[0,5,0],[5,0,0]],b[::-1],[[5]*3]+[[0]*3]*2][4-len({*str(i)})]
# task 168: 117 vs 115 bytes for gold, https://arcprize.org/play?task=6e19193c
import re
p=lambda i,k=39:-k*i or[*zip(*eval(re.sub(r"0((.{35})+, ([^0]).{28}\3, \3)",r"\3\1",str(p(i,k-1))))[::-1])]
# task 169: 134 vs 129 bytes for gold, https://arcprize.org/play?task=6e82a1ae
p=lambda i,k=39,t=0:-k*i or[[[y and y|e,-len(y)%5][k>38]if k else{*[t:=t+1]*y}for y,e in zip(x,x[:1]+x)]for x in zip(*p(i,k-1)[::-1])]
# task 170: 238 (270 unzipped) vs 211 bytes for gold, https://arcprize.org/play?task=6ecd11f4
def p(g):e=enumerate;I,J=max(t:=[(y,x)for y,r in e(g)for x,c in e(r)if c]);s=3-0**g[I][J-3];x=min(x for y,x in t if y<I-s or x<J-s);y,*_,Y=[y for y,x in t if y<I-s or x<J-s];v=(Y+1-y)//(s+1);return[[g[y+v*n][x+v*m]and c for m,c in e(r[J-s:J+1])]for n,r in e(g[I-s:I+1])]
# task 171: 54 vs 52 bytes for gold, https://arcprize.org/play?task=6f8cd79b
p=lambda a:[*map(f:=lambda*b:[8,*b[2:],8],*map(f,*a))]
# task 172: 20 bytes, gold, https://arcprize.org/play?task=6fa7a44f
p=lambda a:a+a[::-1]
# task 173: 228 (271 unzipped) vs 222 bytes for gold, https://arcprize.org/play?task=72322fa7
def p(g):o=[(Y,x,y)for Y,a in enumerate(g)for x,a in enumerate(a)if(y:=[a for a in g[Y:Y+3]for a in a[x:x+3]])==y[::-1]>y[:8]>[0]*8];[0for Y,X,a in o for Y,X,A in o for y,g[Y+y//3][X+y%3]in enumerate(a*(len({*a})==3*len({a[y]for y,r in enumerate(A)if r-a[y]})))];return g
# task 174: 99 vs 97 bytes for gold, https://arcprize.org/play?task=72ca375d
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(f(k)==f(k)[::-1])or p(g,c+1)
# task 175: 75 bytes, gold, https://arcprize.org/play?task=73251a56
r=range(21);p=lambda g:[[g[A][B]|g[B][A]or g[0][B!=A]for B in r]for A in r]
# task 176: 74 vs 65 bytes for gold, https://arcprize.org/play?task=7447852a
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]
# task 177: 51 bytes, gold, https://arcprize.org/play?task=7468f01a
p=lambda a,*n:[*filter(any,zip(*n or p(*a)[::-1]))]
# task 178: 49 vs 47 bytes for gold, https://arcprize.org/play?task=746b3537
p=lambda a:a*-1*-1or[p(b)for b in a if a!=(a:=b)]
# task 179: 21 bytes, gold, https://arcprize.org/play?task=74dd1130
p=lambda a:[*zip(*a)]
# task 180: 81 vs 79 bytes for gold, https://arcprize.org/play?task=75b8110e
p=eval('lambda a:[[max(sum(a+a,())[1:],key=bool)'+'for*a,in map(zip,a,a[4:])]'*2)
# task 181: 67 bytes, gold, https://arcprize.org/play?task=760b3cac
def p(a):
	for b in a[:3]:c=6>>a[3][3];b[c:c+3]=b[5:2:-1]
	return a
# task 182: 187 vs 176 bytes for gold, https://arcprize.org/play?task=776ffc46
def p(g):
 R=F=sum(g,[])
 while C:=[*{*F}][-2]:
  o=F.index(C)-2;N={d for d in range(70)if d%20<6>F[d+o]==C}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g
# task 183: 94 bytes, gold, https://arcprize.org/play?task=77fdfe62
def p(g):A=len(g);B=range(2,A-2);return[[g[C][B]%7*g[0-C*2//A][0-B*2//A]for B in B]for C in B]
# task 184: 101 vs 100 bytes for gold, https://arcprize.org/play?task=780d0b14
p=lambda i,k=0,s=[0]*99:[s+0*(s:=[*x])for x in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
# task 185: 162 vs 143 bytes for gold, https://arcprize.org/play?task=7837ac64
p=lambda i:[[1//len(q:={*sum([[t[0]for t in zip(s,*i)if{*t,0}>h][y:y+2]for s in i if{*s,0}>(h:={*i[0]})][x:x+2],[])})*max(q-h|{0})for y in[0,1,2]]for x in[0,1,2]]
# task 186: 66 vs 60 bytes for gold, https://arcprize.org/play?task=794b24be
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
# task 187: 107 vs 97 bytes for gold, https://arcprize.org/play?task=7b6016b9
p=lambda i,k=79:-k*i or[[y*(y!=2)or(z==3)*3or y or 2for y,z in zip(x,[3,*x])]for x in zip(*p(i,k-1)[::-1])]
# task 188: 75 vs 61 bytes for gold, https://arcprize.org/play?task=7b7f7511
p=lambda a:[a[:len(a)//2],c:=[b[:len(b)//2]for b in a]][a==[b*2for b in c]]
# task 189: 111 bytes, gold, https://arcprize.org/play?task=7c008303
p=lambda i,r=range(6):[[i[a-6+(s:=i[6][0]%3)*3][b-6+(t:=i[0][6]%3)*3]/3*i[a//3-s][b//3-t]for b in r]for a in r]
# task 190: 112 vs 109 bytes for gold, https://arcprize.org/play?task=7ddcd7ec
import re;p=lambda i,k=19:-k*i or p(eval(re.sub("0(?=.{34}([^0]), 0.{31}\\1)","\\1",str([*zip(*i[::-1])]))),k-1)
# task 191: 255 (327 unzipped) vs 251 bytes for gold, https://arcprize.org/play?task=7df24a62
def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:g=E*g[::-1]or[*map(list,zip(*g))];[0for C,H in B(g,-1)for D,I in B(g,-1)for F,H in B(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in B(A)for G,I in B(H)))for G,I in B(H)for g[C+F][D+G]in[I]*(-1<D+G<23>C+F>-1)]
 return g
# task 192: 120 vs 111 bytes for gold, https://arcprize.org/play?task=7e0986d6
b,=c,=z=['for*d,c,b,a in zip(b,c,z+a,a[1:]+z,a)]']
p=lambda a:eval('[[[sum({*d}&{b,c}),a][%s.count(a)>30]'%sum(a,a)+b*2)
# task 193: 98 vs 85 bytes for gold, https://arcprize.org/play?task=7f4411dc
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
# task 194: 74 vs 73 bytes for gold, https://arcprize.org/play?task=7fe24cdd
p=lambda g:(t:=[a+b for*b,a in zip(*g[::-1],g)])+[e[::-1]for e in t[::-1]]
# task 195: 105 bytes, gold, https://arcprize.org/play?task=80af3007
p=lambda a,n=-1:n*[[d&e for d in b for e in c]for b in a for c in a]or p([*filter(any,zip(*a[::3]))],n+1)
# task 196: 135 vs 112 bytes for gold, https://arcprize.org/play?task=810b9b61
p=lambda i,k=79:-k*i or p([[(k<32>y==1<s)*3or~-(k<32>y==4)*y*~-(s<1>y%2)or k//79*4for s,y in zip([0,*x],x)]for x in zip(*i[::-1])],k-1)
# task 197: 54 bytes, gold, https://arcprize.org/play?task=82819916
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]
# task 198: 122 bytes, gold, https://arcprize.org/play?task=83302e8f
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)
# task 199: 102 vs 85 bytes for gold, https://arcprize.org/play?task=834ec97d
p=lambda g,E=enumerate:[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B,_ in E(x)]for A,x in E(g)]
# task 200: 110 vs 84 bytes for gold, https://arcprize.org/play?task=8403a5d5
p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]
# task 201: 208 bytes, gold, https://arcprize.org/play?task=846bdb03
def p(g):j=D=0;P=[];exec("for r in g:V=r[j];F=V==4;P+=[V]*D;D^=F;r[j]*=D|F<1\nj+=1\n"*13+"g[:]=filter(any,zip(*g));"*2);A,*_,B=map(max,*g);E=4,*[0]*len(g[0]),4;return[E,*[[A,*r,B][::A==P[0]or-1]for r in g],E]
# task 202: 109 vs 105 bytes for gold, https://arcprize.org/play?task=855e0971
p=lambda a:(len({*a[0]}-{0})<2)*[[*map(min,*[c for c in a if max(b)in c])]for b in a]or[*zip(*p([*zip(*a)]))]
# task 203: 67 vs 64 bytes for gold, https://arcprize.org/play?task=85c4e7cd
p=lambda i:[[i[g:=len(i)//2][g+i[g].index(y)]for y in x]for x in i]
# task 204: 108 vs 93 bytes for gold, https://arcprize.org/play?task=868de0fa
import re;p=lambda i:eval(re.sub(r"(?<!1, )1, ((0, )+)1(?!, 1)",r"1,*[len([\1])%2*5+2]*len([\1]),1",str(i)))
# task 205: 225 (235 unzipped) vs 166 bytes for gold, https://arcprize.org/play?task=8731374e
p=lambda g:max([[min(w:=r+c,key=w.count)for*c,in zip(*S)]for r in S]for A in range(len(g.pop(0))-6)if(s:=lambda w:len({*sum([r[A:A+6]for r in g[:6]],w[:6])})<=2)for S in[[[v for v,*c in zip(r,*g)if s(c)]for r in g if s(r[A:])]])or p(g)
# task 206: 156 vs 144 bytes for gold, https://arcprize.org/play?task=88a10436
def p(g,E=enumerate):
 r,c=map(min,*[(a,b)for a,x in E(g)for b,y in E(x)if y%5or y>0==(s:=a,t:=b)])
 for i in-1,0,1:g[s+i][t-1:t+2]=g[r-~i][c:c+3]
 return g
# task 207: 81 bytes, gold, https://arcprize.org/play?task=88a62173
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[3:])]'*2)
# task 208: 225 (290 unzipped) bytes, gold, https://arcprize.org/play?task=890034e9
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E,D=len(A:=[A for A in zip(*A)if M in A]),len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[1+B:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g
# task 209: 292 (429 unzipped) bytes, gold, https://arcprize.org/play?task=8a004b2b
def p(g):
 G=g[-5:]
 for s in[()]*4:G=[x for x in zip(*G[::-1])if{*x}-{0,4}];g=[[*x]for x in zip(*g[::-1])if 4in(s:=s+x)]
 for s in[2,3,4]:
  for y in range(20):
   for x in range(20):
    if all(g[Y][X]in[0,4-4*(y<=Y<y+len(G)*s>0<x<=X<x+len(G[0])*s)or G[(Y-y)//s][(X-x)//s]]for Y in range(len(g))for X in range(len(g[0]))):
     for Y in range(len(G)*s):
      for X in range(len(G[0])*s):g[Y+y][X+x]=G[Y//s][X//s]
     return g
# task 210: 20 bytes, gold, https://arcprize.org/play?task=8be77c9e
p=lambda a:a+a[::-1]
# task 211: 48 bytes, gold, https://arcprize.org/play?task=8d5021e8
p=lambda g:[l[::-1]+l for l in(g[::-1]+g)*2][:9]
# task 212: 117 vs 107 bytes for gold, https://arcprize.org/play?task=8d510a79
p=lambda i,k=39:-k*i or[[x[b]or 5in x[:b]and 2-x[b-1]%5&1-x[b+(b<9)]for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
# task 213: 111 vs 92 bytes for gold, https://arcprize.org/play?task=8e1813be
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[k for k in i[0]if k]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
# task 214: 63 vs 62 bytes for gold, https://arcprize.org/play?task=8e5a5113
p=lambda a:[b[:4]+c[::-1]+a.pop()[3::-1]for*c,b in[*zip(*a,a)]]
# task 215: 45 vs 42 bytes for gold, https://arcprize.org/play?task=8eb1be9a
p=lambda g:([max(g[::3]),*g[4:6]]*9)[:len(g)]
# task 216: 125 vs 114 bytes for gold, https://arcprize.org/play?task=8efcae92
r=range(661)
p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]
# task 217: 95 bytes, gold, https://arcprize.org/play?task=8f2ea7aa
p=lambda a,*n:[*filter(any,zip(*[[d&e for d in b for e in c]for b in n for c in a]or p(a,*a)))]
# task 218: 56 bytes, gold, https://arcprize.org/play?task=90c28cc7
p=lambda a,*n:[*{b:0for b in zip(*n or p(*a))if any(b)}]
# task 219: 292 (307 unzipped) vs 269 bytes for gold, https://arcprize.org/play?task=90f3ed37
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)
# task 220: 113 vs 89 bytes for gold, https://arcprize.org/play?task=913fb3ed
p=lambda i,e=enumerate:[[y or max(max(s[b-(b>0):b+2])for s in i[a-(a>0):a+2])*5%9for b,y in e(x)]for a,x in e(i)]
# task 221: 102 vs 87 bytes for gold, https://arcprize.org/play?task=91413438
def p(i):j=3*str(i).count("0");return[[(a//3*j+b<27-j)*i[a%3][b%3]for b in range(j)]for a in range(j)]
# task 222: 106 bytes, gold, https://arcprize.org/play?task=91714a58
p=lambda g,k=5:-k*g or p([[c*(2*f"{c}, "in str(r))*(sum(g,[]).count(c)>4)for c in r]for r in zip(*g)],k-1)
# task 223: 52 vs 51 bytes for gold, https://arcprize.org/play?task=9172f3a0
p=lambda a:eval("[[a "+"for a in a for _ in%s]"%a*2)
# task 224: 171 bytes, gold, https://arcprize.org/play?task=928ad970
p=lambda i,k=3,s=0:-k*i or p([[y or(s==5in{*(h:=[*map(max,i)])[b+1:]}&{*h[:b]})*sum({*sum(i,[])},-5)for b,y in enumerate(x)]*1**(s:=s*2+max(x))for x in zip(*i)][::-1],k-1)
# task 225: 132 bytes, gold, https://arcprize.org/play?task=93b581b8
p=lambda i,r=range(6):[[max([s for t in i[a-3:a]+i[a+3:a:-1]for s in t[b-3:b]+t[b+3:b:-1]if s][:-3]+[i[a][b]])for b in r]for a in r]
# task 226: 159 vs 142 bytes for gold, https://arcprize.org/play?task=941d9a10
p=lambda i,e=enumerate,s=sum:[[y or(s(x[:b])*2==s(x))*(s(k:=[*map(min,i)])==s(k[:a])*2)*2+0**s(x[b:]+k[a:])*3+0**s(x[:b]+k[:a])for b,y in e(x)]for a,x in e(i)]
# task 227: 57 vs 52 bytes for gold, https://arcprize.org/play?task=94f9d214
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(4)]for b in a]
# task 228: 189 vs 120 bytes for gold, https://arcprize.org/play?task=952a094c
f=lambda A:[i for i,r in enumerate(A)if any(r)]
def p(A):
 _,E,*_,k,_=f(A);W,*_,p=f(zip(*A))
 for l,a in[[W+1,p+1],[p-1,W-1]]:A[k+2][a]=A[E][l];A[E-2][a]=A[k][l];A[E][l]=A[k][l]=0
 return A
# task 229: 73 bytes, gold, https://arcprize.org/play?task=9565186b
p=lambda a:[[[5,c][c==max(d:=sum(a,a),key=d.count)]for c in b]for b in a]
# task 230: 125 vs 114 bytes for gold, https://arcprize.org/play?task=95990924
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=.{%d}0, 5.{%d}5)"%((len(m)*3+1,)*2),"3421"[i],str(p(m,i-1)[::-1]))))]
# task 231: 43 bytes, gold, https://arcprize.org/play?task=963e52fc
p=lambda a:[(r[:6]*4)[:len(r)*2]for r in a]
# task 232: 63 vs 58 bytes for gold, https://arcprize.org/play?task=97999447
p=lambda i:[[(0>(e:=y-e))*5or e for y in x]for x in i if[e:=0]]
# task 233: 307 (465 unzipped) bytes, gold, https://arcprize.org/play?task=97a05b5b
e=enumerate
def p(g):
 w=[(y,x,s)for y,p in e(g[:-2])for x,p in e(p[:-2])if{*sum(s:=[v[x:x+3]for v in g[y:y+3]],[])}^{0}>{2,0}]
 for y,x,s in w:
  for n,p in e(s):g[y+n][x:x+3]=0,0,0,
 u=[[y[0]for y in zip(x,*g)if sum(y)]for x in g if sum(x)]
 for y,x,s in w[::-1]:
  for n,p in e(s*4):
   for y,p in e(u):
    for x,p in e(p):
     for n,p in e(s*all((2*(2*u)[n+y])[m+x]==2*(2!=r)for n,p in e(s)for m,r in e(p))):u[n+y][x:x+3]=p;s=[]
   s=*zip(*s[::-1]),
 return u
# task 234: 120 vs 118 bytes for gold, https://arcprize.org/play?task=98cf29f8
p=lambda i,k=3,h={0}:-k*i or p([*zip(*([x for x in i if len(h:=h|{*x})-3+sum(x)-max(x)]+i[-1:]*99)[:len(i)])][::-1],k-1)
# task 235: 62 bytes, gold, https://arcprize.org/play?task=995c5fa3
p=lambda g:[[g[1][x]*sum(g[2][x:x+3])%13^8]*3for x in[1,6,11]]
# task 236: 62 vs 54 bytes for gold, https://arcprize.org/play?task=99b1bc43
p=lambda i:[[-y%5^s*3for s,y in zip(*x)]for x in zip(i,i[5:])]
# task 237: 67 bytes, gold, https://arcprize.org/play?task=99fa7670
p=lambda a,c=0:[(b:=0)or[c:=(b:=b or d)for d in r+[c]]for*r,_ in a]
# task 238: 225 (282 unzipped) bytes, gold, https://arcprize.org/play?task=9aec4887
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and((k:=l[a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]
# task 239: 104 bytes, gold, https://arcprize.org/play?task=9af7a82c
p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted({(e,~e)*b.count(e)+(0,)*99for e in b},key=sum)))][1::2]
# task 240: 107 vs 99 bytes for gold, https://arcprize.org/play?task=9d9215db
p=lambda i,k=4,r=range(19):-k*i or p([[i[~b][a]|i[b][a]|i[b%2*(a<b<18-a)*a+2][a]for b in r]for a in r],k-1)
# task 241: 21 bytes, gold, https://arcprize.org/play?task=9dfd6313
p=lambda a:[*zip(*a)]
# task 242: 54 bytes, gold, https://arcprize.org/play?task=9ecd008a
p=lambda g:[r[~r.index(0)::-1][:3]for r in g if 0in r]
# task 243: 79 bytes, gold, https://arcprize.org/play?task=9edfc990
p=lambda a,n=-79:a*n or[*zip(*eval(str(p(a,n+1)[::-1]).replace('1, 0','1,1')))]
# task 244: 65 bytes, gold, https://arcprize.org/play?task=9f236235
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)
# task 245: 142 vs 110 bytes for gold, https://arcprize.org/play?task=a1570a43
p=lambda i,k=15:-k*i or p([[y[1]%2*3or y[(f:=sum(i,[]).index)(3)//(w:=len(i[0]))<f(2)//w]%3for y in zip([0,*x],x)]for x in zip(*i)][::-1],k-1)
# task 246: 131 vs 126 bytes for gold, https://arcprize.org/play?task=a2fd1cf0
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k+2in x)*8for b,y in enumerate(x)]for x in zip(*i)],k-1)
# task 247: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a3325580
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]
# task 248: 79 vs 72 bytes for gold, https://arcprize.org/play?task=a3df8b1e
def p(g,A=0,C=-1):
 for x in g[::-1]:x[A]=1;C*=-(A%~-len(x)<1)|1;A+=C
 return g
# task 249: 26 bytes, gold, https://arcprize.org/play?task=a416b8f3
p=lambda a:[r*2for r in a]
# task 250: 127 bytes, gold, https://arcprize.org/play?task=a48eeaf7
import re
p=lambda i,k=7:-k*i or p(eval(re.sub(r"5(((.{34}0)+)(.{32})|([0, ]+)), 2",r"0\2\5+5\4,2",str([*zip(*i[::-1])]))),k-1)
# task 251: 94 vs 89 bytes for gold, https://arcprize.org/play?task=a5313dff
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]
# task 252: 61 vs 57 bytes for gold, https://arcprize.org/play?task=a5f85a15
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]
# task 253: 148 bytes, gold, https://arcprize.org/play?task=a61ba2ce
def p(g):f=sum(g,[]);k=f*2;return[[max(v*(k[i+1-j%5]*k[i+13-j%3*13]==v*v)for i,v in enumerate(f))for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]
# task 254: 103 vs 84 bytes for gold, https://arcprize.org/play?task=a61f2674
def p(i):k=*map(sum,zip(*i)),;return[[y and s//max(k)+min({*k}-{0})//s*2for y,s in zip(x,k)]for x in i]
# task 255: 269 (325 unzipped) bytes, gold, https://arcprize.org/play?task=a64e4611
def p(g):
 g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in range(30)]for y in range(30)]
 for y in'y'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in range(30):
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]
# task 256: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a65b410d
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
# task 257: 75 bytes, gold, https://arcprize.org/play?task=a68b268e
p=eval('lambda a:[[max(sum(a,()),key=bool)'+'for*a,in map(zip,a,a[5:])]'*2)
# task 258: 61 bytes, gold, https://arcprize.org/play?task=a699fb00
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))
# task 259: 85 bytes, gold, https://arcprize.org/play?task=a740d043
p=lambda i,k=39:-k*i or p([*zip(*eval(str(i).replace(*"10"))[any(i[-1])-2::-1])],k-1)
# task 260: 150 bytes, gold, https://arcprize.org/play?task=a78176bb
r=range(10)
p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j]or sum(m-n-i+j+k%5-2==0<a[m][n]for m in r for n in r for k in r)==2)for j in r]for i in r]
# task 261: 47 bytes, gold, https://arcprize.org/play?task=a79310a0
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]
# task 262: 39 bytes, gold, https://arcprize.org/play?task=a85d4709
p=lambda i:[[~b//~a^2]*3for a,b,_ in i]
# task 263: 122 bytes, gold, https://arcprize.org/play?task=a87f7484
p=lambda g:g[(T:=[*zip(*[(x>0for y in g for x in y)]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p([*zip(*g)]))]
# task 264: 216 bytes, gold, https://arcprize.org/play?task=a8c38be5
p=lambda g,R=range:[[sorted([sum([s[x:x+3]for s in g[y:y+3]],[])for y in R(len(g)-2)for x in R(len(g[0])-2)],key=lambda v:[-all(v)]+[A==5for A in v])[b"\0"[B//3*3+C//3]][B%3*3+C%3]for C in R(9)]for B in R(9)]
# task 265: 149 vs 115 bytes for gold, https://arcprize.org/play?task=a8d7556c
def p(i):
 for n in range(289):
  for x in i[(a:=n//17)+3%~-sum(i[a][(b:=n%17):b+2]+i[a+1][b:b+2]):a+2]*(sum(i[1])!=49or a!=8):x[b:b+2]=2,2
 return i
# task 266: 103 vs 102 bytes for gold, https://arcprize.org/play?task=a9f96cdd
p=lambda g:[([0,0,0,r%9,0,r//9]*2)[4-max(g).index(2):][:5]for r in b'\09\0G\0'[2-g.index(max(g)):][:3]]
# task 267: 52 vs 46 bytes for gold, https://arcprize.org/play?task=aabf363d
p=lambda i:[[i[-y>>8][x==i[6]]for y in x]for x in i]
# task 268: 284 (331 unzipped) vs 250 bytes for gold, https://arcprize.org/play?task=aba27056
def p(g,k=3):
 l=range(len(g));B=[sum(A>0for A in A)for A in g if any(A)]
 if B[0]==max(B)>0<B.count(B[0])<2:
  (J,E),*B,(C,F)=sorted([A,C]for A in l for C in l if g[A][C])
  for A in l[J+1:]:
   for D in((*range(E+2,F-1),F+A-C-2,E-A+C+2),range(E+1,F))[A<C]:
    if D in l:g[A][D]=4
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
# task 269: 64 vs 63 bytes for gold, https://arcprize.org/play?task=ac0a08a4
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 270: 119 vs 117 bytes for gold, https://arcprize.org/play?task=ae3edfdc
import re;p=lambda i,k=7:-k*i or eval(re.sub(f"({k|3})([, \d]*)0(, {2-k//4})",r"0\2\1\3",str([*zip(*p(i,k-1)[::-1])])))
# task 271: 86 bytes, gold, https://arcprize.org/play?task=ae4f1146
p=eval(f"lambda a:max([str(a).count('1'),a]{'for*a,in map(zip,a,a[1:],a[2:])'*2})[1]")
# task 272: 95 vs 89 bytes for gold, https://arcprize.org/play?task=aedd82e4
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]
# task 273: 116 bytes, gold, https://arcprize.org/play?task=af902bf9
R=range(10)
p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in{*R}-{i}for J in{*R}-{j}})//5*2for j in R]for i in R]
# task 274: 75 vs 71 bytes for gold, https://arcprize.org/play?task=b0c4d837
p=lambda i:[(h:=[8]*sum({*x}=={0,5}for x in i)+[0]*5)[1:4],h[6:3:-1],[0]*3]
# task 275: 137 bytes, gold, https://arcprize.org/play?task=b190f7f5
p=lambda i:"8"in str(i[(u:=len(i[0])):])and[[t*y/8for t in s for y in x]for s in i[:u]for x in i[u:]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
# task 276: 38 bytes, gold, https://arcprize.org/play?task=b1948b0a
p=lambda a:eval(str(a).replace(*'62'))
# task 277: 199 vs 194 bytes for gold, https://arcprize.org/play?task=b230c067
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
# task 278: 143 vs 118 bytes for gold, https://arcprize.org/play?task=b27ca6d3
p=lambda i,k=3,e=enumerate:-k*i or p([[y or("2, 2"in str([h[a:a+3]for h in i[b-(b>0):b+2]]))*3for b,y in e(x)]for a,x in e(zip(*i))][::-1],k-1)
# task 279: 113 vs 110 bytes for gold, https://arcprize.org/play?task=b2862040
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=0:[[b+7*(a>1==b),b%(9+a),(a:=b)or 9][f>>6]for b in r],*g[::-1])],f-1)
# task 280: 182 vs 179 bytes for gold, https://arcprize.org/play?task=b527c5c6
def p(a,n=3,i=0):
	for b in a:
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):(i:=i+1)+d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
# task 281: 146 bytes, gold, https://arcprize.org/play?task=b548a754
import re
p=lambda i,k=39:-k*i or p(eval(re.sub(r"(\((?=[^)]+[1-9])[^)]+., )(\([^)]+.), \((?=.*8)[08, ]+\)",r"\1\1\2",str([*zip(*i[::-1])]))),k-1)
# task 282: 83 bytes, gold, https://arcprize.org/play?task=b60334d2
p=lambda a:[*map(f:=lambda d,*b,c=0:[c|(c:=d)>>2|(d:=e)for e in[*b,0]],*map(f,*a))]
# task 283: 94 vs 86 bytes for gold, https://arcprize.org/play?task=b6afb2da
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]
# task 284: 238 vs 220 bytes for gold, https://arcprize.org/play?task=b7249182
def p(i,k=1,E=enumerate):
 m=max(i)
 if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[(abs(a-i.index(m))in[*(t-s-2)//2*[[0]],[0,1,2],[2],*[[]]*9][min(t-b,b-s)])*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return-k*i or p([*zip(*i)],k-1)
# task 285: 317 (400 unzipped) vs 306 bytes for gold, https://arcprize.org/play?task=b775ac94
def p(g,k=7):
 I=[]
 for A,r in enumerate(g):
  for B,F in enumerate(r):
   G={(A,B)}
   for D in(F>0)*I:
    if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
   I+=(F>0)*[G]
 for G in I:
  for C,D in G:
   for E in range(25):
    if{*G}&{(C-E%5,E//5-~D),(E%5-~C,D-E//5)}:g[C-E%5][D-E//5]|=len({*str([x[D:D+2]for x in g[C:C+2]])})//8*g[C][D]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
# task 286: 121 vs 109 bytes for gold, https://arcprize.org/play?task=b782dc8a
p=lambda i,k=139:-k*i or[[z[1]or([0,*{*z,8}^{*sum(i,[])}]*2)[3]for z in zip([0,*x],x,[*x[1:],0])]for x in zip(*p(i,k-1))]
# task 287: 63 vs 56 bytes for gold, https://arcprize.org/play?task=b8825c91
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]
# task 288: 112 vs 101 bytes for gold, https://arcprize.org/play?task=b8cdaf2b
p=lambda i,e=enumerate:[[y or i[-1][t:=len(i)//2]*(a+abs(b-t)==t*2-0**i[-2][-t])for b,y in e(x)]for a,x in e(i)]
# task 289: 64 vs 63 bytes for gold, https://arcprize.org/play?task=b91ae062
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 290: 69 vs 67 bytes for gold, https://arcprize.org/play?task=b94a9452
p=lambda i:[[sum({*sum(i,x)},-y)for y in x if y]for x in i if any(x)]
# task 291: 62 vs 61 bytes for gold, https://arcprize.org/play?task=b9b7f026
p=lambda i,n=1:len({x.count(n)for x in i})//3*[[n]]or p(i,n+1)
# task 292: 58 vs 56 bytes for gold, https://arcprize.org/play?task=ba26e723
p=lambda g:[[6-j%3&v%~5for j,v in enumerate(r)]for r in g]
# task 293: 60 vs 59 bytes for gold, https://arcprize.org/play?task=ba97ae07
p=lambda a:[[d^c^b[0]or d for*_,c,d in zip(*a,b)]for b in a]
# task 294: 76 vs 70 bytes for gold, https://arcprize.org/play?task=bb43febb
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))
# task 295: 54 bytes, gold, https://arcprize.org/play?task=bbc9ae5d
p=lambda a:[b:=a[0]]+[b:=b[:1]+b[:-1]for _ in b[2::2]]
# task 296: 63 bytes, gold, https://arcprize.org/play?task=bc1d5164
p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]
# task 297: 44 vs 43 bytes for gold, https://arcprize.org/play?task=bd4472b8
p=lambda i:i[:2]+[*zip(*[i[0]*2]*len(i[0]))]
# task 298: 55 bytes, gold, https://arcprize.org/play?task=bda2d7a6
p=lambda i:[[i[3][~-x.index(y)%3]for y in x]for x in i]
# task 299: 54 bytes, gold, https://arcprize.org/play?task=bdad9b1f
p=lambda i:[[3%~t+2&8-(2in x)for t in i[0]]for x in i]
# task 300: 87 bytes, gold, https://arcprize.org/play?task=be94b721
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))if max(range(1,10),key=sum(a,a).count)in b]
# task 301: 31 bytes, gold, https://arcprize.org/play?task=beb8660c
p=lambda g,S=sorted:S(map(S,g))
# task 302: 93 vs 89 bytes for gold, https://arcprize.org/play?task=c0f76784
import re
p=lambda i:eval(re.sub("5,([ 0,]*)5(?=, 0|])",r"5,*[5+(r:=len([\1]))]*r,5",str(i)))
# task 303: 64 vs 62 bytes for gold, https://arcprize.org/play?task=c1d99e64
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]
# task 304: 92 bytes, gold, https://arcprize.org/play?task=c3e719e8
p=lambda i:[[t*(y==max(z:=sum(i,i),key=z.count))for y in x for t in s]for x in i for s in i]
# task 305: 62 bytes, gold, https://arcprize.org/play?task=c3f564a4
p=lambda g:[(sorted({*g[0]}-{0})*9)[y:y+16]for y in range(16)]
# task 306: 81 vs 74 bytes for gold, https://arcprize.org/play?task=c444b776
p=lambda i,k=7:-k*i or[[*x[:10],*map(max,x,x[10:])]for x in zip(*p(i,k-1))][::-1]
# task 307: 52 vs 50 bytes for gold, https://arcprize.org/play?task=c59eb873
p=eval('lambda a:[[a '+"for a in a for _ in'  ']"*2)
# task 308: 249 (266 unzipped) bytes, gold, https://arcprize.org/play?task=c8cbb738
def p(g):
 *L,M=sorted(set(E:=sum(g,[])),key=E.count);A=[99*[M]for(A)in g]
 for N in L:
  (F,G),*B,(P,Q)=C=[[A,C]for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==N];B=max(H:=P-F,I:=Q-G)+1
  for(J,K)in C:A[J-F+(B-H)//2][K-G+(B-I)//2]=N
 return[A[:B]for A in A[:B]]
# task 309: 38 bytes, gold, https://arcprize.org/play?task=c8f0f002
p=lambda a:eval(str(a).replace(*'75'))
# task 310: 81 vs 78 bytes for gold, https://arcprize.org/play?task=c909285e
p=lambda a,*n:[b for b in zip(*n or p(a,*a))if min(c:=sum(a,[]),key=c.count)in b]
# task 311: 32 bytes, gold, https://arcprize.org/play?task=c9e6f938
p=lambda a:[r+r[::-1]for r in a]
# task 312: 45 vs 44 bytes for gold, https://arcprize.org/play?task=c9f8e694
p=lambda a:[[e and r[0]for e in r]for r in a]
# task 313: 65 vs 63 bytes for gold, https://arcprize.org/play?task=caa06a1f
p=lambda g,x=1:[(g[x:=x^1][1:len({*g[0]})]*9)[:len(g)]for _ in g]
# task 314: 97 vs 96 bytes for gold, https://arcprize.org/play?task=cbded52d
p=lambda i,r=range(8):[[max((x:=i[a])[b-5]&x[b-3],i[a-5][b]&i[a-3][b],x[b])for b in r]for a in r]
# task 315: 63 bytes, gold, https://arcprize.org/play?task=cce03e0d
p=lambda i:[[t&-y%5for y in x for t in s]for x in i for s in i]
# task 316: 72 vs 71 bytes for gold, https://arcprize.org/play?task=cdecee7f
p=lambda i:[(q:=sorted(map(max,*i),key=0 .__eq__))[:3],q[5:2:-1],q[6:9]]
# task 317: 59 bytes, gold, https://arcprize.org/play?task=ce22a75a
p=lambda i,r=b"":[[i[a][b]>0for b in r]for a in r]
# task 318: 60 vs 54 bytes for gold, https://arcprize.org/play?task=ce4f8723
p=lambda i:[[any(y)*3for y in zip(*x)]for x in zip(i,i[5:])]
# task 319: 243 (293 unzipped) vs 199 bytes for gold, https://arcprize.org/play?task=ce602527
def p(a):g=max(f:=sum(A:=a,[]),key=f.count);return[[[[g,d][d==e]for*b,d in zip(*a,b)if e in b]for b in a if e in b]for e in{*f}for i in range(2652)if[]<(b:=[a for a,A in zip(a,sum(zip(A,A),((),)*19)[i%51:])for a,A in zip(a,sum(zip(A,A),((),)*19)[i%52:])if a!=A==e!=g])==b[:1]*f.count(b[0])][0]
# task 320: 72 vs 68 bytes for gold, https://arcprize.org/play?task=ce9e57f2
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]
# task 321: 57 vs 55 bytes for gold, https://arcprize.org/play?task=cf98881b
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
# task 322: 48 bytes, gold, https://arcprize.org/play?task=d037b0a7
p=lambda a:[[*map(max,*a[:n]*2)]for n in(1,2,3)]
# task 323: 153 vs 122 bytes for gold, https://arcprize.org/play?task=d06dbe63
p=lambda i,k=1,r=range(13):-k*i or p([[i[a][~b]+any(8in sum(i[a:],[])[n-b::24][:max(14-b-~n%13>>1,0)]for n in b"&%$")*5for b in r]for a in r][::-1],k-1)
# task 324: 289 (343 unzipped) bytes, gold, https://arcprize.org/play?task=d07ae81c
def p(g,e=enumerate):
 s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count)
 if any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g):b,B=B,b
 for y,r in e(eval(str(g))):
  for x,c in e(r):
   for z,s in e(g):
    for Y,X in((z,z),(z,-z),(-z,z),(-z,-z)):
     if{c}&{k,K}and len(g)>Y+y>-1<X+x<len(g[0]):t=g[Y+y][X+x];g[Y+y][X+x]=k*(t==b)+K*(t==B)or t
 return g
# task 325: 172 vs 161 bytes for gold, https://arcprize.org/play?task=d0f5fe59
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
# task 326: 30 bytes, gold, https://arcprize.org/play?task=d10ecb37
p=lambda a:[a[0][:2],a[1][:2]]
# task 327: 67 bytes, gold, https://arcprize.org/play?task=d13f3404
p=lambda i,l=[0]*3:[l:=[*map(max,x+[0]*3,[0]+l*2)]for x in i+[l]*3]
# task 328: 188 vs 175 bytes for gold, https://arcprize.org/play?task=d22278a0
p=lambda i,k=3,e=enumerate:-k*i or[[y|((a-~b>(t:=len(x)-1))*i[0][-1]+b*2//t*i[-1][-1]+a*2//t*i[0][0]<~max(a,b)%2)*i[-1][0]for b,y in e(x)]for a,x in e(zip(*p([*zip(*i[::-1])],k-1)))][::-1]
# task 329: 54 bytes, gold, https://arcprize.org/play?task=d23f8c26
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]
# task 330: 139 vs 134 bytes for gold, https://arcprize.org/play?task=d2abd087
p=lambda i,k=179:-k*i or p([[{*[k:=k-1]*y}if k>78else[y and{*e}|y,118%~len(y)%3][k<1]for y,e in zip(x,[[],*x])]for x in zip(*i[::-1])],k-1)
# task 331: 86 vs 83 bytes for gold, https://arcprize.org/play?task=d364b489
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, 0","1,86//k%10")),k-2)
# task 332: 61 vs 58 bytes for gold, https://arcprize.org/play?task=d406998b
p=lambda m:[[len(r)*r.pop(0)%2*3or x for x in[*r]]for r in m]
# task 333: 92 bytes, gold, https://arcprize.org/play?task=d43fd935
p=lambda a,n=-3:n*a or[(d:=0)or[d:=b.pop()|d*(3in b[:-1])for _ in a]for*b,in zip(*p(a,n+1))]
# task 334: 75 vs 66 bytes for gold, https://arcprize.org/play?task=d4469b4b
p=lambda i:[[((x|y)>>sum({*sum(i,[])})&1)*5for y in[0,6,8]]for x in[4,2,8]]
# task 335: 133 vs 126 bytes for gold, https://arcprize.org/play?task=d4a91cb9
p=lambda i,k=1:-k*i or p([[y or(sum((t:=[*map(max,i)])[:b+1])*sum(t[b:])>0<k*6+2in x)*4for b,y in enumerate(x)]for x in zip(*i)],k-1)
# task 336: 105 vs 103 bytes for gold, https://arcprize.org/play?task=d4f3cd78
p=lambda i,k=3:-k*i or[[x[b]or(sum(x[:b])%8|1in x[:4])*8for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
# task 337: 46 bytes, gold, https://arcprize.org/play?task=d511f180
p=lambda g:[[x^84%x%3*13for x in r]for r in g]
# task 338: 104 vs 64 bytes for gold, https://arcprize.org/play?task=d5d6de2d
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]
# task 339: 37 bytes, gold, https://arcprize.org/play?task=d631b094
p=lambda a:[[*filter(int,sum(a,[]))]]
# task 340: 133 vs 120 bytes for gold, https://arcprize.org/play?task=d687bc17
p=lambda i,k=3:-k*i or[[x[0],sum({*x[1:]}&{*x[:2]}),*[y*(sum(i,i).count(y)>4>0<y!=x[0])for y in x[2:]]]for x in zip(*p(i,k-1)[::-1])]
# task 341: 139 vs 132 bytes for gold, https://arcprize.org/play?task=d6ad076f
p=lambda i,k=1,r=range(10):-k*i or p([[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a-(a>0):a+2])*8for b in r]for a in r],k-1)
# task 342: 119 vs 112 bytes for gold, https://arcprize.org/play?task=d89b689b
p=lambda i,s=-1:[[y==8and[g for g in[*map(max,*i[:a]),*map(max,*i[a:])]if g%8][s:=s+1]for y in i[a]]for a in range(10)]
# task 343: 75 vs 65 bytes for gold, https://arcprize.org/play?task=d8c310e9
p=lambda i:[*zip(*((h:=[*zip(*i)])[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15])]
# task 344: 78 bytes, gold, https://arcprize.org/play?task=d90796e8
p=lambda i,k=3:-k*i or[*zip(*eval(str(p(i,k-1)[::-1]).replace("2, 3","0,8")))]
# task 345: 109 vs 90 bytes for gold, https://arcprize.org/play?task=d9f24cd1
p=lambda i,r=range(10):[[i[a][b]|2&6%~sum((t:=[*zip(*i)])[b-1][a-(a>0):])+max(t[b][a:])for b in r]for a in r]
# task 346: 68 vs 58 bytes for gold, https://arcprize.org/play?task=d9fac9be
p=lambda i:[max([n]for n in sum(i,[])if str(i).count(f"{n}, "*3)<2)]
# task 347: 50 bytes, gold, https://arcprize.org/play?task=dae9d2b5
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]
# task 348: 101 bytes, gold, https://arcprize.org/play?task=db3e9e38
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,_ in a[1:]+a[-1:]],n+1)
# task 349: 239 (261 unzipped) vs 214 bytes for gold, https://arcprize.org/play?task=db93a21d
p=lambda i,n=6,l=0,R=range:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3or 9in[*zip(*i[:x+1])][y]for y in R(l)]for x in R(l)]for a in R(-n*2,l)for b in R(l-n*2+1)if{min(x[max(b,0):b+n*2])for x in i[max(a,0):a+n*2]}=={9}]]and p(i,n-1,len(i))
# task 350: 96 vs 94 bytes for gold, https://arcprize.org/play?task=dbc1a6ce
p=lambda i,*n:[[y or(1in x[b:]!=1in x[:b])*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
# task 351: 68 vs 67 bytes for gold, https://arcprize.org/play?task=dc0a314f
p=lambda i:[s[~x.index(3)::-1][:5]for x,s in zip(i,i[::-1])if 3in x]
# task 352: 86 vs 84 bytes for gold, https://arcprize.org/play?task=dc1df850
p=lambda i,k=3:-k*i or[*map(lambda*x,t=0:[max(0<t<3,t:=y)for y in x],*p(i,k-1)[::-1])]
# task 353: 104 vs 92 bytes for gold, https://arcprize.org/play?task=dc433765
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)
# task 354: 101 vs 97 bytes for gold, https://arcprize.org/play?task=ddf7fa4f
p=lambda i,k=9:-k*i or p([[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0,*x])][::-1]for x in i],k-1)
# task 355: 101 vs 99 bytes for gold, https://arcprize.org/play?task=de1cd16c
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]
# task 356: 105 bytes, gold, https://arcprize.org/play?task=ded97339
p=lambda i,r=range(10):[[max({*i[a][b:]}&{*i[a][:b+1]}|{*c[a:]}&{*c[:a]})for*c,b in zip(*i,r)]for a in r]
# task 357: 92 vs 86 bytes for gold, https://arcprize.org/play?task=e179c5f4
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,x%(l:=len(m[0])-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]
# task 358: 97 bytes, gold, https://arcprize.org/play?task=e21d9049
p=lambda i,k=39:-k*i or[[*map(max,x,x[6-13//len({*x,0}):]+(0,0)*9)]for x in zip(*p(i,k-1)[::-1])]
# task 359: 64 bytes, gold, https://arcprize.org/play?task=e26a3af2
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]
# task 360: 45 bytes, gold, https://arcprize.org/play?task=e3497940
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]
# task 361: 211 (241 unzipped) vs 204 bytes for gold, https://arcprize.org/play?task=e40b9e2f
def p(i):I=[r*2for r in i*2];return[[[max(I[x][y],I[a+n+b+~y][b-a+x],I[a-b+y][b+n+a+~x],I[2*a+n+~x][2*b+n+~y])for y in range(10)]for x in range(10)]for n in(4,3,2)for a in range(10)for b in range(10)if all(all(x[b:b+n])for x in I[a:a+n])][0]
# task 362: 73 vs 69 bytes for gold, https://arcprize.org/play?task=e48d4e1a
def p(g):n=g.count(g[0]);return[r[n:9]+r[:1]+r[:n]for r in g[-n:]+g[:-n]]
# task 363: 236 (310 unzipped) vs 216 bytes for gold, https://arcprize.org/play?task=e5062a87
def p(g):
 v=[[y,x]for y,r in enumerate(g)for x,c in enumerate(r)if c%5];i,j=min(v)
 for y,r in enumerate(g):
  for x,c in enumerate(r):
   for Y,X in(1-(g[0]in[[0,5,5,5,5,0,0,5,y!=1,5],[0,5,5,5,0,0,x,5,5,5]]))*v*all(len(g[0])>X-j+x>-1<Y-i+y<len(g)and g[Y-i+y][X-j+x]<1for Y,X in v):g[Y-i+y][X-j+x]=2
 return g
# task 364: 156 bytes, gold, https://arcprize.org/play?task=e509e548
p=lambda i,k=39:-k*i or p([[[y.bit_count()*5%14%9,y and(u*t>0)<<k%4+2|y|u][k>0]for y,t,u in zip(x,[0,*x],s)]for*x,s in zip(*i,[[0]*99,*zip(*i)])][::-1],k-1)
# task 365: 134 vs 112 bytes for gold, https://arcprize.org/play?task=e50d258f
p=lambda i:max([[x[a%9:][:9-a//9%9]for x in i[a//81%9:][:9-a//729]]for a in range(9**4)],key=lambda p:"0"in(r:=str(p))or r.count("2"))
# task 366: 365 (604 unzipped) bytes, gold, https://arcprize.org/play?task=e6721834
def p(m):
 *H,B,S,D=sorted({*sum(m,C:=[])},key=sum(m,C:=[]).count)
 if{*m[0]}>={S,D}:return[*zip(*p([[*C]for C in zip(*m)]))]
 for y,r in enumerate(m):
  for x,v in enumerate(r):
   if D!=v!=S in r:c={(y,x)};[C.remove(d)or(c:=c|d)for d in[*C]if{(y-1,x),(y,x-1)}&d];C+=[c]
 for y,(G,H),*C in sorted((-sum(B!=m[r][c]for r,c in C),min(C),*C)for C in C):
  for y,r in enumerate(m):
   for x,v in enumerate(r):
    for r,c in C*all(len(m[0])>x-H+c>-1<y-G+r<len(m)and(B!=m[r][c]==m[y-G+r][x-H+c]or B==m[r][c]!=D==m[y-G+r][x-H+c])for r,c in C):m[y-G+r][x-H+c]=m[r][c]
 return[r for y,r in enumerate(m)if D in r]
# task 367: 223 vs 130 bytes for gold, https://arcprize.org/play?task=e73095fd
p=lambda g,k=59,e=enumerate:-k*g or p([*zip(*[[[c-c%5+0**c*4,max(c,x+y<1,(v:=(*g[y-(y>0)][x-1:x+1],r[x-1]))==(5,0,0),y>1<x<sum(v)>10>4<g[y-1][x-2]+g[y-2][x-1]or[0,*r][x]%5)][k>0]for x,c in e(r)]for y,r in e(g)][::-1])],k-1)
# task 368: 138 bytes, gold, https://arcprize.org/play?task=e76a88a6
import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m,q=[re.findall("([^50](, [1-9])+)",str(i)*9)for _ in i]:q[m.end()%8].pop(0)[0],str(i)))
# task 369: 114 vs 113 bytes for gold, https://arcprize.org/play?task=e8593010
p=lambda m,i=95:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("2320,,,,    133"[i%5::4],"1213,,,,121"[i%5::4])))]
# task 370: 269 (361 unzipped) bytes, gold, https://arcprize.org/play?task=e8dc4411
def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8*v][x-1+V%8*v]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
# task 371: 114 bytes, gold, https://arcprize.org/play?task=e9614598
def p(a):
	b=sum(a,[]).index;d=b(1,b(1)+1)+b(1)>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a
# task 372: 48 bytes, gold, https://arcprize.org/play?task=e98196ab
p=lambda a:[b for*b,in map(map,[max]*5,a,a[6:])]
# task 373: 39 bytes, gold, https://arcprize.org/play?task=e9afcf9a
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]
# task 374: 152 vs 123 bytes for gold, https://arcprize.org/play?task=ea32f347
p=lambda i,k=19,t=0:-k*i or p([[0**k*sorted({*sum(i,[])}).index(y)*2%5or(y>0)*max(s,5+(t:=s and-~t),s:=y)for y in x]for x in zip(*i[::-1])if[s:=0]],k-1)
# task 375: 53 bytes, gold, https://arcprize.org/play?task=ea786f4a
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g
# task 376: 30 bytes, gold, https://arcprize.org/play?task=eb281b96
p=lambda a:(a+a[1:-1])*2+a[:1]
# task 377: 57 vs 55 bytes for gold, https://arcprize.org/play?task=eb5a1d5d
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]
# task 378: 144 bytes, gold, https://arcprize.org/play?task=ec883f72
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(f"0(?=({(s:=f'.{ {3*len(i)+1}}0')}, 0)*{s}, ., [^0]{s*2}, (.))","\\2",str(p(i,k-1)))))][::-1]
# task 379: 141 bytes, gold, https://arcprize.org/play?task=ecdecbb3
import re
p=lambda i,k=7,r=re.sub:-k*i or[*zip(*eval(r(", 4, ","|8,8,8|",r("0, 8, ((0, )+)2","4,2,4,*[2]*len([\\1])",str(p(i,k-1)[::-1])))))]
# task 380: 27 bytes, gold, https://arcprize.org/play?task=ed36ccf7
p=lambda a:[*zip(*a)][::-1]
# task 381: 93 vs 84 bytes for gold, https://arcprize.org/play?task=ef135b50
import re
p=lambda m:eval(re.sub("(?<=.{30}2,)([0, ]*)(?=2.{30})","*[9]*len([\\1]),",str(m)))
# task 382: 145 vs 134 bytes for gold, https://arcprize.org/play?task=f15e1fac
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)
# task 383: 121 bytes, gold, https://arcprize.org/play?task=f1cefba8
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]
# task 384: 62 bytes, gold, https://arcprize.org/play?task=f25fbde4
p=lambda a,*n:sum([[b,b]for*b,in zip(*n or p(*a))if 4in b],[])
# task 385: 25 bytes, gold, https://arcprize.org/play?task=f25ffba3
p=lambda a:a[:4:-1]+a[5:]
# task 386: 52 bytes, gold, https://arcprize.org/play?task=f2829549
p=lambda a:[[3>>e+r.pop(0)for e in r[4:]]for r in a]
# task 387: 232 (238 unzipped) vs 222 bytes for gold, https://arcprize.org/play?task=f35d900a
p=lambda i,k=3:-k*i or p([[(y<1>k)*([*{*sum(i,[])}-{*sum([*zip(*i[b-(b>0):b+2])][a-(a>0):a+2],()),5},0]*2)[2]+(sum(x[b+1:])%5>0<sum(x[:b])%5>x[b-1]+x[b+1]==0<x[b-2]+x[b+2])*5or y for b,y in enumerate(x)]for a,x in enumerate(zip(*i))],k-1)
# task 388: 62 vs 61 bytes for gold, https://arcprize.org/play?task=f5b8619d
p=lambda a:2*[2*[d or any(c)*8for*c,d in zip(*a,b)]for b in a]
# task 389: 57 bytes, gold, https://arcprize.org/play?task=f76d97a5
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]
# task 390: 126 vs 100 bytes for gold, https://arcprize.org/play?task=f8a8fe49
p=lambda m,k=3,R=range(-14,1):-k*m or p([*zip(*[m[(len([l:=i-j for j in R if 2in m[-j]])==4>abs(l)>1)*2*l-i]for i in R])],k-1)
# task 391: 63 bytes, gold, https://arcprize.org/play?task=f8b3ba0a
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]
# task 392: 203 vs 156 bytes for gold, https://arcprize.org/play?task=f8c80d96
def p(g):
 e=enumerate;C=max(sum(g,[]));o=2+(f"{C}, 0, 0, {C}"in str(g))
 for k,_ in e(g):g=[[c or any(any(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])*[C,5][k%o<o-1]for x,c in e(r)]for y,r in e(g)]
 return g
# task 393: 63 bytes, gold, https://arcprize.org/play?task=f8ff0b80
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# task 394: 92 vs 91 bytes for gold, https://arcprize.org/play?task=f9012d9b
p=lambda i:[[max(x[b%(n:=2+len(i)//7)::n])for b,y in enumerate(x)if y<1]for x in i if 0in x]
# task 395: 56 vs 53 bytes for gold, https://arcprize.org/play?task=fafffa47
p=lambda a:[[2-c-b.pop(0)&6for c in a.pop(3)]for b in a]
# task 396: 248 (281 unzipped) vs 220 bytes for gold, https://arcprize.org/play?task=fcb5c309
def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for y in range(N):
  for x in range(M):
   Y=y;X=x
   for e in range(M):X+=(m[y]*2)[X]==b<M>X;Y+=Y<N!=(m[Y]*2)[x]==b;z=max(z,[sum(sum(a:=[[d*(e>0)for e in e[x:X]]for e in m[y:Y]],[]))//d,a])
 return z[1]
# task 397: 130 vs 121 bytes for gold, https://arcprize.org/play?task=fcc82909
p=lambda m,k=0:exec('r=k//9;c=k%9;exec("m[r+2][c:c+2]=3,3;r+=1;"*len(a:={*m[r][c:c+2]+m[r+1][c:c+2]})*(not{0,3}&a));k+=1;'*81)or m
# task 398: 79 vs 77 bytes for gold, https://arcprize.org/play?task=feca6190
def p(a):b,=a;l=25-5*b.count(0);return[((~-l*[0]+b)*2)[i:i+l]for i in range(l)]
# task 399: 64 bytes, gold, https://arcprize.org/play?task=ff28f65a
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]
# task 400: 70 vs 67 bytes for gold, https://arcprize.org/play?task=ff805c23
p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]
