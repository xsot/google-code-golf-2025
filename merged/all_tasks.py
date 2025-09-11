# task 1: 61 bytes, gold, https://arcprize.org/play?task=007bbfb7
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]
# task 2: 91 vs 90 bytes for gold, https://arcprize.org/play?task=00d62c1b
p=lambda a,n=-62:[*map(lambda*b,d=0:[d:=c%(d+4)+(n>c)*4for c in b][::-1],*n*a or p(a,n+1))]
# task 3: 58 bytes, gold, https://arcprize.org/play?task=017c7c7b
p=lambda g:[[v*2for v in l]for l in g+g[g[:3]*2==g:][2:5]]
# task 4: 83 vs 80 bytes for gold, https://arcprize.org/play?task=025d127b
import re
p=lambda i:eval(re.sub(r"(([1-9]).*?), 0(?=.*\2.*].*\2)",r"0,\1",str(i)))
# task 5: 219 (290 unzipped) vs 206 bytes for gold, https://arcprize.org/play?task=045e512c
p=lambda g:(R:=max([{(i,j)for i in range(21)[I:I+3]for j in range(21)[J:J+3]if g[i][j]}for I in range(21)for J in range(21)],key=len),[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in(-4,0,4)for D in(-4,0,4)for k in range(21)[1:]for c in R)for x in range(21)]for y in range(21)])[1]
# task 6: 51 bytes, gold, https://arcprize.org/play?task=0520fde7
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
# task 7: 65 vs 62 bytes for gold, https://arcprize.org/play?task=05269061
p=lambda a:[[max(sum(a:=a[1:3]+a,[0])[::3])for _ in r]for r in a]
# task 8: 94 vs 84 bytes for gold, https://arcprize.org/play?task=05f2a901
p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]
# task 9: 109 bytes, gold, https://arcprize.org/play?task=06df4c85
p=lambda g,E=enumerate:[[max({*r[:j+1]}&{*r[j::3]}|{*c[:i]}&{*c[i::3]})for j,c in E(zip(*g))]for i,r in E(g)]
# task 10: 72 vs 68 bytes for gold, https://arcprize.org/play?task=08ed6ac7
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]
# task 11: 125 vs 121 bytes for gold, https://arcprize.org/play?task=09629e4f
v=[[5]*11]*9
p=eval(f"lambda a:[a {'for*a,in map(zip,a,a,a,v,*[a[1:]]*3,v,*[a[2:]]*3)'*2}if(c:=sum(a,()).count)(5)<c(0)][0]")
# task 12: 132 vs 127 bytes for gold, https://arcprize.org/play?task=0962bcdd
import re;p=lambda i:[i:=eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0,",r"\1\2\4\3,0,\2+",str([*zip(*i[::-1])])))for _ in i][7]
# task 13: 146 vs 140 bytes for gold, https://arcprize.org/play?task=0a938d79
def p(i):f,*r=map(i.index,filter(any,i));a=62+f;return[len(x)*[max(i[f+61%(a:=a-1)%(r[0]-f<<1)])]for x in i if i[len(x):]]or[*zip(*p([*zip(*i)]))]
# task 14: 69 vs 70 bytes for gold, https://arcprize.org/play?task=0b148d64
p=lambda i,*I:[w for*w,r in zip(*I or p(zip(*i),*i),i)if len({*r})>2]
# task 15: 106 vs 93 bytes for gold, https://arcprize.org/play?task=0ca9ddb6
p=eval(f"lambda i:[i:=[[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7{'for %s in range(9)]'*3%(*'ba_',)}[3]")
# task 16: 44 vs 43 bytes for gold, https://arcprize.org/play?task=0d3d703e
p=lambda m:[[i^466%(1|12-i)for i in m[0]]]*3
# task 17: 118 vs 99 bytes for gold, https://arcprize.org/play?task=0dfd9992
R=range(21);p=lambda a,n=1:[[max(max(a[i%n::n])[j%n::n])for j in R]for i in R]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
# task 18: 316 (390 unzipped) vs 323 bytes for gold, https://arcprize.org/play?task=0e206a2e
def p(g):
 def p(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v}
 for j in G:s={j};[abs(x-y)<2==s.add(x)for x in[*G]*5for y in[*s]];[*s][3:]and[p((x-j-a//4*(x-j).real*2)*1j**a+O,G[x])==p(x,0)for a in[1,3,6,7]for O in G if all(G[A]in{max(f:=[*G.values()],key=f.count),G.get((A-j-a//4*(A-j).real*2)*1j**a+O)}for A in s)for x in s]
 return g
# task 19: 105 bytes, gold, https://arcprize.org/play?task=10fcaaa3
z=[[0]*9]
p=eval('lambda a:[[a[1][1]or 8*any(sum(a,())[::2])'+'for*a,in map(zip,z+a+a,a+a,a[1:]+a+z)]'*2)
# task 20: 139 vs 146 bytes for gold, https://arcprize.org/play?task=11852cab
S='+[*map(any,g:=[*zip(*g)])].index(1)'*2
p=eval(f"lambda g:[g:=[[g[J][I]|((g*2)[I-{S}]*2)[4{S}-J]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")
# task 21: 51 vs 57 bytes for gold, https://arcprize.org/play?task=1190e5a7
p=lambda i:i*-1*-1or-~min(map(i.count,i))*[p(i[0])]
# task 22: 97 vs 91 bytes for gold, https://arcprize.org/play?task=137eaa0f
p=lambda i:[[*map(max,*[s[t:t+3]for t in range(132)if(s:=sum(i*2,[]))[t-x]==5])]for x in b'mx\n']
# task 23: 205 vs 195 bytes for gold, https://arcprize.org/play?task=150deff5
import re
p=lambda i:max([i[("5"in(s:=str(i)))*(k:=len(i[0])*3-2):]]+[p(eval(r))for l in[("5,? ?"*3,"2,"*3),("5(.{%d}...)?"%k*3,r"2\1 2\2 2\3"),("5, 5(.{%d})5, 5"%k,r"8,8\1 8,8")]if(r:=re.sub(*l,s,1))!=s])
# task 24: 62 bytes, gold, https://arcprize.org/play?task=178fcbfb
p=lambda i:[[3%-~sum(x)or(2in y)*2for y in zip(*i)]for x in i]
# task 25: 153 vs 131 bytes for gold, https://arcprize.org/play?task=1a07d186
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)
# task 26: 52 bytes, gold, https://arcprize.org/play?task=1b2d62fb
p=lambda a:[[8>>i+b.pop(0)for i in b[4:]]for b in a]
# task 27: 104 vs 103 bytes for gold, https://arcprize.org/play?task=1b60fb0c
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]
# task 28: 70 vs 63 bytes for gold, https://arcprize.org/play?task=1bfc4729
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']
# task 29: 118 vs 108 bytes for gold, https://arcprize.org/play?task=1c786137
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]
# task 30: 97 vs 94 bytes for gold, https://arcprize.org/play?task=1caeab9d
p=lambda i:[[c*x[(H:=h.index)(1)-(j:=j-1)-H(c)]for c in h]for x in i if(h:=[*map(max,*i)],j:=11)]
# task 31: 45 bytes, gold, https://arcprize.org/play?task=1cf80156
p=lambda a,*n:[*filter(any,zip(*n or p(*a)))]
# task 32: 39 bytes, gold, https://arcprize.org/play?task=1e0a9b12
p=lambda a:[*zip(*map(sorted,zip(*a)))]
# task 33: 76 vs 73 bytes for gold, https://arcprize.org/play?task=1e32b0e9
p=lambda g,i=-1:[[v|(v<g[(i:=i+1)//17%6][i%17%6])*r[5]for v in r]for r in g]
# task 34: 164 vs 125 bytes for gold, https://arcprize.org/play?task=1f0c79e5
import re;p=lambda i,k=27:-k*[x[1:10]for x in i[1:10]]or p(eval(re.sub(f"(([13-9]).*)2, 0(.{ {len(i)*3}}.)0, 0",r"\1\2,\2\3\2,2",str([*zip(*i[::-1],[0]*11)]))),k-1)
# task 35: 87 vs 83 bytes for gold, https://arcprize.org/play?task=1f642eb9
p=lambda i,k=3:-k*i or[[x[0**k<=(k:=y)^8]or y for y in x]for x in zip(*p(i,k-1)[::-1])]
# task 36: 90 vs 75 bytes for gold, https://arcprize.org/play?task=1f85a75f
p=lambda i,n=1:(len(l:=(f:=lambda g:[x for x in zip(*g)if n in x])(f(i)))<6)*l or p(i,n+1)
# task 37: 109 vs 105 bytes for gold, https://arcprize.org/play?task=1f876c06
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]
# task 38: 51 bytes, gold, https://arcprize.org/play?task=1fad071e
p=lambda g:[(str(g).count('1, 1')*[1]+[0]*9)[:9:2]]
# task 39: 61 vs 60 bytes for gold, https://arcprize.org/play?task=2013d3e2
p=lambda a,f=filter:[*zip(*[*f(any,zip(*f(any,a)))][:3])][:3]
# task 40: 71 vs 69 bytes for gold, https://arcprize.org/play?task=2204b7a8
p=lambda i,c=9:[[(y>0)*i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]
# task 41: 49 bytes, gold, https://arcprize.org/play?task=22168020
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]
# task 42: 169 vs 139 bytes for gold, https://arcprize.org/play?task=22233c11
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]
# task 43: 57 vs 56 bytes for gold, https://arcprize.org/play?task=2281f1f4
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]
# task 44: 244 (348 unzipped) vs 255 bytes for gold, https://arcprize.org/play?task=228f6490
def p(i):
 for n in range(10):
  for a in range(10):
   for b in range(10):
    k=[[5]+[y*(y==n)or 5for y,*s in zip(x,*i)if n in s]+[5]for x in i if n in x]or i;k=[t:=[5]*len(k[0])]+k+[t]
    if all(i+k in(10,n)for i,k in zip(i[a:]+i,k)for i,k in zip(i[b:]+i,k)):i=[[y*(y!=n)for y in x]for x in i];[5for r,r[b:b+len(k[0])]in zip(i[a:],k)]
 return i
# task 45: 45 bytes, gold, https://arcprize.org/play?task=22eb0ac0
p=lambda g:[10*r[:r[0]==r[9]]or r for r in g]
# task 46: 170 bytes, gold, https://arcprize.org/play?task=234bbc79
p=lambda i,n=0,Z=zip:[*Z(*[[y and max({*p,*x,*q}-{5})for y in x[n:]+x[:n]]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]
# task 47: 55 bytes, gold, https://arcprize.org/play?task=23581191
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
# task 48: 118 vs 92 bytes for gold, https://arcprize.org/play?task=239be575
p=lambda m,i=99,s="":-i*[[8-8*("2"in'%s'%m)]]or p([*zip(*eval(str(m).replace("282"[i%3]+s,"1"+s,2)))][::-1],i-1,", 1")
# task 49: 81 bytes, gold, https://arcprize.org/play?task=23b5c85d
p=lambda a:[c*[e]for b in a if(c:=b.count(e:=min(d:=sum(a,[0]*99),key=d.count)))]
# task 50: 91 vs 85 bytes for gold, https://arcprize.org/play?task=253bf280
p=lambda a:[*map(f:=lambda*b,i=0:[c|3*(8in{*b[:i]}&{*b[(i:=i+1):]})for c in b],*map(f,*a))]
# task 51: 115 bytes, gold, https://arcprize.org/play?task=25d487eb
p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[0*(l:=l|(b!=y>a<1)*(a:=b))+(b:=y)or l for y in x][::-1],*"*4+"i))))")]
# task 52: 41 vs 40 bytes for gold, https://arcprize.org/play?task=25d8a9c8
p=lambda a:[3*[1//len({*b})*5]for b in a]
# task 53: 21 bytes, gold, https://arcprize.org/play?task=25ff71a9
p=lambda a:(a+a)[2:5]
# task 54: 283 (362 unzipped) vs 280 bytes for gold, https://arcprize.org/play?task=264363fd
def p(g):
 f=sum(g,[]);*C,_,B=sorted({*f},key=f.count);M={i*1j+j:v for i,r in enumerate(g)for j,v in enumerate(r)if v in C};T={i for i in M for I in M if abs(I-i)==1}
 for i in{*M}-T:
  for I in T:
   d=I-sum(T)/len(T);g[int(I.imag)][int(I.real)]=B;F=1;u=d+i
   while(g[int(u.imag)][int(u.real)]^B)*F:g[int(u.imag)][int(u.real)]=M[I];u+=d/2;F-=abs(d)<2
 return g
# task 55: 77 vs 83 bytes for gold, https://arcprize.org/play?task=272f95fa
p=lambda i,z=0:i*0!=0and[p(y,3*(z:=z+([y]>i)))for y in i]or i or 2222096>>z&7
# task 56: 40 bytes, gold, https://arcprize.org/play?task=27a28665
p=lambda i:[[0**i[0][0]+0**i[0][2]*3^2]]
# task 57: 49 vs 48 bytes for gold, https://arcprize.org/play?task=28bf18c6
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]
# task 58: 120 vs 103 bytes for gold, https://arcprize.org/play?task=28e73c20
p=lambda i,k=22,s=0:-k*i or[[(len(x)-k>=0==y+s==a-k//4*2)*3+(s:=y)for y in x]for a,x in enumerate(zip(*p(i,k-1)))][::-1]
# task 59: 167 vs 156 bytes for gold, https://arcprize.org/play?task=29623171
p=lambda g,R=range(11):[[(g[r][c]==5)*5or(max(f:=[sum(sum(v[c//3*4:][:3])for v in g[c%3*4:][:3])for c in R])==f[r//4+c//4*3])*sum({*sum(g,[-5])})for c in R]for r in R]
# task 60: 48 bytes, gold, https://arcprize.org/play?task=29c11459
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]
# task 61: 63 bytes, gold, https://arcprize.org/play?task=29ec7d0e
p=lambda i,r=range(18):[[y*x%max(i[~0])+1for y in r]for x in r]
# task 62: 143 bytes, gold, https://arcprize.org/play?task=2bcee788
p=lambda i:{*i[s:=str(i).index(", 2")//31]+i[s+1]}-{2,3}and[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]or i[:s]+(i*2)[9+s::-1]
# task 63: 76 vs 74 bytes for gold, https://arcprize.org/play?task=2bee17df
p=lambda g:[[v or(c>[0]*99<r[1:-1])*3^3for _,*c,_,v in zip(*g,r)]for r in g]
# task 64: 152 bytes, gold, https://arcprize.org/play?task=2c608aff
p=lambda a,n=-3:n*a or[[d:=[e:=b.pop(),d][g[2]!=d>0<e!=g[1]in b]for _ in[*b]]for*b,in zip(*p(a,n+1))if[d:=0,g:=sorted(set(c:=sum(a,a[5])),key=c.count)]]
# task 65: 91 bytes, gold, https://arcprize.org/play?task=2dc579da
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[len(a)//2+1:])]'*2)
# task 66: 278 (322 unzipped) vs 268 bytes for gold, https://arcprize.org/play?task=2dd70a9a
def p(g):
 M={A*1j+B:D for A,C in enumerate(g)for B,D in enumerate(C)};A,C=[y for y in M if M[y]==3];S=[(C+C-A,C-A,0,0),(A+A-C,A-C,0,0)]
 for*V,y,A,C,G in S:
  if(y in M)*16>G|C+13:
   for y in(M[y]==2)*V:g[int(y.imag)][int(y.real)]=3
   F=M[y]>7;y-=A*F;S+=[(y,*V,y+D,D,C+F,~-F*~G)for D in[A][F:]or[A*1j,A/1j]*G]
 return g
# task 67: 33 bytes, gold, https://arcprize.org/play?task=2dee498d
p=lambda a:[b[:len(a)]for b in a]
# task 68: 119 vs 116 bytes for gold, https://arcprize.org/play?task=31aa019c
s='for*a,in map(zip,[s]+a,a,a,a[1:]+[s])]'
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+s*2)
# task 69: 174 vs 151 bytes for gold, https://arcprize.org/play?task=321b1fc6
def p(g):f=str(g+[E:=enumerate]*9);return[[v==8and int([K for k,K in E(f)if{'8'}=={f[32*i+2+j*3-k+h]for h,H in E(f)if{K,H}<{*'12345679'}}][0])for j,v in E(r)]for i,r in E(g)]
# task 70: 82 vs 78 bytes for gold, https://arcprize.org/play?task=32597951
p=lambda i:[[(c[0]+7in{*x}&{*c,hash(c)%1070})*2+c[0]for c in zip(x,*i)]for x in i]
# task 71: 137 vs 119 bytes for gold, https://arcprize.org/play?task=3345333e
p=lambda i,n=32,e=1:[[(e:=e-2%len({*t,l:=[*{}.fromkeys(sum(i,[]))][2]}))*t[t[0]==l]for t in zip(x,(x*9)[n::-1])]for x in i]*e or p(i,n-1)
# task 72: 61 vs 54 bytes for gold, https://arcprize.org/play?task=3428a4f5
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]
# task 73: 46 bytes, gold, https://arcprize.org/play?task=3618c87e
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]
# task 74: 80 vs 79 bytes for gold, https://arcprize.org/play?task=3631a71a
p=lambda i:[i:=[[*map(min,a,[9,9]+a[::-1],c)]for*c,a in zip(*i,i)]for _ in i][2]
# task 75: 88 vs 86 bytes for gold, https://arcprize.org/play?task=363442ee
p=lambda i,r=range(9):[i[a][:4]+[i[a//3*3+1][b//3*3+5]*i[a%3][b%3]for b in r]for a in r]
# task 76: 302 (355 unzipped) vs 276 bytes for gold, https://arcprize.org/play?task=36d67576
E=enumerate
def p(g):
 G={j+i*1j:v^2for i,r in E(g)for j,v in E(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a in range(8):
  for I in G:P=min(J:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=J.get)-I;g=g*any(13%-~J[y]^G.get(y-P,1)for y in J)or[[J.get(i*1j+j+P,v^2)^2for j,v in E(r)]for i,r in E(g)]
 return g
# task 77: 126 bytes, gold, https://arcprize.org/play?task=36fdfd69
import re;p=lambda i,k=23:-k*i or p(eval(re.sub(f"(?<=[24], )[^2](?=(.{ {len(i)*3}}|.) [24])","4",str([*zip(*i[::-1])]))),k-1)
# task 78: 61 vs 60 bytes for gold, https://arcprize.org/play?task=3906de3d
p=lambda i:[*zip(*[sorted(x,key=0 .__eq__)for x in zip(*i)])]
# task 79: 123 bytes, gold, https://arcprize.org/play?task=39a8645d
p=lambda i:max(t:=[h for a in range(144)if all(map(any,(h:=[x[a//12:][:3]for x in i[a%12:][:3]])+[*zip(*h)]))],key=t.count)
# task 80: 252 (272 unzipped) vs 253 bytes for gold, https://arcprize.org/play?task=39e1d7f9
def p(g):e=enumerate;E=g.index(min(g,key=set))+1;c={i*1j+j:V for i,A in e(g[::E])for j,V in e(A[::E])};return[[[y or[c[k:=a//E*1j+q//E],*[c[u+k-K]for K in c if(c[K]==c[u])*2>abs(k-K)]][-1]for q,y in e(b)]for a,b in e(g)]for u in c if all(c.get(u+1j**P)for P,_ in e(g))][0]
# task 81: 95 vs 91 bytes for gold, https://arcprize.org/play?task=3aa6fb7a
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]
# task 82: 50 bytes, gold, https://arcprize.org/play?task=3ac3eb23
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3
# task 83: 40 bytes, gold, https://arcprize.org/play?task=3af2c5a8
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 84: 63 vs 62 bytes for gold, https://arcprize.org/play?task=3bd67248
def p(i,x=1):
 while i[x:]:i[-1][x]=4;i[~x][x]=2;x+=1
 return i
# task 85: 56 vs 50 bytes for gold, https://arcprize.org/play?task=3bdb4ada
p=lambda i:[i:=[f:=y*(x!=i or f<y)for y in x]for x in i]
# task 86: 172 bytes, gold, https://arcprize.org/play?task=3befdf3e
p=lambda i,k=7,s=0:-k*i or[[k<7and(-((s:=(y>0)*min(s-1,-1)or~-max(-s,s,1))>1)or y)or(z:=[*{}.fromkeys(sum(i,[]))])[y and~(y!=z[1])]for y in x]for x in zip(*p(i,k-1)[::-1])]
# task 87: 36 bytes, gold, https://arcprize.org/play?task=3c9b0459
p=lambda a:[b[::-1]for b in a[::-1]]
# task 88: 109 vs 101 bytes for gold, https://arcprize.org/play?task=3de23699
p=lambda a,n=-3:n*a[1:-1]or p([a[1:],[[d and(b:=max(a[n%2]))for d in c]for c in zip(*a[:0:-1])]][e:=b>0],n+e)
# task 89: 236 (278 unzipped) bytes, gold, https://arcprize.org/play?task=3e980e27
def p(g):
 for i in(M:={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g}):
  for I in M:
   s={I}
   for y in[*M]*3:
    if M[i]==M[I]!=any(0<abs(i-I)<2for I in M)<any(0<abs(y-I)<2for I in s):s|={y};g[int((y-I+i).imag)][int(((I-y)*(-1)**M[I]+i).real)]=M[y]
 return g
# task 90: 156 vs 159 bytes for gold, https://arcprize.org/play?task=3eda0437
s='for %s,b in enumerate(%s)';exec(f"p=lambda a:min([j<=i,(C:=str(g:=[[b|6*(i<=m<=j)*(k<=n<=l){s}]{s}]).count)('7'),-C('6'),g]{s*4})[3]"%(*'nbmaiakbjalb',))
# task 91: 63 bytes, gold, https://arcprize.org/play?task=3f7978a0
p=lambda a,n=46:a*~n or p([*zip(*a[(5in a[n%2-2])-2::-1])],n-1)
# task 92: 93 vs 86 bytes for gold, https://arcprize.org/play?task=40853293
p=lambda a:[*map(f:=lambda*b,i=-1:[b[i:=i+1]or sum({*b[i:]}&{*b[:i]})for _ in b],*map(f,*a))]
# task 93: 100 vs 99 bytes for gold, https://arcprize.org/play?task=4093f84a
import re
p=lambda g:[g:=eval(re.sub("[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])])))for _ in g][11]
# task 94: 106 vs 102 bytes for gold, https://arcprize.org/play?task=41e4d17e
p=lambda i,*h:[h:=[(y>2==x.count((c:=h.count)(1)%5-1)>=c(6))*6or y for y in x]for x in zip(*h or p(i,*i))]
# task 95: 75 vs 73 bytes for gold, https://arcprize.org/play?task=4258a5f9
p=lambda a,n=6:~n*a or[[n%2|(n:=b.pop())for _ in a]for*b,in zip(*p(a,n-2))]
# task 96: 322 (373 unzipped) vs 325 bytes for gold, https://arcprize.org/play?task=4290ef0e
def p(g,*S):
 for c in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i for i,v in enumerate(r)if v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for x in r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
 R=range(w:=max(S)[0]);return[[([C for W,G,C in S if G<(M:=sorted(abs(w//2-v)for v in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for j in R]for i in R]
# task 97: 113 vs 108 bytes for gold, https://arcprize.org/play?task=42a50994
p=lambda i,e=enumerate:[[y*(sum(sum([z[b+b%~b:b+2]for z in i[a+a%~a:a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
# task 98: 92 vs 88 bytes for gold, https://arcprize.org/play?task=4347f46a
p=lambda i:[[y^min(t)for*t,y in zip(*w,[0]+s,s[1:]+[0],s)]for*w,s in zip(i[:1]+i,i[1:]+i,i)]
# task 99: 116 vs 115 bytes for gold, https://arcprize.org/play?task=444801d8
p=lambda g,r=range(10):[[g[y][x]or max(sum(g[y:y+4],g[y-1]))*any(g[y-9][:x+1])*any(g[y-9][x:])for x in r]for y in r]
# task 100: 88 vs 85 bytes for gold, https://arcprize.org/play?task=445eab21
p=lambda a:[[max(range(1,10),key=[sum({*b}&{*c})for c in zip(*a)for b in a].count)]*2]*2
# task 101: 280 (338 unzipped) vs 281 bytes for gold, https://arcprize.org/play?task=447fd412
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
# task 105: 153 vs 148 bytes for gold, https://arcprize.org/play?task=4612dd53
A=any;p=lambda g:[g:=[[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for _ in g][3]
# task 106: 75 vs 67 bytes for gold, https://arcprize.org/play?task=46442a0e
p=lambda i:(s:=[a+x for a,*x in zip(i,*i[::-1])])+[x[::-1]for x in s[::-1]]
# task 107: 176 vs 170 bytes for gold, https://arcprize.org/play?task=469497ad
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>>(x-y)%z|g[(t+s)%5::4].count(f)>>(x-~y)%z)&2for y in r]for x in r]
# task 108: 46 vs 56 bytes for gold, https://arcprize.org/play?task=46f33fce
p=lambda a:a>a*0!=0and[p(a[1])]*4+p(a[2:])or a
# task 109: 83 vs 81 bytes for gold, https://arcprize.org/play?task=47c1f68c
p=lambda a:eval('[[a and%s[0]'%a[i:=len(a)//2]+f'for a in a[:{i}]+a[{i}-1::-1]]'*2)
# task 110: 105 vs 85 bytes for gold, https://arcprize.org/play?task=484b58aa
p=lambda g,k=-1:k*g or p([*zip(*[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g])],k+1)
# task 111: 60 bytes, gold, https://arcprize.org/play?task=48d8fb45
p=lambda g:[(f:=sum(g,g))[f.index(5)+d:][:3]for d in b'	']
# task 112: 112 vs 109 bytes for gold, https://arcprize.org/play?task=4938f0c2
p=lambda i,k=1:-k*i or p([[y or(x*2)[[*map(max,i)].index(3)*2-b+1]for b,y in enumerate(x)]for x in zip(*i)],k-1)
# task 113: 25 bytes, gold, https://arcprize.org/play?task=496994bd
p=lambda a:a[:5]+a[4::-1]
# task 114: 65 vs 64 bytes for gold, https://arcprize.org/play?task=49d1d64f
p=lambda g:[[0,*g[0],0],*[r[:1]+r+r[-1:]for r in g],[0,*g[-1],0]]
# task 115: 54 bytes, gold, https://arcprize.org/play?task=4be741c5
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]
# task 116: 20 bytes, gold, https://arcprize.org/play?task=4c4377d9
p=lambda a:a[::-1]+a
# task 117: 172 vs 148 bytes for gold, https://arcprize.org/play?task=4c5c2cf0
p=lambda i,k=1:-k*i or p([[*map(max,x,[*x,*(s:=sum(i,[]))][s.index(max(s,key=lambda n:[x.count(n)for x in i if n in x]==[2,1,2]))//len(i)*2+2::-1]+s)]for x in zip(*i)],k-1)
# task 118: 242 (282 unzipped) vs 271 bytes for gold, https://arcprize.org/play?task=50846271
def p(I):
 for n in 2,3:
  z,t,T,*R=[{(l,n)for l,I in enumerate(I)for n,I in enumerate(I)if I>=C}for C in(0,2,5,7)]
  for d,i in z:v={(l,I)for l,I in z if abs(d-l+(i-I)*1j)in{0,1,2,n}};R+=[l|v for l in R if t-l>v]
  for l in R:
   if t-T<l:
    for l,n in l&T:I[l][n]=8
    return I
# task 119: 106 bytes, gold, https://arcprize.org/play?task=508bd3b6
import re;p=lambda i,k=39:-k*i or[*zip(*eval(re.sub("0(?=.{34}[38].{34}[382])","3",str(p(i,k-1))))[::-1])]
# task 120: 102 vs 97 bytes for gold, https://arcprize.org/play?task=50cb2852
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]
# task 121: 96 vs 89 bytes for gold, https://arcprize.org/play?task=5117e062
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)
# task 122: 82 bytes, gold, https://arcprize.org/play?task=5168d44c
p=lambda a:7in map(sum,a)and a[-2:][::(-1)**len(a)]+a[:-2]or[*zip(*p([*zip(*a)]))]
# task 123: 76 vs 75 bytes for gold, https://arcprize.org/play?task=539a4f51
R=range(10)
p=lambda g:[[g[0][max(i,j)%(5-0**g[0][4])]for j in R]for i in R]
# task 124: 100 vs 96 bytes for gold, https://arcprize.org/play?task=53b68214
p=lambda i,n=0,s=2:(r:=[(k//s*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+s%2,s^1)
# task 125: 141 vs 126 bytes for gold, https://arcprize.org/play?task=543a7ed5
p=lambda i,k=15,r=range(15):-k*i or p([[(y:=i[~b][a])*(y&4>0)or(3<i[~b][a-1]&i[-b][a]<7)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)
# task 126: 57 vs 54 bytes for gold, https://arcprize.org/play?task=54d82841
p=lambda a:a[:-1]+[[4*(sum(c)<2*max(c))for c in zip(*a)]]
# task 127: 79 vs 65 bytes for gold, https://arcprize.org/play?task=54d9e175
p=eval('lambda a:[[sum(b"%r0"%a)%5+5'+'for*a,in map(zip,a[:1]+a,a,a[1:]+a)]'*2)
# task 128: 64 bytes, gold, https://arcprize.org/play?task=5521c0d9
p=lambda i:[*zip(*[x[(j:=-x.count(0)):]+x[:j]for x in zip(*i)])]
# task 129: 47 bytes, gold, https://arcprize.org/play?task=5582e5ca
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3
# task 130: 65 bytes, gold, https://arcprize.org/play?task=5614dbcf
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]
# task 131: 125 bytes, gold, https://arcprize.org/play?task=56dc2b01
p=lambda a:[a:=[[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))]for _ in a][3]
# task 132: 108 vs 86 bytes for gold, https://arcprize.org/play?task=56ff96f3
p=lambda i:[i:=[[max({*i[a]}&{*y}|{*y[:a+1]}&{*y[a:]})for a in range(len(i))]for y in zip(*i)]for _ in i][3]
# task 133: 297 (389 unzipped) vs 298 bytes for gold, https://arcprize.org/play?task=57aa92db
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
# task 134: 208 vs 186 bytes for gold, https://arcprize.org/play?task=5ad4f10b
p=lambda i,n=9:(t:=[k[0]for x in i if(k:=[y for y in x if(n*f", {y}")[2:]in"%s"%x!=y>0])])[n*2:]and[[(sum({*sum(i,[])})-y)*(y==t[2])for*s,y in zip(*i,x)if t[2]in s][::n]for x in i if t[2]in x][::n]or p(i,n-1)
# task 135: 32 bytes, gold, https://arcprize.org/play?task=5bd6f4ac
p=lambda a:[b[6:]for b in a[:3]]
# task 136: 113 vs 105 bytes for gold, https://arcprize.org/play?task=5c0a986e
import re
p=lambda m,S=re.sub:eval(eval('S("(?<=(2.{34}){2})0","2",S("0(?=(.{34}1){2})","1",'*9+f'"{m}"'+'))'*9))
# task 137: 141 bytes, gold, https://arcprize.org/play?task=5c2c9af4
def p(a):r=range(len(a));*_,B,C=sorted(map(a.index,a));W=max(a[B]);return[[W>>max(i-B,B-i,abs(a[B].index(W)-j))%(C-B)*9for j in r]for i in r]
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
# task 143: 137 vs 135 bytes for gold, https://arcprize.org/play?task=63613498
p=lambda i,n=1,w=0:any(w==(w:=[*map(len,str(i).split(str(n))[1:-1])])for n in{n,max(i[:3])[0]})*eval(str(i).replace(*f"{n}5"))or p(i,n+1)
# task 144: 59 vs 53 bytes for gold, https://arcprize.org/play?task=6430c8c4
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]
# task 145: 199 vs 191 bytes for gold, https://arcprize.org/play?task=6455b5f5
p=lambda i,k=79,t=0:-k*i or p([[{*0**y*[t:=t+1]}if k>78else[y|(y and e),2*0**(h:=len(y))+(min(s:={*map(len,sum(i,[]))}-{0})==h)*8+h//max(s)][k<1]for y,e in zip(x,x[:1]+x)]for x in zip(*i[::-1])],k-1)
# task 146: 58 bytes, gold, https://arcprize.org/play?task=662c240a
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
# task 147: 83 bytes, gold, https://arcprize.org/play?task=67385a82
p=lambda i:[*eval("map(lambda*x,s=0:[-y%~s%8+(s:=y)for y in x][::-1],*"*4+"i))))")]
# task 148: 148 vs 141 bytes for gold, https://arcprize.org/play?task=673ef223
p=lambda g,*w:[[-v%12&6or(any(r[:j])*any(r[j:])|c)*8for j,v in enumerate(r)]for r in g if(w:=[r]*any(r)+[*w],c:=2in r!=r[0]!=w[-1][0]!=8in w.pop())]
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
# task 153: 153 vs 133 bytes for gold, https://arcprize.org/play?task=681b3aeb
s=' in[a '+'for*a,in map(zip,a[9:]+a,a,a[1:]+a)'*2
p=eval(f'lambda a:max(all(sum(d:=[[*map(int.__xor__,*e)]for*e,in zip(b,c)],a))*d for b{s}]for c{s}])')
# task 154: 122 vs 99 bytes for gold, https://arcprize.org/play?task=6855a6e4
p=lambda g,k=-1:k*g or p([*zip(*[[*[g[k-~k]for k in(1,2,-3,-4)if g[k].count(2)>4],r][0]for r in g if(g:=g[1:]+[r])])],k+1)
# task 155: 18 bytes, gold, https://arcprize.org/play?task=68b16354
p=lambda a:a[::-1]
# task 156: 156 vs 146 bytes for gold, https://arcprize.org/play?task=694f12f3
p=lambda i,r=range(10),S=sum:[[i[a][b]-S(S(t[b-1:b+2])for t in i[a-1:a+2])//36*(S(t:=[*map(S,i)])//S(t[:(h:=t.index(0,1))]*2)+2^(h<a))for b in r]for a in r]
# task 157: 257 (271 unzipped) vs 250 bytes for gold, https://arcprize.org/play?task=6a1e5592
def p(g):
 r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
 for l in range(16+t%15-w):
  for s in 0,1:
   u=*map(list,g),
   for x in u[6:]:
    s+=any(x[t:w])
    for b in range(w-t):u[s][b+l]+=x[b+t]>4;x[b+t]=0
   if k:=p(u):return k
 if{*sum(g[:3],[])}=={1,2}:return g
# task 158: 268 (488 unzipped) vs 269 bytes for gold, https://arcprize.org/play?task=6aa20dc0
def p(g):
 s,t=max((len({*str(a:=[R[x:x+3]for R in g[y:y+3]])}),a)for y in range(len(g))for x in range(len(g[1])))
 for s in range(len(g[1])):
  for y in range(len(g))[:-s*3]:
   for x in range(len(g[1]))[:-s*3]:
    for z in range(len(g[1])):
     t=*zip(*t[::-1]),
     for Y in range(s*3*all(g[y+Y][x+X]==t[Y//s][X//s]or g[y+Y][x+X]==g[1][-1]!=t[Y//s][X//s]==max({*t[1]}-{g[1][-1]})for Y in range(s*3)for X in range(s*3))):
      for X in range(s*3):g[y+Y][x+X]=t[Y//s][X//s]
 return g
# task 159: 110 vs 109 bytes for gold, https://arcprize.org/play?task=6b9890af
p=lambda g,*G:sum([[[2,*r,2]]*(any({*r}-{2})*str(g).count('2')//12or{*r}=={2})for*r,in zip(*G or p(g,*g))],[])
# task 160: 107 vs 105 bytes for gold, https://arcprize.org/play?task=6c434453
import re;p=lambda i,*n:eval(re.sub("1, 1,"+' 1(.{26}), .,'*2,r"0,2,0\1*2,2,2\2*0,2,0*",str(n or p(i,*i))))
# task 161: 83 vs 82 bytes for gold, https://arcprize.org/play?task=6cdd2623
p=lambda m:[[sum({x,i}-{*sum([*zip(*m[1:9])][1:-1],())})for i in m[0]]for*_,x in m]
# task 162: 101 vs 96 bytes for gold, https://arcprize.org/play?task=6cf79266
import re;p=lambda i:[i:=eval(re.sub("0, 0, 0(.{55})?"*3,"1,1,1\%d "*3%(1,2,3),str(i)))for _ in i][2]
# task 163: 136 vs 131 bytes for gold, https://arcprize.org/play?task=6d0160f0
R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]
# task 164: 32 bytes, gold, https://arcprize.org/play?task=6d0aefbc
p=lambda a:[b+b[::-1]for b in a]
# task 165: 136 bytes, gold, https://arcprize.org/play?task=6d58a25d
def p(i):z,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(s in t[:a]!=b in t[t.index(s):])*b for t in zip(*i)]for a,x in enumerate(i)]
# task 166: 65 vs 61 bytes for gold, https://arcprize.org/play?task=6d75e8bb
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]
# task 167: 72 vs 71 bytes for gold, https://arcprize.org/play?task=6e02f1e3
p=lambda i:[[5*(y==x*5%len({*str(i)})%3)for x in(6,5,4)]for y in(0,1,2)]
# task 168: 117 vs 111 bytes for gold, https://arcprize.org/play?task=6e19193c
import re
p=lambda i,k=39:-k*i or[*zip(*eval(re.sub(r"0((.{35})+, ([^0]).{28}\3, \3)",r"\3\1",str(p(i,k-1))))[::-1])]
# task 169: 134 vs 129 bytes for gold, https://arcprize.org/play?task=6e82a1ae
p=lambda i,k=39,t=0:-k*i or[[[y and y|e,-len(y)%5][k>38]if k else{*[t:=t+1]*y}for y,e in zip(x,x[:1]+x)]for x in zip(*p(i,k-1)[::-1])]
# task 170: 220 (226 unzipped) vs 196 bytes for gold, https://arcprize.org/play?task=6ecd11f4
def p(g):e=enumerate;y,x=max((y+1,x+1)for y,r in e(g)for x,c in e(r)if c);s=4-0**g[y-1][x-4];v=-~len(h:=[*filter(max,zip(*filter(max,zip(*g[:y-s]))))])//s;return[[h[Y*v][X*v]and C for X,C in e(R[x-s:x])]for Y,R in e(g[y-s:y])]
# task 171: 51 bytes, gold, https://arcprize.org/play?task=6f8cd79b
p=lambda a:a*all(a[0])or p([*zip(*a[:0:-1],[8]*9)])
# task 172: 20 bytes, gold, https://arcprize.org/play?task=6fa7a44f
p=lambda a:a+a[::-1]
# task 173: 214 (295 unzipped) vs 218 bytes for gold, https://arcprize.org/play?task=72322fa7
p=lambda n:[exec(((r:=[n[y-f//3][t-f%3]for f in range(9)])==r[::-1])*any(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(n[l-f//3][d-f%3]==r[f]for f in range(9))>7)*'for f in range(9):n[l-f//3][d-f%3]=r[f]')for l in range(len(n))for y in range(len(n))for d in range(len(n[0]))for t in range(len(n[0]))]*0+n
# task 174: 97 bytes, gold, https://arcprize.org/play?task=72ca375d
p=lambda g,c=1:((f:=lambda g:[r for r in zip(*g)if c in r])(k:=f(g))==f(k[::-1]))*f(k)or p(g,c+1)
# task 175: 75 bytes, gold, https://arcprize.org/play?task=73251a56
r=range(21);p=lambda g:[[g[A][B]|g[B][A]or g[0][B!=A]for B in r]for A in r]
# task 176: 74 vs 64 bytes for gold, https://arcprize.org/play?task=7447852a
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
# task 182: 187 vs 169 bytes for gold, https://arcprize.org/play?task=776ffc46
def p(g):
 R=F=sum(g,[])
 while C:=[*{*F}][-2]:
  o=F.index(C)-2;N={d for d in range(70)if d%20<6>F[d+o]==C}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g
# task 183: 94 vs 93 bytes for gold, https://arcprize.org/play?task=77fdfe62
def p(g):A=len(g);B=range(2,A-2);return[[g[C][B]%7*g[0-C*2//A][0-B*2//A]for B in B]for C in B]
# task 184: 101 vs 100 bytes for gold, https://arcprize.org/play?task=780d0b14
p=lambda i,k=0,s=[0]*99:[s+0*(s:=[*x])for x in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
# task 185: 162 vs 143 bytes for gold, https://arcprize.org/play?task=7837ac64
p=lambda i:[[1//len(q:={*sum([[t[0]for t in zip(s,*i)if{*t,0}>h][y:y+2]for s in i if{*s,0}>(h:={*i[0]})][x:x+2],[])})*max(q-h|{0})for y in[0,1,2]]for x in[0,1,2]]
# task 186: 66 vs 60 bytes for gold, https://arcprize.org/play?task=794b24be
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
# task 187: 106 vs 92 bytes for gold, https://arcprize.org/play?task=7b6016b9
p=lambda i,k=79:-k*i or[[y*(y!=2)or(z==3)*3or y or 2for y,z in zip(x,[3]+x)]for*x,in zip(*p(i,k-1)[::-1])]
# task 188: 75 vs 61 bytes for gold, https://arcprize.org/play?task=7b7f7511
p=lambda a:[a[:len(a)//2],c:=[b[:len(b)//2]for b in a]][a==[b*2for b in c]]
# task 189: 111 bytes, gold, https://arcprize.org/play?task=7c008303
p=lambda i,r=range(6):[[i[a-6+(s:=i[6][0]%3)*3][b-6+(t:=i[0][6]%3)*3]/3*i[a//3-s][b//3-t]for b in r]for a in r]
# task 190: 108 vs 109 bytes for gold, https://arcprize.org/play?task=7ddcd7ec
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub("0(?=.{34}(.), 0.{31}\\1)","\\1",str(p(i,k-1))))[::-1])]
# task 191: 254 (327 unzipped) vs 241 bytes for gold, https://arcprize.org/play?task=7df24a62
def p(g):
 B=enumerate;A=[[c[0]for c in zip(r,*g)if 1in c]for r in g if 1in r]
 for E in[0,1]*4:g=E*g[::-1]or[*map(list,zip(*g))];[0for C,H in B(g,-1)for D,I in B(g,-1)for F,H in B(A*all(g[C+F][D+G]==I&-2if-1<D+G<23>C+F>-1else I<4for F,H in B(A)for G,I in B(H)))for G,I in B(H)for g[C+F][D+G]in[I]*(-1<D+G<23>C+F>-1)]
 return g
# task 192: 120 vs 110 bytes for gold, https://arcprize.org/play?task=7e0986d6
b,=c,=z=['for*d,c,b,a in zip(b,c,z+a,a[1:]+z,a)]']
p=lambda a:eval('[[[sum({*d}&{b,c}),a][%s.count(a)>30]'%sum(a,a)+b*2)
# task 193: 97 vs 81 bytes for gold, https://arcprize.org/play?task=7f4411dc
import re
p=lambda m,*a:eval(re.sub("(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
# task 194: 74 vs 67 bytes for gold, https://arcprize.org/play?task=7fe24cdd
p=lambda g:(t:=[a+b for*b,a in zip(*g[::-1],g)])+[e[::-1]for e in t[::-1]]
# task 195: 105 bytes, gold, https://arcprize.org/play?task=80af3007
p=lambda a,n=-1:n*[[d&e for d in b for e in c]for b in a for c in a]or p([*filter(any,zip(*a[::3]))],n+1)
# task 196: 112 bytes, gold, https://arcprize.org/play?task=810b9b61
p=lambda i,k=-99:k*i or p([*map(lambda*r,a=-4:[[b%4,b or-4&a,b|2*(a%3<(a:=b))][k//50]for b in r],*i[::-1])],k+1)
# task 197: 54 bytes, gold, https://arcprize.org/play?task=82819916
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]
# task 198: 122 bytes, gold, https://arcprize.org/play?task=83302e8f
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)
# task 199: 102 vs 84 bytes for gold, https://arcprize.org/play?task=834ec97d
p=lambda g,E=enumerate:[[g[A-1][B]+4*any(any(A[B%2::2])for A in g[A:])for B,_ in E(x)]for A,x in E(g)]
# task 200: 93 vs 84 bytes for gold, https://arcprize.org/play?task=8403a5d5
p=lambda g,P=[0]*9:[*zip(*([P*2]*g[9].index(c:=max(g[9]))+[C:=[c]*10,[5]+P,C,P+[5]]*9)[:10])]
# task 201: 208 bytes, gold, https://arcprize.org/play?task=846bdb03
def p(g):j=D=0;P=[];exec("for r in g:V=r[j];F=V==4;P+=[V]*D;D^=F;r[j]*=D|F<1\nj+=1\n"*13+"g[:]=filter(any,zip(*g));"*2);A,*_,B=map(max,*g);E=4,*[0]*len(g[0]),4;return[E,*[[A,*r,B][::A==P[0]or-1]for r in g],E]
# task 202: 106 vs 102 bytes for gold, https://arcprize.org/play?task=855e0971
p=lambda a:[[*map(min,*[c for c in a if max(b)in c])]for b in(len({*a[0],0})<3)*a]or[*zip(*p([*zip(*a)]))]
# task 203: 67 vs 64 bytes for gold, https://arcprize.org/play?task=85c4e7cd
p=lambda i:[[i[g:=len(i)//2][g+i[g].index(y)]for y in x]for x in i]
# task 204: 104 vs 93 bytes for gold, https://arcprize.org/play?task=868de0fa
import re;p=lambda i:eval(re.sub("(?<!1, )1, ([0, ]+)1(?!, 1)",r"1,*[(s:=len([\1]))%2*5+2]*s,1",str(i)))
# task 205: 170 vs 166 bytes for gold, https://arcprize.org/play?task=8731374e
p=lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in range(5**6)if len({*str(s:=[r[y//625:][:10-y//5%5]for r in i[y//25%25:][:10-y%5]])})<7and s[5:]][0]
# task 206: 156 vs 144 bytes for gold, https://arcprize.org/play?task=88a10436
def p(g,E=enumerate):
 r,c=map(min,*[(a,b)for a,x in E(g)for b,y in E(x)if y%5or y>0==(s:=a,t:=b)])
 for i in-1,0,1:g[s+i][t-1:t+2]=g[r-~i][c:c+3]
 return g
# task 207: 81 bytes, gold, https://arcprize.org/play?task=88a62173
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[3:])]'*2)
# task 208: 225 (290 unzipped) vs 215 bytes for gold, https://arcprize.org/play?task=890034e9
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E,D=len(A:=[A for A in zip(*A)if M in A]),len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[1+B:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g
# task 209: 290 (429 unzipped) vs 289 bytes for gold, https://arcprize.org/play?task=8a004b2b
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
# task 212: 117 vs 105 bytes for gold, https://arcprize.org/play?task=8d510a79
p=lambda i,k=39:-k*i or[[x[b]or 5in x[:b]and 2-x[b-1]%5&1-x[b+(b<9)]for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
# task 213: 109 vs 92 bytes for gold, https://arcprize.org/play?task=8e1813be
p=lambda i:len({*i[-1]})<=(n:=len({*i[0]}))>2and~-n*[[*filter(int,i[0])]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
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
# task 219: 278 (325 unzipped) vs 267 bytes for gold, https://arcprize.org/play?task=90f3ed37
def p(i,n=0,k=0):
 t=2;f=len(r:=[x[k:]for x in i if(t:=~any(x)%3%-~t)*any(x)])
 for l in range(3,len(i)-f):
  for x in range(all(sum(q:=[[0**i+r*(i!=1)for i,r in zip(i[n:],r)]for i,r in zip(i[l:],r)],[sum([9in x[:2]for x in q]+i[l-1])<1]))*(len(i[0])-n-k)*f):i[l+x%f][x//f+n]=(-q[x%f][x//f]&9)%9
 return k*i or p(i,-~n%3,n>1)
# task 220: 93 vs 87 bytes for gold, https://arcprize.org/play?task=913fb3ed
p=lambda i:[*eval("map(lambda*x,s=0:[[-(s*2^s-7)%7,s:=y][y>0]for y in x][::-1],*"*4+"i))))")]
# task 221: 87 bytes, gold, https://arcprize.org/play?task=91413438
def p(i):j=str(i).count("0");a=2;return[(q*(9-(a:=a+1)//3*j)+[0]*21)[:j*3]for q in i*j]
# task 222: 103 bytes, gold, https://arcprize.org/play?task=91714a58
p=lambda g:[g:=[[c*(2*f"{c}, "in"%s"%r)*(sum(g,g).count(c)>4)for c in r]for*r,in zip(*g)]for _ in g][5]
# task 223: 46 vs 51 bytes for gold, https://arcprize.org/play?task=9172f3a0
p=lambda a:a>a*0!=0and[p(a[0])]*3+p(a[1:])or a
# task 224: 171 bytes, gold, https://arcprize.org/play?task=928ad970
p=lambda i,k=3,s=0:-k*i or p([[y or(s==5in{*(h:=[*map(max,i)])[b+1:]}&{*h[:b]})*sum({*sum(i,[])},-5)for b,y in enumerate(x)]*1**(s:=s*2+max(x))for x in zip(*i)][::-1],k-1)
# task 225: 132 bytes, gold, https://arcprize.org/play?task=93b581b8
p=lambda i,r=range(6):[[max([s for t in i[a-3:a]+i[a+3:a:-1]for s in t[b-3:b]+t[b+3:b:-1]if s][:-3]+[i[a][b]])for b in r]for a in r]
# task 226: 159 vs 139 bytes for gold, https://arcprize.org/play?task=941d9a10
p=lambda i,e=enumerate,s=sum:[[y or(s(x[:b])*2==s(x))*(s(k:=[*map(min,i)])==s(k[:a])*2)*2+0**s(x[b:]+k[a:])*3+0**s(x[:b]+k[:a])for b,y in e(x)]for a,x in e(i)]
# task 227: 55 vs 52 bytes for gold, https://arcprize.org/play?task=94f9d214
p=lambda a:[[~b.pop(0)+c&2for c in a.pop(4)]for b in a]
# task 228: 119 bytes, gold, https://arcprize.org/play?task=952a094c
import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'([^0])((, (?!\1|0).).*0\3.{28})0',r'0\2\1',str(p(a,n+1)[::-1]))))]
# task 229: 73 bytes, gold, https://arcprize.org/play?task=9565186b
p=lambda a:[[[5,c][c==max(d:=sum(a,a),key=d.count)]for c in b]for b in a]
# task 230: 114 bytes, gold, https://arcprize.org/play?task=95990924
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub(f"0(?=, 0.{ {len(m)*3}}.5, 5)","3**i%5",str(p(m,i-1))))[::-1])]
# task 231: 43 bytes, gold, https://arcprize.org/play?task=963e52fc
p=lambda a:[(r[:6]*4)[:len(r)*2]for r in a]
# task 232: 61 vs 58 bytes for gold, https://arcprize.org/play?task=97999447
p=lambda i:[(e:=0)or[(e:=y-e)>>9&5or e for y in x]for x in i]
# task 233: 298 (394 unzipped) vs 297 bytes for gold, https://arcprize.org/play?task=97a05b5b
e=enumerate
def p(g):
 for G in[g]*60:*g,=map(list,zip(*g[max(map(len,str(g[0]).split('0')))<12:][::-1]))
 for s in [[v[x:x+3]for v in G[y:y+3]]for y,p in e(G[2:])for x,p in e(p[2:])][::-1]*4:
  for y,p in e(g*({*sum(s,s[0])}^{0}>{2,0})):
   for x,p in e(p):
    for n,p in e(s*all((2*(2*g)[n+y])[m+x]==2*(2!=p)for n,p in e(s)for m,p in e(p))):g[n+y][x:x+3],*s=p,
  s[:]=zip(*s[::-1])
 return g
# task 234: 120 vs 118 bytes for gold, https://arcprize.org/play?task=98cf29f8
p=lambda i,k=3,h={0}:-k*i or p([*zip(*([x for x in i if len(h:=h|{*x})-3+sum(x)-max(x)]+i[-1:]*99)[:len(i)])][::-1],k-1)
# task 235: 62 bytes, gold, https://arcprize.org/play?task=995c5fa3
p=lambda g:[[g[1][x]*sum(g[2][x:x+3])%13^8]*3for x in[1,6,11]]
# task 236: 61 vs 54 bytes for gold, https://arcprize.org/play?task=99b1bc43
p=lambda a:[[3*c^-b.pop(0)%5for c in a.pop(0)]for b in a[5:]]
# task 237: 67 bytes, gold, https://arcprize.org/play?task=99fa7670
p=lambda a,c=0:[(b:=0)or[c:=(b:=b or d)for d in r+[c]]for*r,_ in a]
# task 238: 223 (282 unzipped) bytes, gold, https://arcprize.org/play?task=9aec4887
def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and((k:=l[a-1][b-1])and m[1-(b>a<len(m)-1-b)|-(b<a>len(m)-1-b)][1-(b<a<len(m)-1-b)|-(b>a>len(m)-1-b)]or k)or m[a][b]for b in range(len(m))]for a in range(len(m))]
# task 239: 99 bytes, gold, https://arcprize.org/play?task=9af7a82c
p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted([c:=-b.count(e)]+[e]*-c+[0]*11for e in{*b})))][2:]
# task 240: 105 vs 99 bytes for gold, https://arcprize.org/play?task=9d9215db
p=lambda i,r=range(19):[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]for b in r]for a in r]for _ in r][4]
# task 241: 21 bytes, gold, https://arcprize.org/play?task=9dfd6313
p=lambda a:[*zip(*a)]
# task 242: 54 bytes, gold, https://arcprize.org/play?task=9ecd008a
p=lambda g:[r[~r.index(0)::-1][:3]for r in g if 0in r]
# task 243: 79 bytes, gold, https://arcprize.org/play?task=9edfc990
p=lambda a,n=-79:a*n or[*zip(*eval(str(p(a,n+1)[::-1]).replace('1, 0','1,1')))]
# task 244: 64 bytes, gold, https://arcprize.org/play?task=9f236235
p=lambda a,n=1:[b[::~n]for b in(a[n]!=a[0])*a][::1+n]or p(a,n+1)
# task 245: 108 vs 106 bytes for gold, https://arcprize.org/play?task=a1570a43
p=lambda i,k=7:-k*i or p([*map(lambda*r,w=0:[[v,w%3][(w:=v)<=2in{*max(i,key=any)}&{*r}]for v in r],*i)],k-1)
# task 246: 126 vs 105 bytes for gold, https://arcprize.org/play?task=a2fd1cf0
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k+2in x)*8for y in x],*i)],k-1)
# task 247: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a3325580
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]
# task 248: 79 vs 72 bytes for gold, https://arcprize.org/play?task=a3df8b1e
def p(g,A=0,C=-1):
 for x in g[::-1]:x[A]=1;C*=-(A%~-len(x)<1)|1;A+=C
 return g
# task 249: 26 bytes, gold, https://arcprize.org/play?task=a416b8f3
p=lambda a:[r*2for r in a]
# task 250: 125 vs 119 bytes for gold, https://arcprize.org/play?task=a48eeaf7
import re
p=lambda i:[i:=eval(re.sub("5(((.{34}0)+)(.{32})|([0, ]+)), 2",r"0\2\5+5\4,2",str([*zip(*i[::-1])])))for _ in i][7]
# task 251: 94 vs 89 bytes for gold, https://arcprize.org/play?task=a5313dff
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]
# task 252: 61 vs 57 bytes for gold, https://arcprize.org/play?task=a5f85a15
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]
# task 253: 144 vs 129 bytes for gold, https://arcprize.org/play?task=a61ba2ce
def p(g):f=sum(g,[]);k=f*99;i=0;return[[max(v*(k[(i:=i+1)-j%5]==k[i+12-j%3*13]==v)for v in f)for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]
# task 254: 103 vs 84 bytes for gold, https://arcprize.org/play?task=a61f2674
def p(i):k=*map(sum,zip(*i)),;return[[y and s//max(k)+min({*k}-{0})//s*2for y,s in zip(x,k)]for x in i]
# task 255: 244 (276 unzipped) vs 243 bytes for gold, https://arcprize.org/play?task=a64e4611
def p(g):
 for S in[{0,3}]*8:g=[[r[~x]+10*any({*s[-2%(30-x):31-x]}-S for s in g[y+y%~y:y+2])for y,r in enumerate(g)]for x,_ in enumerate(g)];g=[[v%10|3*({*r[:10]}<=S)*(len(w:=[r[x]for r in g if{*r[:10]}<=S])>3!=S>={*w}or 3in r[x:])for x,v in enumerate(r)]for r in g]
 return g
# task 256: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a65b410d
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
# task 257: 75 vs 74 bytes for gold, https://arcprize.org/play?task=a68b268e
p=eval('lambda a:[[max(sum(a,()),key=bool)'+'for*a,in map(zip,a,a[5:])]'*2)
# task 258: 61 bytes, gold, https://arcprize.org/play?task=a699fb00
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))
# task 259: 85 bytes, gold, https://arcprize.org/play?task=a740d043
p=lambda i,k=39:-k*i or p([*zip(*eval(str(i).replace(*"10"))[any(i[-1])-2::-1])],k-1)
# task 260: 150 vs 135 bytes for gold, https://arcprize.org/play?task=a78176bb
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
# task 265: 131 vs 104 bytes for gold, https://arcprize.org/play?task=a8d7556c
import re;p=lambda g,i=2:eval(max(g:=re.sub("[02], [02](.{52})[02], [0i]","i, 2\g<1>2, 2",str(g))for _ in-~hash((*g[0],))%881*[0]))
# task 266: 103 vs 102 bytes for gold, https://arcprize.org/play?task=a9f96cdd
p=lambda g:[([0,0,0,r%9,0,r//9]*2)[4-max(g).index(2):][:5]for r in b'\09\0G\0'[2-g.index(max(g)):][:3]]
# task 267: 52 vs 46 bytes for gold, https://arcprize.org/play?task=aabf363d
p=lambda i:[[i[-y>>8][x==i[6]]for y in x]for x in i]
# task 268: 238 (253 unzipped) vs 239 bytes for gold, https://arcprize.org/play?task=aba27056
def p(g):
 l=range(len(g));(J,E),*B,(C,F)=[[A,D]for A in l for D in l if g[A][D]]
 if g[C][F-2]<1:
  for A in l[J+1:]:
   for D in({*l[E+2:F-1],F+A-C-2,E-A+C+2}&{*l},l[E+1:F])[A<C]:g[A][D]=4
  return g
 return[*zip(*p([*map(list,zip(*g[::-1]))]))][::-1]
# task 269: 64 vs 63 bytes for gold, https://arcprize.org/play?task=ac0a08a4
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 270: 117 bytes, gold, https://arcprize.org/play?task=ae3edfdc
import re;p=lambda i,k=7:-k*i or eval(re.sub(f"({k|3})([^)]*)0(, {2-k//4})",r"0\2\1\3",str([*zip(*p(i,k-1)[::-1])])))
# task 271: 86 bytes, gold, https://arcprize.org/play?task=ae4f1146
p=eval(f"lambda a:max([str(a).count('1'),a]{'for*a,in map(zip,a,a[1:],a[2:])'*2})[1]")
# task 272: 95 vs 89 bytes for gold, https://arcprize.org/play?task=aedd82e4
p=lambda a,n=7:-n*a or[*map(lambda*b,d=0:[2*(d*(d:=c)>0)or c-(c>n)for c in b][::-1],*p(a,n-1))]
# task 273: 116 bytes, gold, https://arcprize.org/play?task=af902bf9
R=range(10)
p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in{*R}-{i}for J in{*R}-{j}})//5*2for j in R]for i in R]
# task 274: 75 vs 71 bytes for gold, https://arcprize.org/play?task=b0c4d837
p=lambda i:[(h:=[8]*sum({*x}=={0,5}for x in i)+[0]*5)[1:4],h[6:3:-1],[0]*3]
# task 275: 136 bytes, gold, https://arcprize.org/play?task=b190f7f5
p=lambda i:"8"in"%s"%i[(u:=len(i[0])):]and[[t*y/8for t in s for y in x]for s in i[:u]for x in i[u:]]or[*zip(*p([*zip(*i[::-1])]))][::-1]
# task 276: 38 bytes, gold, https://arcprize.org/play?task=b1948b0a
p=lambda a:eval(str(a).replace(*'62'))
# task 277: 199 vs 194 bytes for gold, https://arcprize.org/play?task=b230c067
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
# task 278: 119 vs 118 bytes for gold, https://arcprize.org/play?task=b27ca6d3
import re;p=lambda i:[i:=eval(re.sub(f"0(?=(.{ {len(i)*3-5}}.{{,9}}|..)2, 2)","3",str([*zip(*i[::-1])])))for _ in i][3]
# task 279: 113 vs 107 bytes for gold, https://arcprize.org/play?task=b2862040
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=0:[[b+7*(a>1==b),b%(9+a),(a:=b)or 9][f>>6]for b in r],*g[::-1])],f-1)
# task 280: 182 vs 179 bytes for gold, https://arcprize.org/play?task=b527c5c6
def p(a,n=3,i=0):
	for b in a:
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):(i:=i+1)+d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
# task 281: 145 bytes, gold, https://arcprize.org/play?task=b548a754
import re
p=lambda i,k=39:-k*i or p(eval(re.sub("(\((?=[^)]+[1-9])[^)]+., )(\([^)]+.), \((?=.*8)[08, ]+\)",r"\1\1\2",str([*zip(*i[::-1])]))),k-1)
# task 282: 83 bytes, gold, https://arcprize.org/play?task=b60334d2
p=lambda a:[*map(f:=lambda d,*b,c=0:[c|(c:=d)>>2|(d:=e)for e in[*b,0]],*map(f,*a))]
# task 283: 94 vs 82 bytes for gold, https://arcprize.org/play?task=b6afb2da
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]
# task 284: 228 vs 220 bytes for gold, https://arcprize.org/play?task=b7249182
def p(i):
 for E in[enumerate]*2:
  *i,=zip(*i);m=max(i)
  if len(l:=[n for n,y in E(m)if y])==2:s,t=l;i=[[([*(t-s-2)//2*[1],7,4,*[0]*4][min(t-b,b-s)]>>abs(a-i.index(m))&1)*m[l[t-b<b-s]]for b,_ in E(x)]for a,x in E(i)]
 return i
# task 285: 302 (426 unzipped) vs 288 bytes for gold, https://arcprize.org/play?task=b775ac94
def p(g):
 for E in range(8):
  I=[]
  for A,r in enumerate(g):
   for B,F in enumerate(r):
    G={(A,B)}
    for D in I[:F*5]:
     if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
    I+=[G][:F]
  for G in I:
   for A,B in G:
    for E in range(8):
     for F in range(8):
      if{(A-F,B-~E),(A-~F,B-E)}&{*G}:g[A-F][B-E]|=len({*str([x[B:B+2]for x in g[A:A+2]])})//8*g[A][B]
  *g,=map(list,zip(*g[::-1]))
 return g
# task 286: 111 vs 109 bytes for gold, https://arcprize.org/play?task=b782dc8a
p=lambda i,k=43:-k*i or[*map(lambda*x,t=0:[t:=y or([0,*{*sum(i,[])}-{y,t,8}]*2)[3]for y in x],*p(i,k-1)[::-1])]
# task 287: 63 vs 56 bytes for gold, https://arcprize.org/play?task=b8825c91
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]
# task 288: 112 vs 89 bytes for gold, https://arcprize.org/play?task=b8cdaf2b
p=lambda i,e=enumerate:[[y or i[-1][t:=len(i)//2]*(a+abs(b-t)==t*2-0**i[-2][-t])for b,y in e(x)]for a,x in e(i)]
# task 289: 64 vs 63 bytes for gold, https://arcprize.org/play?task=b91ae062
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 290: 69 vs 67 bytes for gold, https://arcprize.org/play?task=b94a9452
p=lambda i:[[sum({*sum(i,x)},-y)for y in x if y]for x in i if any(x)]
# task 291: 62 vs 61 bytes for gold, https://arcprize.org/play?task=b9b7f026
p=lambda i,n=1:len({x.count(n)for x in i})//3*[[n]]or p(i,n+1)
# task 292: 57 vs 56 bytes for gold, https://arcprize.org/play?task=ba26e723
p=lambda g:[[j*v//4for j,v in zip(b''*7,r)]for r in g]
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
# task 306: 75 vs 71 bytes for gold, https://arcprize.org/play?task=c444b776
p=lambda i,k=7:-k*i or[[*map(max,x,[0]*10+x)]for*x,in zip(*p(i,k-1))][::-1]
# task 307: 46 vs 50 bytes for gold, https://arcprize.org/play?task=c59eb873
p=lambda a:a>a*0!=0and[p(a[0])]*2+p(a[1:])or a
# task 308: 243 (253 unzipped) vs 226 bytes for gold, https://arcprize.org/play?task=c8cbb738
def p(g):
 A=[9*[M:=max(E:=sum(g,[]),key=E.count)]for(A)in g]
 for N in{*E}-{M}:
  (F,G),*B,(P,Q)=C=[[A,C]for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==N];B=max(P-F,Q-G)+1
  for(J,K)in C:A[J*2-F+B-P>>1][K*2-G+B-Q>>1]=N
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
# task 317: 43 vs 59 bytes for gold, https://arcprize.org/play?task=ce22a75a
p=lambda a:a==5or a and[p(a[1])]*3+p(a[3:])
# task 318: 60 vs 54 bytes for gold, https://arcprize.org/play?task=ce4f8723
p=lambda i:[[any(y)*3for y in zip(*x)]for x in zip(i,i[5:])]
# task 319: 242 (293 unzipped) vs 194 bytes for gold, https://arcprize.org/play?task=ce602527
def p(a):g=max(f:=sum(A:=a,[]),key=f.count);return[[[[g,d][d==e]for*b,d in zip(*a,b)if e in b]for b in a if e in b]for e in{*f}for i in range(2652)if[]<(b:=[a for a,A in zip(a,sum(zip(A,A),((),)*19)[i%51:])for a,A in zip(a,sum(zip(A,A),((),)*19)[i%52:])if a!=A==e!=g])==b[:1]*f.count(b[0])][0]
# task 320: 72 vs 68 bytes for gold, https://arcprize.org/play?task=ce9e57f2
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]
# task 321: 57 vs 55 bytes for gold, https://arcprize.org/play?task=cf98881b
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
# task 322: 48 bytes, gold, https://arcprize.org/play?task=d037b0a7
p=lambda a:[[*map(max,*a[:n]*2)]for n in(1,2,3)]
# task 323: 125 vs 102 bytes for gold, https://arcprize.org/play?task=d06dbe63
p=lambda i,r=range(13):[[i[a][b]|5*(abs((y:=a-(n:=sum(i,[]).index(8))//13)-n%13-~b-(y>0)*2)<2-y%2>0!=y)for b in r]for a in r]
# task 324: 261 (313 unzipped) vs 259 bytes for gold, https://arcprize.org/play?task=d07ae81c
def p(g):s=sum(g,[]);k,K,b,B=sorted({*s},key=s.count);b=[b,B][any({*r}in({k,B},{K,b})for r in[*zip(*g)]+g)];[0for y,r in enumerate(eval(str(g)))for x,c in enumerate(r)for z,s in enumerate(g)for Y in(-z,z)for X in(-z,z)if c in{k,K}!=len(g)>Y+y>-1<X+x<len(g[0])for g[Y+y][X+x]in[[K,k][g[Y+y][X+x]in(b,k)]]];return g
# task 325: 172 vs 160 bytes for gold, https://arcprize.org/play?task=d0f5fe59
p=lambda i,k=39,z=0:-k*[x*[0]+[8]+(z+~x)*[0]for x in range(z)]or p([(s:=1)*[(k<39)*max(h and s,s:=h)or(z:=z+1)*h for h in x]for x in zip(*i[::-1])],k-1,len({*sum(i,[])})-1)
# task 326: 30 bytes, gold, https://arcprize.org/play?task=d10ecb37
p=lambda a:[a[0][:2],a[1][:2]]
# task 327: 67 bytes, gold, https://arcprize.org/play?task=d13f3404
p=lambda i,l=[0]*3:[l:=[*map(max,x+[0]*3,[0]+l*2)]for x in i+[l]*3]
# task 328: 173 vs 163 bytes for gold, https://arcprize.org/play?task=d22278a0
def p(g):R=range(len(g));return[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*v)for x in R for y in R if(v:=g[x][y])))and(D[0][0]<D[1][0])*D[0][1]for c in R]for r in R]
# task 329: 54 bytes, gold, https://arcprize.org/play?task=d23f8c26
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]
# task 330: 135 vs 134 bytes for gold, https://arcprize.org/play?task=d2abd087
p=lambda i,k=179:-k*i or p([[[k>78and 1<<4*(k:=k-1)or e|y,118%~(y%15)%3][k<1]*(y>0)for y,e in zip(x,[0]+x)]for*x,in zip(*i[::-1])],k-1)
# task 331: 84 vs 83 bytes for gold, https://arcprize.org/play?task=d364b489
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, ","1,86//k%1")),k-2)
# task 332: 61 vs 58 bytes for gold, https://arcprize.org/play?task=d406998b
p=lambda m:[[len(r)*r.pop(0)%2*3or x for x in[*r]]for r in m]
# task 333: 89 bytes, gold, https://arcprize.org/play?task=d43fd935
p=lambda a,n=-3:n*a or[(d:=0)or[d:=b.pop()or d*(3in b)for _ in a]for*b,in zip(*p(a,n+1))]
# task 334: 75 vs 66 bytes for gold, https://arcprize.org/play?task=d4469b4b
p=lambda i:[[((x|y)>>sum({*sum(i,[])})&1)*5for y in[0,6,8]]for x in[4,2,8]]
# task 335: 128 vs 107 bytes for gold, https://arcprize.org/play?task=d4a91cb9
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=0:[y|(any(sum(i[b:],[]))*any(sum(i[:(b:=b+1)],[]))>y<k*6+2in x)*4for y in x],*i)],k-1)
# task 336: 105 vs 93 bytes for gold, https://arcprize.org/play?task=d4f3cd78
p=lambda i,k=3:-k*i or[[x[b]or(sum(x[:b])%8|1in x[:4])*8for b in range(10)]for x in zip(*p(i,k-1)[::-1])]
# task 337: 46 bytes, gold, https://arcprize.org/play?task=d511f180
p=lambda g:[[x^84%x%3*13for x in r]for r in g]
# task 338: 71 vs 64 bytes for gold, https://arcprize.org/play?task=d5d6de2d
p=lambda i,s=0:[[~y%~(s:=y-s>>t&2)%4for y,t in zip(x,[0]+x)]for x in i]
# task 339: 37 bytes, gold, https://arcprize.org/play?task=d631b094
p=lambda a:[[*filter(int,sum(a,[]))]]
# task 340: 122 vs 119 bytes for gold, https://arcprize.org/play?task=d687bc17
p=lambda i,k=3:-k*i or[*map(lambda s,t,*x:[y*(sum(i,i).count(y)>3>0<y!=s)for y in x[::-1]]+[sum({*x}&{s,t}),s],*p(i,k-1))]
# task 341: 137 vs 132 bytes for gold, https://arcprize.org/play?task=d6ad076f
p=lambda i,r=range(10):[i:=[[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a+a%~a:a+2])*8for b in r]for a in r]for _ in i][1]
# task 342: 119 vs 111 bytes for gold, https://arcprize.org/play?task=d89b689b
p=lambda i,s=-1:[[y==8and[g for g in[*map(max,*i[:a]),*map(max,*i[a:])]if g%8][s:=s+1]for y in i[a]]for a in range(10)]
# task 343: 75 vs 65 bytes for gold, https://arcprize.org/play?task=d8c310e9
p=lambda i:[*zip(*((h:=[*zip(*i)])[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15])]
# task 344: 78 bytes, gold, https://arcprize.org/play?task=d90796e8
p=lambda i,k=3:-k*i or[*zip(*eval(str(p(i,k-1)[::-1]).replace("2, 3","0,8")))]
# task 345: 108 vs 90 bytes for gold, https://arcprize.org/play?task=d9f24cd1
p=lambda i,r=range(10):[[i[a][b]|2&6%~sum((t:=[*zip(*i)])[b-1][a+a%~a:])+max(t[b][a:])for b in r]for a in r]
# task 346: 68 vs 58 bytes for gold, https://arcprize.org/play?task=d9fac9be
p=lambda i:[max([n]for n in sum(i,[])if str(i).count(f"{n}, "*3)<2)]
# task 347: 50 bytes, gold, https://arcprize.org/play?task=dae9d2b5
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]
# task 348: 94 bytes, gold, https://arcprize.org/play?task=db3e9e38
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,in a[1:]]+a,n+1)
# task 349: 237 (261 unzipped) vs 214 bytes for gold, https://arcprize.org/play?task=db93a21d
p=lambda i,n=6,l=0,R=range:-n*i or[[i:=[[(i[x][y]>1)*i[x][y]or(a<=x+n<a+n*4)*(b<=y+n<b+n*4)*3or 9in[*zip(*i[:x+1])][y]for y in R(l)]for x in R(l)]for a in R(-n*2,l)for b in R(l-n*2+1)if{min(x[max(b,0):b+n*2])for x in i[max(a,0):a+n*2]}=={9}]]and p(i,n-1,len(i))
# task 350: 96 vs 91 bytes for gold, https://arcprize.org/play?task=dbc1a6ce
p=lambda i,*n:[[y or(1in x[b:]!=1in x[:b])*8for b,y in enumerate(x)]for x in zip(*n or p(i,*i))]
# task 351: 68 vs 67 bytes for gold, https://arcprize.org/play?task=dc0a314f
p=lambda i:[s[~x.index(3)::-1][:5]for x,s in zip(i,i[::-1])if 3in x]
# task 352: 84 bytes, gold, https://arcprize.org/play?task=dc1df850
p=lambda i:[*eval("map(lambda*x,t=0:[max(0<t<3,t:=y)for y in x][::-1],*"*4+"i))))")]
# task 353: 104 vs 92 bytes for gold, https://arcprize.org/play?task=dc433765
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)
# task 354: 99 vs 96 bytes for gold, https://arcprize.org/play?task=ddf7fa4f
p=lambda i:[i:=[[(y==5)*(c[0]or s)or y for*c,y,s in zip(*i,x,[0]+x)][::-1]for x in i]for x in i][9]
# task 355: 101 vs 98 bytes for gold, https://arcprize.org/play?task=de1cd16c
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]
# task 356: 105 bytes, gold, https://arcprize.org/play?task=ded97339
p=lambda i,r=range(10):[[max({*i[a][b:]}&{*i[a][:b+1]}|{*c[a:]}&{*c[:a]})for*c,b in zip(*i,r)]for a in r]
# task 357: 90 vs 86 bytes for gold, https://arcprize.org/play?task=e179c5f4
p=lambda m,x=1,d=1:m and p(m,x:=x-d,x%(l:=len(m.pop())-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]
# task 358: 97 bytes, gold, https://arcprize.org/play?task=e21d9049
p=lambda i,k=39:-k*i or[[*map(max,x,x[6-13//len({*x,0}):]+(0,0)*9)]for x in zip(*p(i,k-1)[::-1])]
# task 359: 64 bytes, gold, https://arcprize.org/play?task=e26a3af2
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]
# task 360: 45 bytes, gold, https://arcprize.org/play?task=e3497940
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]
# task 361: 193 (245 unzipped) bytes, gold, https://arcprize.org/play?task=e40b9e2f
def p(a):I=[a*2for a in a+a];return[[[max(I[x][y],I[a+b+n+~y][b-a+x],I[a-b+y][a+b+n+~x],I[a+a+n+~x][b+b+n+~y])for y in range(10)]for x in range(10)]for n in range(10)for a in range(10)for b in range(10)if all(all(x[b:b+n])for x in I[a:a+n])][-1]
# task 362: 69 bytes, gold, https://arcprize.org/play?task=e48d4e1a
p=lambda g:[r[(n:=g.count(g[0])):9]+r[:1]+r[:n]for r in g*2][10-n:-n]
# task 363: 228 vs 213 bytes for gold, https://arcprize.org/play?task=e5062a87
E=enumerate
def p(g):
 z,v,V=[{(y,x)for y,r in E(g)for x,c in E(r)if c==C}for C in(0,2,5)];i,j=min(v)
 for y,x in z|V:
  for Y,X in(m:=[(Y-i+y,X-j+x)for Y,X in v])*(hash((*g[0],))%263+y!=7!={*m}<z):g[Y][X]=2;z-={(Y,X)}
 return g
# task 364: 155 bytes, gold, https://arcprize.org/play?task=e509e548
p=lambda i,k=39:-k*i or p([[[y.bit_count()*5%14%9,y and(u*t>0)<<k%4+2|y|u][k>0]for y,t,u in zip(x,[0]+x,s)]for*x,s in zip(*i,[[0]*99,*zip(*i)])][::-1],k-1)
# task 365: 128 vs 111 bytes for gold, https://arcprize.org/play?task=e50d258f
p=lambda i:max((-(r:=str(p:=[x[a%9:10-a//9%9]for x in i[a//81%9:10-a//729]]).count)("0"),*map(r,"21"),p)for a in range(9**4))[3]
# task 366: 364 (604 unzipped) vs 365 bytes for gold, https://arcprize.org/play?task=e6721834
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
# task 367: 129 bytes, gold, https://arcprize.org/play?task=e73095fd
import re
p=lambda g,k=-23:k*g or p(eval(re.sub(f"(0.{(N:={len(g)*3-2})}0, 5, 5.{N}5,|4,) 0","\\1 4",str([*zip(*g)][::-1]))),k+1)
# task 368: 138 bytes, gold, https://arcprize.org/play?task=e76a88a6
import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m,q=[re.findall("([^50](, [1-9])+)",str(i)*9)for _ in i]:q[m.end()%8].pop(0)[0],str(i)))
# task 369: 114 vs 113 bytes for gold, https://arcprize.org/play?task=e8593010
p=lambda m,i=95:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("2320,,,,    133"[i%5::4],"1213,,,,121"[i%5::4])))]
# task 370: 268 (357 unzipped) vs 269 bytes for gold, https://arcprize.org/play?task=e8dc4411
def p(g,k=3):
 y,*t=[y for y,r in enumerate(g)if 0in r];x,*t=[y for y,r in enumerate(zip(*g))if 0in r];V=g[y][x];v=V>0
 for s in range(10):
  for i in range(len(t)+1):
   for j in range(len(t)+1):
    a,b=y-i-s*(len(t)+1-v)+v-1,x-j-s*(len(t)+1-v)+v-1
    if-g[y+i][x+j]>-1<a>-1<b:g[a][b]=g[y-1+V//8][x-1+V%8]
 return-k*g or p([*map(list,zip(*g))][::-1],k-1)
# task 371: 109 bytes, gold, https://arcprize.org/play?task=e9614598
def p(a):
 for i in[l:=len(a[0]),-l,1,0,-1]:b=sum(a,[]).index;i+=b(1,b(1)+1)+b(1)>>1;a[i//l][i%l]=3
 return a
# task 372: 48 bytes, gold, https://arcprize.org/play?task=e98196ab
p=lambda a:[b for*b,in map(map,[max]*5,a,a[6:])]
# task 373: 39 bytes, gold, https://arcprize.org/play?task=e9afcf9a
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]
# task 374: 112 bytes, gold, https://arcprize.org/play?task=ea32f347
p=lambda g,i=2,l=39:-l*g or p([*zip(*(a:=eval(str(g).replace(l//4*"5, ",l//4*f"{i*3%5},"))))][::-1],i+(g>a),l-1)
# task 375: 53 bytes, gold, https://arcprize.org/play?task=ea786f4a
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g
# task 376: 30 bytes, gold, https://arcprize.org/play?task=eb281b96
p=lambda a:(a+a[1:-1])*2+a[:1]
# task 377: 57 vs 55 bytes for gold, https://arcprize.org/play?task=eb5a1d5d
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]
# task 378: 144 vs 143 bytes for gold, https://arcprize.org/play?task=ec883f72
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(f"0(?=({(s:=f'.{ {3*len(i)+1}}0')}, 0)*{s}, ., [^0]{s*2}, (.))","\\2",str(p(i,k-1)))))][::-1]
# task 379: 141 bytes, gold, https://arcprize.org/play?task=ecdecbb3
import re
p=lambda i,k=7,r=re.sub:-k*i or[*zip(*eval(r(", 4, ","|8,8,8|",r("0, 8, ((0, )+)2","4,2,4,*[2]*len([\\1])",str(p(i,k-1)[::-1])))))]
# task 380: 27 bytes, gold, https://arcprize.org/play?task=ed36ccf7
p=lambda a:[*zip(*a)][::-1]
# task 381: 91 vs 79 bytes for gold, https://arcprize.org/play?task=ef135b50
p=lambda i,E=enumerate:[[y or(a%9>0<2in{*x[b:]}&{*x[:b]})*9for b,y in E(x)]for a,x in E(i)]
# task 382: 144 vs 134 bytes for gold, https://arcprize.org/play?task=f15e1fac
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a:[a:=[b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]]for _ in a][3]
# task 383: 121 bytes, gold, https://arcprize.org/play?task=f1cefba8
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]
# task 384: 62 bytes, gold, https://arcprize.org/play?task=f25fbde4
p=lambda a,*n:sum([[b,b]for*b,in zip(*n or p(*a))if 4in b],[])
# task 385: 25 bytes, gold, https://arcprize.org/play?task=f25ffba3
p=lambda a:a[:4:-1]+a[5:]
# task 386: 52 bytes, gold, https://arcprize.org/play?task=f2829549
p=lambda a:[[3>>e+r.pop(0)for e in r[4:]]for r in a]
# task 387: 228 (238 unzipped) vs 218 bytes for gold, https://arcprize.org/play?task=f35d900a
p=lambda i,k=3:-k*i or p([[(y<1>k)*([*{*sum(i,[])}-{*sum([*zip(*i[b-(b>0):b+2])][a-(a>0):a+2],()),5},0]*2)[2]+(sum(x[b+1:])%5>0<sum(x[:b])%5>x[b-1]+x[b+1]==0<x[b-2]+x[b+2])*5or y for b,y in enumerate(x)]for a,x in enumerate(zip(*i))],k-1)
# task 388: 62 vs 61 bytes for gold, https://arcprize.org/play?task=f5b8619d
p=lambda a:2*[2*[d or any(c)*8for*c,d in zip(*a,b)]for b in a]
# task 389: 57 bytes, gold, https://arcprize.org/play?task=f76d97a5
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]
# task 390: 121 vs 99 bytes for gold, https://arcprize.org/play?task=f8a8fe49
p=lambda g:[g:=[*zip(*[[*[g[k-~k]for k in(1,2,-3,-4)if g[k].count(2)>4],r][0]for r in g if(g:=g[1:]+[r])])]for _ in g][1]
# task 391: 63 bytes, gold, https://arcprize.org/play?task=f8b3ba0a
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]
# task 392: 157 vs 149 bytes for gold, https://arcprize.org/play?task=f8c80d96
p=lambda n,r=range(10):[[(a:=max(max(n)),5,5)[min(max(abs(f-b),abs(m-s))for b in r for s in r if n[b][s])%(3-(f'{a}, 0, {a}'in'%s'%n))]for m in r]for f in r]
# task 393: 63 bytes, gold, https://arcprize.org/play?task=f8ff0b80
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# task 394: 92 vs 91 bytes for gold, https://arcprize.org/play?task=f9012d9b
p=lambda i:[[max(x[b%(n:=2+len(i)//7)::n])for b,y in enumerate(x)if y<1]for x in i if 0in x]
# task 395: 56 vs 53 bytes for gold, https://arcprize.org/play?task=fafffa47
p=lambda a:[[2-c-b.pop(0)&6for c in a.pop(3)]for b in a]
# task 396: 188 vs 179 bytes for gold, https://arcprize.org/play?task=fcb5c309
E=enumerate
p=lambda m,X=8:[*[[[min(a:=sum(m,[]),key=a.count)*(e>0)for e in e[x:x+X]]for e in m[y:]if(f:=f*e[x]==b)]for y,r in E(m)for x,b in E(r)if(f:=[b]*X==r[x:x+X])*b],0][0]or p(m,X-1)
# task 397: 125 vs 121 bytes for gold, https://arcprize.org/play?task=fcc82909
p=lambda m,k=0:exec('r=k//9;exec("m[2%s=3,3;r+=1;"*len(a:={*m[%s+m[1%s})*(not{0,3}&a));k+=1;'%(('+r][k%9:k%9+2]',)*3)*81)or m
# task 398: 79 vs 77 bytes for gold, https://arcprize.org/play?task=feca6190
def p(a):b,=a;l=25-5*b.count(0);return[((~-l*[0]+b)*2)[i:i+l]for i in range(l)]
# task 399: 64 bytes, gold, https://arcprize.org/play?task=ff28f65a
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]
# task 400: 68 vs 67 bytes for gold, https://arcprize.org/play?task=ff805c23
p=lambda g:[h[:5]for r in[*g]if(h:=g.pop()[::-1][[*r,1].index(1):])]
