# task 1: 61 bytes, gold, https://arcprize.org/play?task=007bbfb7:
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]
# task 2: 98 vs 90 bytes for gold, https://arcprize.org/play?task=00d62c1b:
p=lambda a,n=-62:[*map(lambda*b,d=0:[(c%2|d//3)*(d:=c+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]
# task 3: 60 vs 58 bytes for gold, https://arcprize.org/play?task=017c7c7b:
p=lambda g:[[v*2for v in l]for l in g+g[g[:2]!=g[4:]:][2:5]]
# task 4: 110 vs 80 bytes for gold, https://arcprize.org/play?task=025d127b:
p=lambda g,s=0:g and[[[v,j][{*g[0]}<={*sum(g[min(2,s:=s+(v>0)):],[])}]for j,v in zip([0]+g[0],g[0])]]+p(g[1:])
# task 5: 244 vs 206 bytes for gold, https://arcprize.org/play?task=045e512c:
W=range(21)
t=-4,0,4
def p(g):R=max([{(i,j)for i in W[I:I+3]for j in W[J:J+3]if g[i][j]}for I in W for J in W],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in t for D in t for k in W[1:]for c in R)for x in W]for y in W]
# task 6: 51 bytes, gold, https://arcprize.org/play?task=0520fde7:
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
# task 7: 67 vs 65 bytes for gold, https://arcprize.org/play?task=05269061:
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]
# task 8: 94 bytes, gold, https://arcprize.org/play?task=05f2a901:
p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]
# task 9: 127 vs 109 bytes for gold, https://arcprize.org/play?task=06df4c85:
E=enumerate
p=lambda g:[[v or max(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]}|{0})for j,(v,*c)in E(zip(r,*g))]for i,r in E(g)]
# task 10: 72 vs 69 bytes for gold, https://arcprize.org/play?task=08ed6ac7:
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]
# task 11: 160 vs 121 bytes for gold, https://arcprize.org/play?task=09629e4f:
E=enumerate;R=0,4,8
p=lambda g:[[v*(v==5)or min([sum([r[j:j+3]for r in g[i:i+3]],[])for i in R for j in R],key=sum)[i//4*3+j//4]for j,v in E(r)]for i,r in E(g)]
# task 12: 169 vs 129 bytes for gold, https://arcprize.org/play?task=0962bcdd:
E=enumerate
p=lambda g:[[v or max({*zip(b'\0',[v]+sorted(f:=sum(g,[]),key=f.count))}&{((I//12-i)**2+(I%12-j)**2,V)for I,V in E(f)})[1]for j,v in E(r)]for i,r in E(g)]
# task 13: 169 vs 146 bytes for gold, https://arcprize.org/play?task=0a938d79:
def p(g):h=len(g);w=len(g[0]);*q,=filter(any,g);i,*j=map(g.index,q);return h<w and[*zip(*p([*zip(*g)]))]or[w*[(y>=y%(a:=j[0]-i)<1)*max(q[y//a%2])]for y in range(-i,h-i)]
# task 14: 85 vs 70 bytes for gold, https://arcprize.org/play?task=0b148d64:
p=lambda g:[[v for v,*c in zip(l,*g)if{*c}&t]for l in g if{*l}&(t:={*g[0]}^{*g[-1]})]
# task 15: 119 vs 98 bytes for gold, https://arcprize.org/play?task=0ca9ddb6:
E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]
# task 16: 46 vs 43 bytes for gold, https://arcprize.org/play?task=0d3d703e:
p=lambda m:[[b'AA	'[i]for i in m[0]]]*3
# task 17: 120 bytes, gold, https://arcprize.org/play?task=0dfd9992:
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
# task 18: 374 bytes, gold, https://arcprize.org/play?task=0e206a2e:
E=enumerate
def p(g):
 def S(i,v):g[int(i.imag)][int(i.real)]=v
 G={i*1j+j:v for i,r in E(g)for j,v in E(r)if v};*f,=G.values()
 for j in G:s={j};[s:=s|{x}for x in[*G]*5for y in s if abs(x-y)<2];[*s][3:]and[S(T(x-j),G[x])==S(x,0)for a in b''for O in G if all({G[A]}<{max(f,key=f.count),G.get((T:=lambda x:(x-a//4*x.real*2)*1j**a+O)(A-j))}for A in s)for x in s]
 return g
# task 19: 126 vs 119 bytes for gold, https://arcprize.org/play?task=10fcaaa3:
E=enumerate
p=lambda g:[[v or 8*any([*[*g*2,[0]*9][y+d%5-1]*2,0][x+d%3-1]for d in b'-/29')for x,v in E(l*2)]for y,l in E(g*2)]
# task 20: 173 bytes, gold, https://arcprize.org/play?task=11852cab:
r=range(10)
def p(g):i=complex(*[[*map(any,G)].index(1)+2for*G,in(zip(*g),g)]);return[[max((abs(y*1j+x-i)==abs(I*1j+J-i))*g[y][x]for y in r for x in r)for J in r]for I in r]
# task 21: 64 vs 57 bytes for gold, https://arcprize.org/play?task=1190e5a7:
p=eval('lambda a:[[a '+'for a in-~min(map(a.count,a))*a[:1]]'*2)
# task 22: 101 vs 91 bytes for gold, https://arcprize.org/play?task=137eaa0f:
R=-1,0,1
p=lambda g:[[max(f[I+i*11+j]for I in range(121)if(f:=sum(g,[]))[I]==5)for j in R]for i in R]
# task 23: 218 vs 205 bytes for gold, https://arcprize.org/play?task=150deff5:
def p(g,*S):
 w=len(g[0])
 for c in-6&len(S)+4,5:
  for I in S:g[I//w][I%w]=c
  try:f=sum(g,[])*2;i=f.index(5);[{5}-{c}=={f[I]for I in s}!=g==p(g,i,*s)>1for s in[[w+i,1+i,w-~i],[i+1,i+2],[i+w,i+w*2]]]
  except:return g
# task 24: 65 vs 62 bytes for gold, https://arcprize.org/play?task=178fcbfb:
p=lambda a:[[max({*r}-{2})or(2in c)*2for c in zip(*a)]for r in a]
# task 25: 153 bytes, gold, https://arcprize.org/play?task=1a07d186:
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)
# task 26: 52 bytes, gold, https://arcprize.org/play?task=1b2d62fb:
p=lambda a:[[8>>i+b.pop(0)for i in b[4:]]for b in a]
# task 27: 104 vs 103 bytes for gold, https://arcprize.org/play?task=1b60fb0c:
R=range(10)
p=lambda g:[[(g[i][j]^-g[~i+(C:=sum(map(max,*g,*zip(*g)))%2)][~j+C])%3for j in R]for i in R]
# task 28: 70 vs 63 bytes for gold, https://arcprize.org/play?task=1bfc4729:
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']
# task 29: 118 vs 115 bytes for gold, https://arcprize.org/play?task=1c786137:
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]
# task 30: 132 vs 109 bytes for gold, https://arcprize.org/play?task=1caeab9d:
E=enumerate
p=lambda g:[[sum(c for c in(1,2,4)if(g*2)[i+(F:=sum(g,[]).index)(c)//10-F(1)//10][j]==c)for j,_ in E(r)]for i,r in E(g)]
# task 31: 47 vs 45 bytes for gold, https://arcprize.org/play?task=1cf80156:
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)))]
# task 32: 39 bytes, gold, https://arcprize.org/play?task=1e0a9b12:
p=lambda a:[*zip(*map(sorted,zip(*a)))]
# task 33: 77 bytes, gold, https://arcprize.org/play?task=1e32b0e9:
p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]
# task 34: 220 vs 160 bytes for gold, https://arcprize.org/play?task=1f0c79e5:
def p(g):
 f=sum(g,[]);C,={*f}-{0,2};i=min(map(f.index,(2,C)))
 for d in-1,1:
  for D in-1,0:
   o=i//9-~d//2;O=i%9-D
   for a,A in[w:=(d,0),(-d,D|1),w]*9*(g[o][O]==2):
    if-1<o<9>O>-1:g[o][O]=C
    o+=a;O-=A
 return g
# task 35: 108 vs 87 bytes for gold, https://arcprize.org/play?task=1f642eb9:
p=lambda g:[g:=[[r[0]*(s^(s:=s|{v})=={8})or v for v in r]for*r,in zip(*g[::-1])if(s:={0})]for _ in' '*4][-1]
# task 36: 115 vs 92 bytes for gold, https://arcprize.org/play?task=1f85a75f:
p=lambda g:min([(h:=lambda g,k=-99:k*g or h([*zip(*g[C not in g[0]:][::-1])],k+1))(g)for C in{*sum(g,[])}],key=len)
# task 37: 109 vs 108 bytes for gold, https://arcprize.org/play?task=1f876c06:
p=lambda g,a=-1:[[max(sum({*(f:=sum(g,[]))[(a:=a+9//d)::d]}&{*f[a::-d]})for d in(9,11))for _ in g]for _ in g]
# task 38: 52 vs 51 bytes for gold, https://arcprize.org/play?task=1fad071e:
p=lambda g:[(str(g).count('1, 1')//2*[1]+[0]*5)[:5]]
# task 39: 65 vs 60 bytes for gold, https://arcprize.org/play?task=2013d3e2:
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]
# task 40: 97 vs 69 bytes for gold, https://arcprize.org/play?task=2204b7a8:
p=lambda g,k=-1:k*g or p([[[v,g[0][q]][v>0in g[0]]for v in r]for*r,q in zip(*g,[0]*5+[9]*5)],k+1)
# task 41: 49 bytes, gold, https://arcprize.org/play?task=22168020:
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]
# task 42: 169 vs 162 bytes for gold, https://arcprize.org/play?task=22233c11:
Q=range(10)
def p(g):C=sum(b'%r'%g)//38%4;return[[g[i][j]|any(all(((g+g[:1]*3)[i+y*s]+g[0])[j+(3-y)*S]for y in(1,2))for s in(-C,C)for S in(-C,C))*8for j in Q]for i in Q]
# task 43: 57 bytes, gold, https://arcprize.org/play?task=2281f1f4:
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]
# task 45: 45 bytes, gold, https://arcprize.org/play?task=22eb0ac0:
p=lambda g:[10*r[:r[0]==r[9]]or r for r in g]
# task 47: 55 bytes, gold, https://arcprize.org/play?task=23581191:
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
# task 49: 87 vs 81 bytes for gold, https://arcprize.org/play?task=23b5c85d:
p=lambda a:[b.count(e)*[e]for b in a if(e:=min(set(d:=sum(a,[]))-{0},key=d.count))in b]
# task 50: 96 vs 88 bytes for gold, https://arcprize.org/play?task=253bf280:
p=lambda g,*G:[[v or(8in{*r[:j]}&{*r[j:]})*3for j,v in enumerate(r)]for*r,in zip(*G or p(g,*g))]
# task 52: 41 vs 40 bytes for gold, https://arcprize.org/play?task=25d8a9c8:
p=lambda a:[3*[1//len({*b})*5]for b in a]
# task 53: 21 bytes, gold, https://arcprize.org/play?task=25ff71a9:
p=lambda a:(a+a)[2:5]
# task 56: 43 vs 40 bytes for gold, https://arcprize.org/play?task=27a28665:
p=lambda g:[[5^(g[0][0]>0)-3*~(g[0][2]>0)]]
# task 57: 49 bytes, gold, https://arcprize.org/play?task=28bf18c6:
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]
# task 59: 191 vs 156 bytes for gold, https://arcprize.org/play?task=29623171:
def p(g):f=sum(g,[]);C=[sum(R[i%11&~3:][:4].count(0)for R in g[i//11&~3:][:4])for i in range(121)];return[[v*(v==5)or(C[i]==min(C))*max({*f}-{5})for i,v in r]for r in zip(*[enumerate(f)]*11)]
# task 60: 48 bytes, gold, https://arcprize.org/play?task=29c11459:
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]
# task 61: 101 vs 63 bytes for gold, https://arcprize.org/play?task=29ec7d0e:
p=lambda a:min([*map(f:=lambda*b:[max(b[i%n::n])for i in range(18)],*map(f,*a))]for n in range(5,10))
# task 63: 79 vs 77 bytes for gold, https://arcprize.org/play?task=2bee17df:
p=lambda g:[[v or(any(c)*any(r[1:-1])<1)*3for _,*c,_,v in zip(*g,r)]for r in g]
# task 67: 33 bytes, gold, https://arcprize.org/play?task=2dee498d:
p=lambda a:[b[:len(a)]for b in a]
# task 69: 251 vs 153 bytes for gold, https://arcprize.org/play?task=321b1fc6:
def p(a):
	f=lambda b:[c for*c,in zip(*b)if{*c}-{0,8}];s=f(f(a));n=len(s[0])
	for i in range(99):
		j=i%10;i//=10;t=[c[j:j+n]for c in a[i:i+len(s)]]
		for c,d in zip(s,a[i:]*(t in[s,[[d and 8for d in c]for c in s]])):d[j:j+n]=c*(t!=s)or[0]*n
	return a
# task 72: 61 vs 54 bytes for gold, https://arcprize.org/play?task=3428a4f5:
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]
# task 73: 46 bytes, gold, https://arcprize.org/play?task=3618c87e:
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]
# task 74: 158 vs 91 bytes for gold, https://arcprize.org/play?task=3631a71a:
def p(g):g=[[x%9for x in r]+[0,0]for r in g]+[[0]*32]*2;return[[*map(max,*sum([[x,x[:1:-1]]for x in k],[]))]for k in zip(g,g[:1:-1],[*zip(*g)][::-1],zip(*g))]
# task 76: 355 vs 311 bytes for gold, https://arcprize.org/play?task=36d67576:
E=enumerate
def p(g):
 G={j+i*1j:v^2for i,r in E(g)for j,v in E(r)if v};[abs(I-J)<2!=s.add(J)for P in G if G[P]%2if[s:={P}]for J in[*G]*6for I in[*s]]
 for a in range(8):
  for I in G:i=min(r:={(x-a//4*x.real*2)*1j**a:G[x]for x in s},key=r.get)-I;g=g*any(13%-~r[y]^G.get(y-i,1)for y in r)or[[r.get(I*1j+j+i,v^2)^2for j,v in E(R)]for I,R in E(g)]
 return g
# task 78: 65 vs 60 bytes for gold, https://arcprize.org/play?task=3906de3d:
p=lambda g:[[c[c.count(1)+~i]for*c,in zip(*g)]for i in range(10)]
# task 81: 95 bytes, gold, https://arcprize.org/play?task=3aa6fb7a:
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(m,i-1)[::-1]))))]
# task 82: 50 bytes, gold, https://arcprize.org/play?task=3ac3eb23:
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3
# task 83: 40 bytes, gold, https://arcprize.org/play?task=3af2c5a8:
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 84: 65 vs 62 bytes for gold, https://arcprize.org/play?task=3bd67248:
def p(g,i=0):
 while g[1-i:]:i-=1;g[~i][i]=2;g[-1][i]=4
 return g
# task 85: 57 vs 56 bytes for gold, https://arcprize.org/play?task=3bdb4ada:
p=lambda g,t=0:[g:=[t:=v^t&v*(g==r)for v in r]for r in g]
# task 87: 36 bytes, gold, https://arcprize.org/play?task=3c9b0459:
p=lambda a:[b[::-1]for b in a[::-1]]
# task 88: 109 vs 101 bytes for gold, https://arcprize.org/play?task=3de23699:
p=lambda a,n=-3:n*a[1:-1]or p([a[1:],[[d and(b:=max(a[n%2]))for d in c]for c in zip(*a[:0:-1])]][e:=b>0],n+e)
# task 90: 197 vs 159 bytes for gold, https://arcprize.org/play?task=3eda0437:
e=enumerate
p=lambda a:min(['7'in str(g:=[[s|6*(i<=m<=j)*(k<=n<=l)for n,s in e(r)]for m,r in e(a)]),-str(g).count('6'),g]for i,b in e(a)for j,_ in e(a)for k,_ in e(b)for l,_ in e(b)if j-i>0<l-k)[2]
# task 91: 69 vs 63 bytes for gold, https://arcprize.org/play?task=3f7978a0:
p=lambda a,n=-3:a*n or p([a[1:],[*zip(*a)][::-1]][c:=5in a[n%2]],n+c)
# task 96: 373 vs 321 bytes for gold, https://arcprize.org/play?task=4290ef0e:
def p(g,*S):
 for c in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i for i,v in enumerate(r)if v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for x in r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
 R=range(w:=max(S)[0]);return[[([C for W,G,C in S if G<(M:=sorted(abs(w//2-v)for v in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for j in R]for i in R]
# task 98: 101 vs 88 bytes for gold, https://arcprize.org/play?task=4347f46a:
E=enumerate
p=lambda g:[[v*(0in[*r[j-1:j+2],*[*zip(*g)][j][i-1:i+2]])for j,v in E(r)]for i,r in E(g)]
# task 100: 88 vs 54 bytes for gold, https://arcprize.org/play?task=445eab21:
p=lambda a:[[max(range(1,10),key=[sum({*b}&{*c})for c in zip(*a)for b in a].count)]*2]*2
# task 102: 310 vs 150 bytes for gold, https://arcprize.org/play?task=44d8ac46:
R=range;W=R(12)
def p(g):
 def t(C):
  for _ in W:C|={(a+d,A+D)for a,A in C for d,D in[(1,0),(-1,0),(0,1),(0,-1)]if-1<a+d<12>A+D>=0==g[a+d][A+D]}
  y,x=min(C);Y,X=max(C)
  if X-x==Y-y!=C=={(a,b)for a in R(y,Y+1)for b in R(x,X+1)}:
   for i,j in C:g[i][j]=2
 [g[i][j]or t({(i,j)})for i in W for j in W];return g
# task 103: 29 bytes, gold, https://arcprize.org/play?task=44f52bb0:
p=lambda a:[[a==a[::-1]or 7]]
# task 104: 116 vs 84 bytes for gold, https://arcprize.org/play?task=4522001f:
Q=[0]
p=lambda g:[Q*9][(t:=g[0][1]>0):]+([Q[(f:=g[1][0]>0):]+(H:=[3]*4+Q*f)+Q*4]*4+[Q*(5-f)+H]*4)[::-t^-f|1]+[Q*9]*t
# task 105: 154 vs 148 bytes for gold, https://arcprize.org/play?task=4612dd53:
A=any
p=lambda g,k=-3:k*g or p([[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1],k+1)
# task 106: 76 vs 67 bytes for gold, https://arcprize.org/play?task=46442a0e:
p=lambda g,*x:[x:=[w:=a+b[::-1],*x,w[::-1]]for*b,a in[*zip(*g,g)][::-1]][-1]
# task 108: 58 vs 56 bytes for gold, https://arcprize.org/play?task=46f33fce:
p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)
# task 109: 91 vs 81 bytes for gold, https://arcprize.org/play?task=47c1f68c:
p=lambda a:[*map(f:=lambda*b,i=len(a)//2:[c and b[i]for c in b[:i]+b[i-1::-1]],*map(f,*a))]
# task 111: 61 vs 60 bytes for gold, https://arcprize.org/play?task=48d8fb45:
p=lambda g:[(f:=sum(g,[]))[f.index(5)+d:][:3]for d in b'	']
# task 113: 25 bytes, gold, https://arcprize.org/play?task=496994bd:
p=lambda a:a[:5]+a[4::-1]
# task 114: 65 bytes, gold, https://arcprize.org/play?task=49d1d64f:
p=lambda g:[[0,*g[0],0],*[r[:1]+r+r[-1:]for r in g],[0,*g[-1],0]]
# task 115: 54 bytes, gold, https://arcprize.org/play?task=4be741c5:
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]
# task 116: 20 bytes, gold, https://arcprize.org/play?task=4c4377d9:
p=lambda a:a[::-1]+a
# task 119: 127 vs 106 bytes for gold, https://arcprize.org/play?task=508bd3b6:
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)
# task 120: 102 vs 98 bytes for gold, https://arcprize.org/play?task=50cb2852:
p=lambda g,P=[[0]*20]:[[[8,*w][0in w]for w in zip(r,*e,[0]+r,r[1:]+[0])]for*e,r in zip(P+g,g[1:]+P,g)]
# task 121: 96 vs 90 bytes for gold, https://arcprize.org/play?task=5117e062:
p=lambda g,k=-39:[[sum({*g[0]*v})for v in r]for r in k*g]or p([*zip(*g[(8in g[-2])-2::-1])],k+1)
# task 122: 102 vs 88 bytes for gold, https://arcprize.org/play?task=5168d44c:
p=lambda g:[[v%2*v|o[sum(3in r for r in g)<2]%3for*o,v in zip(i,[0,0]+r,r)]for i,r in zip(g[-2:]+g,g)]
# task 123: 76 vs 75 bytes for gold, https://arcprize.org/play?task=539a4f51:
R=range(10)
p=lambda g:[[g[0][max(i,j)%(5-0**g[0][4])]for j in R]for i in R]
# task 126: 57 vs 54 bytes for gold, https://arcprize.org/play?task=54d82841:
p=lambda a:a[:-1]+[[4*(sum(c)<2*max(c))for c in zip(*a)]]
# task 127: 85 vs 65 bytes for gold, https://arcprize.org/play?task=54d9e175:
p=lambda a:[*map(f:=lambda*b:sum(([5]+3*[e%5+5]for e in b[1::4]),[])[1:],*map(f,*a))]
# task 128: 73 vs 64 bytes for gold, https://arcprize.org/play?task=5521c0d9:
p=lambda g,k=15:k*[0]and[[c[c.count(max(c))-k]for c in zip(*g)]]+p(g,k-1)
# task 129: 47 bytes, gold, https://arcprize.org/play?task=5582e5ca:
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3
# task 130: 65 bytes, gold, https://arcprize.org/play?task=5614dbcf:
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]
# task 131: 126 bytes, gold, https://arcprize.org/play?task=56dc2b01:
p=lambda a,n=-3:n*a or p([[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))],n+1)
# task 135: 32 bytes, gold, https://arcprize.org/play?task=5bd6f4ac:
p=lambda a:[b[6:]for b in a[:3]]
# task 136: 113 vs 105 bytes for gold, https://arcprize.org/play?task=5c0a986e:
import re
p=lambda m,S=re.sub:eval(eval('S("(?<=(2.{34}){2})0","2",S("0(?=(.{34}1){2})","1",'*9+f'"{m}"'+'))'*9))
# task 137: 143 bytes, gold, https://arcprize.org/play?task=5c2c9af4:
def p(a):r=range(len(a));X,Y=[(x:=i,j)for i in r for j in r if a[i][j]][1];return[[a[X][Y]*(max(X-i,i-X,Y-j,j-Y)%(x-X)<1)for j in r]for i in r]
# task 139: 102 vs 94 bytes for gold, https://arcprize.org/play?task=60b61512:
import re
p=lambda m,i=11:-i*m or[*zip(*eval(re.sub("0(?=, [^0].{25}[^0])","7",str(p(m,i-1)[::-1]))))]
# task 140: 36 bytes, gold, https://arcprize.org/play?task=6150a2bd:
p=lambda a:[b[::-1]for b in a[::-1]]
# task 141: 119 vs 96 bytes for gold, https://arcprize.org/play?task=623ea044:
p=lambda m:(R:=range(N:=len(m)))and[[(a:=sum(m,[]))[i:=a.index(max(a))]*(abs(r-i//N)==abs(c-i%N))for c in R]for r in R]
# task 142: 40 bytes, gold, https://arcprize.org/play?task=62c24649:
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 144: 59 vs 53 bytes for gold, https://arcprize.org/play?task=6430c8c4:
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]
# task 146: 58 bytes, gold, https://arcprize.org/play?task=662c240a:
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
# task 147: 88 vs 84 bytes for gold, https://arcprize.org/play?task=67385a82:
p=lambda g,k=-3:g*k or p([[a+-a%~b%8for a,b in zip(r,[0]+r)]for*r,in zip(*g[::-1])],k+1)
# task 149: 83 vs 75 bytes for gold, https://arcprize.org/play?task=6773b310:
p=lambda m,a=[0,4,8]:[[sum(sum(m[r+i//4][c:c+3])for i in a)>7for c in a]for r in a]
# task 150: 30 bytes, gold, https://arcprize.org/play?task=67a3c6ac:
p=lambda g:[r[::-1]for r in g]
# task 152: 40 bytes, gold, https://arcprize.org/play?task=67e8384a:
p=lambda a:[r+r[::-1]for r in a+a[::-1]]
# task 155: 18 bytes, gold, https://arcprize.org/play?task=68b16354:
p=lambda a:a[::-1]
# task 157: 391 vs 296 bytes for gold, https://arcprize.org/play?task=6a1e5592:
t=b'\n'
def p(g):
 def Q(o,p):
  c=C[o:];(3,)<=c!=Q(o+1,p)
  for A in S:
   h=len(A);A in p or h==sum(x-y-4%y<=min(map(int.__sub__,A,c))for x,y in zip(A,c))!=Q(o+h,p|{A:o})
   for I in 6,7,8,9:
    for J in range(o//15*h):g[I-A[0]+C[p[A]]][J+p[A]]|=g[I][m:=J+K.find(t+A+t)]>0;g[I][m]=0
 K,C=zip(*[([*c,5].index(5),c.count(2))for c in zip(*g)]);K=t+bytes(K)+t;S={*K.split(t)};Q(0,{});return g
# task 160: 123 vs 116 bytes for gold, https://arcprize.org/play?task=6c434453:
import re
p=lambda m,i=9:-i*m or p(eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1",r'0,2,0\1 2,2,2\2 0,2,0',str(m))),i-1)
# task 162: 132 vs 97 bytes for gold, https://arcprize.org/play?task=6cf79266:
r=range(324)
def p(a):
	for i in r:
		b=a[i%18:][:3];i//=18;z=any(max([*zip(*b)][i:i+3]))
		for k in r:b[k%5%3][i+k%3]**=z
	return a
# task 163: 143 vs 137 bytes for gold, https://arcprize.org/play?task=6d0160f0:
R=0,4,8
e=enumerate
p=lambda a:[[b*(b==5)or sum({a[k+i%4][l+j%4]for k in R for l in R if 4==a[k+i//4][l+j//4]})for j,b in e(r)]for i,r in e(a)]
# task 164: 32 bytes, gold, https://arcprize.org/play?task=6d0aefbc:
p=lambda a:[b+b[::-1]for b in a]
# task 166: 65 vs 61 bytes for gold, https://arcprize.org/play?task=6d75e8bb:
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]
# task 170: 303 vs 211 bytes for gold, https://arcprize.org/play?task=6ecd11f4:
E=enumerate
def p(g):
 I,J,W,*C=next((i,j,3+(r[j+3]>0))for i,r in E(g)for j,_ in E(r)if[*{*all(s:=r[j:j+3]+g[i+1][j:j+3])*s}][1:])
 for r in g[I:I+W]:C+=r[J:J+W],;r[J:J+W]=[0]*W
 [g:=[r for*r,in zip(*g)if any(r)]for _ in'  '];B=len(g)//W;return[[V*(v>0)for v,V in zip(r[::B],R)]for r,R in zip(g[::B],C)]
# task 171: 54 bytes, gold, https://arcprize.org/play?task=6f8cd79b:
p=lambda a:[*map(f:=lambda*b:[8,*b[2:],8],*map(f,*a))]
# task 172: 20 bytes, gold, https://arcprize.org/play?task=6fa7a44f:
p=lambda a:a+a[::-1]
# task 174: 105 vs 97 bytes for gold, https://arcprize.org/play?task=72ca375d:
p=lambda g,c=1:(k:=(f:=lambda g:[r for*r,in zip(*g)if c in r])(f(g)))*(k==[x[::-1]for x in k])or p(g,c+1)
# task 176: 74 vs 65 bytes for gold, https://arcprize.org/play?task=7447852a:
p=lambda g:[[*map(max,(([4]*3+[0]*9)*9)[a%8::a%3],g[a%5])]for a in b"7)a"]
# task 177: 55 vs 53 bytes for gold, https://arcprize.org/play?task=7468f01a:
p=lambda g:[[*filter(abs,r)][::-1]for r in g if any(r)]
# task 178: 49 bytes, gold, https://arcprize.org/play?task=746b3537:
p=lambda a:a*-1*-1or[p(b)for b in a if a!=(a:=b)]
# task 179: 21 bytes, gold, https://arcprize.org/play?task=74dd1130:
p=lambda a:[*zip(*a)]
# task 180: 82 vs 79 bytes for gold, https://arcprize.org/play?task=75b8110e:
p=lambda g:[[max(x,key=bool)for x in zip(r[4:],R,R[4:],r)]for r,R in zip(g,g[4:])]
# task 181: 67 bytes, gold, https://arcprize.org/play?task=760b3cac:
def p(a):
	for b in a[:3]:c=6>>a[3][3];b[c:c+3]=b[5:2:-1]
	return a
# task 182: 187 vs 176 bytes for gold, https://arcprize.org/play?task=776ffc46:
def p(g):
 R=F=sum(g,[])
 while C:=[*{*F}][-2]:
  o=F.index(C)-2;N={d for d in range(70)if d%20<6>F[d+o]==C}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g
# task 186: 66 vs 61 bytes for gold, https://arcprize.org/play?task=794b24be:
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
# task 188: 75 vs 61 bytes for gold, https://arcprize.org/play?task=7b7f7511:
p=lambda a:[a[:len(a)//2],c:=[b[:len(b)//2]for b in a]][a==[b*2for b in c]]
# task 193: 98 vs 85 bytes for gold, https://arcprize.org/play?task=7f4411dc:
import re
p=lambda m,*a:eval(re.sub(r"(?<=[0 ,]..)\d(?=..[0 ])",'0',f" {[*zip(*a or p(m,*m))]} "))
# task 194: 92 vs 73 bytes for gold, https://arcprize.org/play?task=7fe24cdd:
def p(M,m=[[0]*6]*6):
 for i in[0,1,2]*9:m[i][:3]=M[i];*m,=map(list,zip(*m[::-1]))
 return m
# task 195: 105 bytes, gold, https://arcprize.org/play?task=80af3007:
p=lambda a,n=-1:n*[[d&e for d in b for e in c]for b in a for c in a]or p([*filter(any,zip(*a[::3]))],n+1)
# task 197: 54 bytes, gold, https://arcprize.org/play?task=82819916:
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]
# task 198: 122 bytes, gold, https://arcprize.org/play?task=83302e8f:
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)
# task 200: 110 vs 84 bytes for gold, https://arcprize.org/play?task=8403a5d5:
p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]
# task 202: 109 vs 107 bytes for gold, https://arcprize.org/play?task=855e0971:
p=lambda a:(len({*a[0]}-{0})<2)*[[*map(min,*[c for c in a if max(b)in c])]for b in a]or[*zip(*p([*zip(*a)]))]
# task 203: 69 vs 64 bytes for gold, https://arcprize.org/play?task=85c4e7cd:
p=lambda a:[[(d:=a[l:=len(a)//2])[l+d.index(c)]for c in b]for b in a]
# task 204: 142 vs 96 bytes for gold, https://arcprize.org/play?task=868de0fa:
def p(g):
 for r in g:
  I=0
  for i,c in enumerate(r):
   if c<1==r[i-1]!=(r+[0])[i-2]:I^=1;j=i
   if I>c:r[i]=2|r[j:].index(1)%2*5
 return g
# task 205: 235 vs 189 bytes for gold, https://arcprize.org/play?task=8731374e:
p=lambda g:max([[min(w:=r+c,key=w.count)for*c,in zip(*S)]for r in S]for A in range(len(g.pop(0))-6)if(s:=lambda w:len({*sum([r[A:A+6]for r in g[:6]],w[:6])})<=2)for S in[[[v for v,*c in zip(r,*g)if s(c)]for r in g if s(r[A:])]])or p(g)
# task 206: 176 vs 144 bytes for gold, https://arcprize.org/play?task=88a10436:
def p(g):
 r,c=[min(i for i,r in enumerate(k)if{*r}-{0,5})for k in(g,zip(*g))];I=sum(g,[]).index(5);W=len(g[0])
 for i in 0,1,2:g[I//W-1+i][I%W-1:I%W+2]=g[r+i][c:c+3]
 return g
# task 207: 81 bytes, gold, https://arcprize.org/play?task=88a62173:
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[3:])]'*2)
# task 210: 20 bytes, gold, https://arcprize.org/play?task=8be77c9e:
p=lambda a:a+a[::-1]
# task 211: 48 bytes, gold, https://arcprize.org/play?task=8d5021e8:
p=lambda g:[l[::-1]+l for l in(g[::-1]+g)*2][:9]
# task 213: 113 vs 92 bytes for gold, https://arcprize.org/play?task=8e1813be:
def p(g):R=all(map(any,g));C={v:0 for r in[g,zip(*g)][R]for v in r if v%5};return[[[c,b][R]for b in C]for c in C]
# task 214: 63 vs 62 bytes for gold, https://arcprize.org/play?task=8e5a5113:
p=lambda a:[b[:4]+c[::-1]+a.pop()[3::-1]for*c,b in[*zip(*a,a)]]
# task 215: 46 bytes, gold, https://arcprize.org/play?task=8eb1be9a:
p=lambda a:[max((a:=a[:2]+a)[2::3])for _ in a]
# task 216: 125 vs 114 bytes for gold, https://arcprize.org/play?task=8efcae92:
r=range(661)
p=lambda a:max([-(c:=sum(b:=[b[x>>5:y>>5]for b in a[x%32:y%32]],a).count)(0),c(2),-x,b]for x in r for y in r)[3]
# task 217: 95 bytes, gold, https://arcprize.org/play?task=8f2ea7aa:
p=lambda a,*n:[*filter(any,zip(*[[d&e for d in b for e in c]for b in n for c in a]or p(a,*a)))]
# task 218: 58 bytes, gold, https://arcprize.org/play?task=90c28cc7:
p=lambda a,*n:[*{b:0for b in zip(*n or p(a,*a))if any(b)}]
# task 219: 307 vs 269 bytes for gold, https://arcprize.org/play?task=90f3ed37:
Z=zip
def p(a,h=0):
	b=[*map(any,a)].index;d=b(0,c:=b(1));q=a[c:d];k=h//4;j=h%4>2;i=h%4%3;u,*r,v=a[k:k+d-c+2];*s,=Z(*r);l=-[*map(any,s[::-1]),1].index(1);s=s[:l];e=[*Z(*q)][j:l+j-i]==s[i:]!=s[:i]==s[i:i+i]!=u==v
	for m,n in Z(q,r):n[l:]=[x+(e*y>x)for x,y in Z(n[l:],m[l+j-i:]+u)]
	return h//52*a or p(a,h+1)
# task 220: 116 vs 89 bytes for gold, https://arcprize.org/play?task=913fb3ed:
E=enumerate
p=lambda g:[[v or max(v*95%9for r in g[i+i%~i:i+2]for v in[0,*r][j:j+3])for j,v in E(l)]for i,l in E(g)]
# task 221: 103 vs 94 bytes for gold, https://arcprize.org/play?task=91413438:
def p(a):r=range(d:=str(a).count('0'));return[[c*(j<9+d*~i)for j in r for c in b]for i in r for b in a]
# task 222: 230 vs 144 bytes for gold, https://arcprize.org/play?task=91714a58:
def p(g):n=len(g);R=range(n);_,a,b,c,d=max(((c-a)*(d-b),a,b,c,d)for a in R for b in R for c in R for d in R if{0}!={g[a][b]}=={g[i][j]for i in range(a,c)for j in range(b,d)});return[[g[i][j]*(a<=i<c)*(b<=j<d)for j in R]for i in R]
# task 223: 52 vs 51 bytes for gold, https://arcprize.org/play?task=9172f3a0:
p=lambda a:eval("[[a "+"for a in a for _ in%s]"%a*2)
# task 224: 218 vs 171 bytes for gold, https://arcprize.org/play?task=928ad970:
def p(g):E=enumerate;(y,*_,Y),(x,*_,X)=map(sorted,zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]));f=sum(g,[]);c,={*f}-{0,5};return[[v|c*((x<j<X)*(i in{y+1,Y-1})|(y<i<Y)*(j in{x+1,X-1}))for j,v in E(r)]for i,r in E(g)]
# task 225: 224 vs 139 bytes for gold, https://arcprize.org/play?task=93b581b8:
def p(g):
 o=eval(str(g));R={*range(6)}
 for i in R:
  for j in R:
   for S in b' *#-':
    for A in({i+(d:=S%5-1),j+(D:=S%3-1)}<R!=0<o[i+d][j+D])*b"*/&+":
     if{b:=A%5*d+i,B:=A%4*D+j}<R:g[b][B]=g[b][B]or o[i][j]
 return g
# task 227: 57 vs 52 bytes for gold, https://arcprize.org/play?task=94f9d214:
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(4)]for b in a]
# task 229: 73 bytes, gold, https://arcprize.org/play?task=9565186b:
p=lambda a:[[[5,c][c==max(d:=sum(a,a),key=d.count)]for c in b]for b in a]
# task 230: 144 vs 115 bytes for gold, https://arcprize.org/play?task=95990924:
E=enumerate
p=lambda g:[[v+sum(k*((t:=(g+g)[i-(~-k&2)+1]+[0])[s:=j-(-1)**k]>t[j]|[*g[i],0][s])for k in(1,2,3,4))for j,v in E(r)]for i,r in E(g)]
# task 231: 43 bytes, gold, https://arcprize.org/play?task=963e52fc:
p=lambda a:[(r[:6]*4)[:len(r)*2]for r in a]
# task 232: 67 vs 58 bytes for gold, https://arcprize.org/play?task=97999447:
p=lambda a:[(c:=0)or[c:=e or c and 5^c^sum(b)for e in b]for b in a]
# task 233: 552 vs 331 bytes for gold, https://arcprize.org/play?task=97a05b5b:
E=enumerate
W=range
J=1j
def p(g,*S):
 V={*S};G={i*J+j:v for i,r in E(g)for j,v in E(r)}
 for I in G:
  s={I}
  for _ in' '*25:s={n for I in s for n in G if G[n]if abs(I-n)<2}-V
  if s:V|=s;S+=s,
 T,*f=sorted(S,key=lambda c:-sum(G[i]==2for i in c));(y,x),*_,(Y,X)=sorted([int(c.imag),int(c.real)]for c in T)
 for H in f:
  for a in W(4):
   o,*_=h={I*J**a:G[I]for I in H}
   for d in G:
    for I in[*h]*all((x<=(i:=I-o+d).real<=X)*(y<=i.imag<=Y)and(h[I]==2)^(G[i]>0)for I in h):G[I-o+d]=h[I]
 return[[G.get(i*J+j,0)for j in W(x,X+1)]for i in W(y,Y+1)]
# task 235: 66 vs 62 bytes for gold, https://arcprize.org/play?task=995c5fa3:
p=lambda g:[[1-g[2][s+1]*2-g[1][s]&g[3][s+2]+6]*3for s in(0,5,10)]
# task 236: 63 vs 54 bytes for gold, https://arcprize.org/play?task=99b1bc43:
p=lambda a:[[3*c^b.pop(0)*3//2for c in a.pop(0)]for b in a[5:]]
# task 237: 67 bytes, gold, https://arcprize.org/play?task=99fa7670:
p=lambda a,c=0:[(b:=0)or[c:=(b:=b or d)for d in r+[c]]for*r,_ in a]
# task 239: 108 vs 105 bytes for gold, https://arcprize.org/play?task=9af7a82c:
p=lambda a,i=0:[b:=sum(a,[]),c:=b.count]*any(r:=sorted([e*(c(e)>i)for e in{*b}],key=c)[::-1])and[r]+p(a,i+1)
# task 241: 21 bytes, gold, https://arcprize.org/play?task=9dfd6313:
p=lambda a:[*zip(*a)]
# task 242: 54 bytes, gold, https://arcprize.org/play?task=9ecd008a:
p=lambda g:[r[~r.index(0)::-1][:3]for r in g if 0in r]
# task 243: 79 bytes, gold, https://arcprize.org/play?task=9edfc990:
p=lambda a,n=-79:a*n or[*zip(*eval(str(p(a,n+1)[::-1]).replace('1, 0','1,1')))]
# task 244: 65 bytes, gold, https://arcprize.org/play?task=9f236235:
p=lambda a,n=1:(a[n]!=a[0])*[b[::~n]for b in a][::1+n]or p(a,n+1)
# task 246: 137 vs 126 bytes for gold, https://arcprize.org/play?task=a2fd1cf0:
def p(a,n=0,b=0):
	for c in a:d=b;b^=sum(c)%8*4&8;c[j]=c[j:=sum(a,c).index(3-n)%len(c)]or d|b
	*d,=map(list,zip(*a));return n*d or p(d,1)
# task 247: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a3325580:
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]
# task 249: 26 bytes, gold, https://arcprize.org/play?task=a416b8f3:
p=lambda a:[r*2for r in a]
# task 250: 205 vs 127 bytes for gold, https://arcprize.org/play?task=a48eeaf7:
T=10
def p(g):
 *E,=enumerate(f:=sum(g,[]))
 for J,v in E:
  if v==5:g[J//T][J%T]=0;_,I=min({(abs(a//T-J//T)+abs(a%T-J%T),a)for d in b'*+,! "456'for i,v in E if v==2>f[a:=i+d-43]});g[I//T][I%T]=5
 return g
# task 251: 94 vs 89 bytes for gold, https://arcprize.org/play?task=a5313dff:
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]
# task 252: 61 vs 57 bytes for gold, https://arcprize.org/play?task=a5f85a15:
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]
# task 253: 148 bytes, gold, https://arcprize.org/play?task=a61ba2ce:
def p(g):f=sum(g,[]);k=f*2;return[[max(v*(k[i+1-j%5]*k[i+13-j%3*13]==v*v)for i,v in enumerate(f))for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]
# task 254: 119 vs 99 bytes for gold, https://arcprize.org/play?task=a61f2674:
E=enumerate
def p(g):a,*_,b={j%9:1for j,v in E(sum(g,[]))if v};return[[v%2*(j==a or(j==b)*2)for j,v in E(r)]for r in g]
# task 255: 381 vs 280 bytes for gold, https://arcprize.org/play?task=a64e4611:
def p(g):
 for R in[lambda x:[r[::-1]for*r,in zip(*x)]]*4:
  c,={*sum(g:=R(g),[])}-{0,3};D=*[[*r,c].index(c)for r in g],99,0;j=-1
  while(i:=j+1)<30:
   while 10<D[j:=j+1]:0
   for r in g[i+(i>0):j+j%~j]:w=min(D[i:j])-1;r[:w]=[3]*w
 for _ in g*2:
  for r in(m:=(g:=R(g))[:[*[3in(a,b)for a,*_,b in g],1].index(1)]):r[:]=[v*(v!=3or[*f,f[0]].count(3)>2)for*f,v in zip(*m,r)]
 return g
# task 256: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a65b410d:
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
# task 257: 81 bytes, gold, https://arcprize.org/play?task=a68b268e:
p=eval('lambda a:[[next(filter(int,sum(a,())),0)'+'for*a,in map(zip,a,a[5:])]'*2)
# task 258: 61 bytes, gold, https://arcprize.org/play?task=a699fb00:
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))
# task 259: 86 vs 85 bytes for gold, https://arcprize.org/play?task=a740d043:
p=lambda a,n=-23:n*a or p([[d*(d>1)for d in c]for c in zip(*a[a<[[0]*9]:])][::-1],n+1)
# task 260: 150 bytes, gold, https://arcprize.org/play?task=a78176bb:
r=range(10)
p=lambda a:[[(c:=max({*max(a)}-{5}))*(c==a[i][j]or sum(m-n-i+j+k%5-2==0<a[m][n]for m in r for n in r for k in r)==2)for j in r]for i in r]
# task 261: 47 bytes, gold, https://arcprize.org/play?task=a79310a0:
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]
# task 262: 42 vs 39 bytes for gold, https://arcprize.org/play?task=a85d4709:
p=lambda a:[3*[-b.index(5)%3+2]for b in a]
# task 263: 122 bytes, gold, https://arcprize.org/play?task=a87f7484:
p=lambda g:g[(T:=[*zip(*[(x>0for y in g for x in y)]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p([*zip(*g)]))]
# task 264: 237 vs 216 bytes for gold, https://arcprize.org/play?task=a8c38be5:
def p(g):
 w=len(g[0]);I=0,1,2,w,w+1,w+2,2*w,w-~w,2*w+2;O=[[*I]for _ in I];f=sum(g,[]);i=0
 for v in f:
  if v:
   P=b'@6!9<@\0'[hash((*(f[i+o]!=5for o in I),))%11]
   for o in I:O[P//9+o//w][P%9+o%w]=f[i+o];f[i+o]=0
  i+=1
 return O
# task 266: 103 vs 102 bytes for gold, https://arcprize.org/play?task=a9f96cdd:
p=lambda g:[([0,0,0,r%9,0,r//9]*2)[4-max(g).index(2):][:5]for r in b'\09\0G\0'[2-g.index(max(g)):][:3]]
# task 267: 57 vs 46 bytes for gold, https://arcprize.org/play?task=aabf363d:
p=lambda a:[[(d:=a[-1][0])*(0<c!=d)for c in b]for b in a]
# task 268: 341 vs 265 bytes for gold, https://arcprize.org/play?task=aba27056:
E=enumerate
def p(g):
 for _ in[G:=[*g]]*4:
  for v in g,G:v[:]=map(list,zip(*v[::-1]))
  for i,r in E(G):
   for j,v in E(r):
    for D in(-1,1,0)*(v<max(r)<sum(r[j:])&sum(r[:j])):
     for J in[j,j-1,j+1,j][[i<G.index(max(G)),4>>4*r[j+D]][D]or 3:]:
      I=i-(D^J==j)
      while-1<(I:=I+1)<len(g)>(J:=J+D)>-1<G[I][J]<1:g[I][J]=4
 return g
# task 269: 64 vs 63 bytes for gold, https://arcprize.org/play?task=ac0a08a4:
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 270: 122 vs 119 bytes for gold, https://arcprize.org/play?task=ae3edfdc:
import re
p=lambda m,i=31:-i*m or p(eval(re.sub(f'({7>>i%3})([^(]*)0(?=, {i%3%2+1})',r'0\2\1',str([*zip(*m)][::-1]))),i-1)
# task 271: 86 bytes, gold, https://arcprize.org/play?task=ae4f1146:
p=eval(f"lambda a:max([str(a).count('1'),a]{'for*a,in map(zip,a,a[1:],a[2:])'*2})[1]")
# task 272: 101 vs 89 bytes for gold, https://arcprize.org/play?task=aedd82e4:
P=[[0]*9]
p=lambda g:[[v>>1-any(c)for*c,v in zip(*X,[0]+r,r[1:]+[0],r)]for*X,r in zip(P+g,g[1:]+P,g)]
# task 273: 116 bytes, gold, https://arcprize.org/play?task=af902bf9:
R=range(10)
p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in{*R}-{i}for J in{*R}-{j}})//5*2for j in R]for i in R]
# task 274: 77 vs 71 bytes for gold, https://arcprize.org/play?task=b0c4d837:
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,4+c&8],[0]*3]
# task 275: 140 vs 137 bytes for gold, https://arcprize.org/play?task=b190f7f5:
p=lambda g,k=-3:g*k or p([h:=[*zip(*g[(w:=len(g))::-1])],[[v*t//8for v in c for t in r]for c in h[:w]for r in h[w:]]]['8'in str(h[w:])],k+1)
# task 276: 38 bytes, gold, https://arcprize.org/play?task=b1948b0a:
p=lambda a:eval(str(a).replace(*'62'))
# task 277: 199 bytes, gold, https://arcprize.org/play?task=b230c067:
def p(g,*M):
 for i in(A:=[i+i//10*20for i,v in enumerate(sum(g,[]))if v])*2:s={0};[s.add(y-i)for y in A*3for I in[*s]if abs(y-i-I)in[*b'\0']];M+=s,;g[i//30][i%10]=3-M[:len(A)].count(s)
 return g
# task 278: 179 vs 118 bytes for gold, https://arcprize.org/play?task=b27ca6d3:
def p(g):E=enumerate;L=abs;S={(i,j)for i,r in E(g)for j,v in E(r)if v};return[[v or 3*any(L(a-I)+L(A-J)==1==L(i-I)|L(j-J)for a,A in S for I,J in S)for j,v in E(r)]for i,r in E(g)]
# task 279: 118 bytes, gold, https://arcprize.org/play?task=b2862040:
p=lambda g,f=126:~f*g or p([[[b+7*(a>7>1==b),b%(9+a),b or 9][f>>6]for a,b in zip([0]+r,r)]for*r,in zip(*g[::-1])],f-1)
# task 280: 185 bytes, gold, https://arcprize.org/play?task=b527c5c6:
def p(a,n=3):
	for i,b in enumerate(a):
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):i-~d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
# task 281: 187 vs 146 bytes for gold, https://arcprize.org/play?task=b548a754:
r=lambda g:[r[::-1]for*r,in zip(*g)]
def p(g):u=*map(set,g),{0,8};j=u.index(max(u,key=len));i=u.index({0,8});return g[:i]==i*g[:1]and g[:i]+[g[j-1]]+[g[j]]*(j+~i)+g[j:]or r(r(r(p(r(g)))))
# task 282: 89 vs 86 bytes for gold, https://arcprize.org/play?task=b60334d2:
p=lambda a:[*map(f:=lambda*b:[c|e|d>>2for c,d,e in zip([0,*b],b,b[1:]+(0,))],*map(f,*a))]
# task 283: 94 vs 86 bytes for gold, https://arcprize.org/play?task=b6afb2da:
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]
# task 286: 134 vs 109 bytes for gold, https://arcprize.org/play?task=b782dc8a:
import re
p=lambda m,i=291:-i*m or p([*zip(*eval(re.sub("0(?=, ([^08]))",lambda x:s.strip(", 08[]()"+x[1])[0],s:=str(m))))][::-1],i-1)
# task 287: 63 vs 56 bytes for gold, https://arcprize.org/play?task=b8825c91:
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]
# task 289: 64 vs 63 bytes for gold, https://arcprize.org/play?task=b91ae062:
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 290: 84 vs 67 bytes for gold, https://arcprize.org/play?task=b94a9452:
p=lambda g:[[sum({*sum(g,[])})-v for*c,v in zip(*g,r)if any(c)]for r in g if any(r)]
# task 291: 69 vs 61 bytes for gold, https://arcprize.org/play?task=b9b7f026:
p=lambda a:max([[c]]for c in sum(a,a)if[*{b.count(c)for b in a}][2:])
# task 292: 58 vs 56 bytes for gold, https://arcprize.org/play?task=ba26e723:
p=lambda g:[[6-j%3&v%~5for j,v in enumerate(r)]for r in g]
# task 293: 60 vs 59 bytes for gold, https://arcprize.org/play?task=ba97ae07:
p=lambda a:[[d^c^b[0]or d for*_,c,d in zip(*a,b)]for b in a]
# task 294: 76 vs 70 bytes for gold, https://arcprize.org/play?task=bb43febb:
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))
# task 295: 54 bytes, gold, https://arcprize.org/play?task=bbc9ae5d:
p=lambda a:[b:=a[0]]+[b:=b[:1]+b[:-1]for _ in b[2::2]]
# task 296: 63 bytes, gold, https://arcprize.org/play?task=bc1d5164:
p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]
# task 297: 47 vs 43 bytes for gold, https://arcprize.org/play?task=bd4472b8:
p=lambda a:a[:2]+[[b]*len(a[0])for b in a[0]]*2
# task 299: 64 vs 54 bytes for gold, https://arcprize.org/play?task=bdad9b1f:
p=lambda g:[[26%(c+C+R-~r)for c,*_,C in zip(*g)]for r,*_,R in g]
# task 300: 87 bytes, gold, https://arcprize.org/play?task=be94b721:
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))if max(range(1,10),key=sum(a,a).count)in b]
# task 301: 31 bytes, gold, https://arcprize.org/play?task=beb8660c:
p=lambda g,S=sorted:S(map(S,g))
# task 303: 64 vs 62 bytes for gold, https://arcprize.org/play?task=c1d99e64:
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]
# task 304: 93 vs 92 bytes for gold, https://arcprize.org/play?task=c3e719e8:
p=lambda g:[[V*(v==max(f:=sum(g,[]),key=f.count))for v in r for V in R]for r in g for R in g]
# task 305: 74 vs 62 bytes for gold, https://arcprize.org/play?task=c3f564a4:
p=lambda g:[[max(r[j%(n:=len({*r}-{0}))::n])for j in range(16)]for r in g]
# task 306: 82 vs 81 bytes for gold, https://arcprize.org/play?task=c444b776:
p=lambda a:[*map(f:=lambda*b:[max(b[i%10::10])for i in range(len(b))],*map(f,*a))]
# task 307: 52 vs 50 bytes for gold, https://arcprize.org/play?task=c59eb873:
p=eval('lambda a:[[a '+"for a in a for _ in'  ']"*2)
# task 309: 38 bytes, gold, https://arcprize.org/play?task=c8f0f002:
p=lambda a:eval(str(a).replace(*'75'))
# task 310: 96 vs 78 bytes for gold, https://arcprize.org/play?task=c909285e:
import re
p=lambda m:[*map(eval,re.findall((c:=min(s:=str(m)+'[]'*8,key=s.count))+"[^[]*"+c,s))]
# task 311: 32 bytes, gold, https://arcprize.org/play?task=c9e6f938:
p=lambda a:[r+r[::-1]for r in a]
# task 312: 45 vs 44 bytes for gold, https://arcprize.org/play?task=c9f8e694:
p=lambda a:[[e and r[0]for e in r]for r in a]
# task 313: 74 vs 63 bytes for gold, https://arcprize.org/play?task=caa06a1f:
p=lambda g,k=1:-k*g or p(([*zip(*g)][k:len({*g[0]})-1+k]*99)[:len(g)],k-1)
# task 315: 64 vs 63 bytes for gold, https://arcprize.org/play?task=cce03e0d:
p=lambda a:[[d//2*e for d in b for e in c]for b in a for c in a]
# task 318: 61 vs 54 bytes for gold, https://arcprize.org/play?task=ce4f8723:
p=lambda a:[[c|b.pop(0)and 3for c in a.pop(0)]for b in a[5:]]
# task 319: 392 vs 199 bytes for gold, https://arcprize.org/play?task=ce602527:
E=enumerate
def p(g):
 f=sum(g,[]);*r,b=sorted({*f},key=f.count);W,H=len(g[0]),len(g);T={C:{(i,j)for i,r in E(g)for j,v in E(r)if C==v}for C in r}
 for c in r:
  for l in r:
   if T[c]in({(i*2+q+a,j*2+Q+A)for i,j in T[l]for a in(0,1)for A in(0,1)if H>i*2+q+a>-1<j*2+Q+A<W}for q in range(-H*2,H*2)for Q in range(-W*2,W*2)):return[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]
# task 320: 72 vs 68 bytes for gold, https://arcprize.org/play?task=ce9e57f2:
p=lambda a:[[c<<b.pop(0)for c in a.pop(0)]for*b,in(a[:1]*len(a)+a)[::2]]
# task 321: 57 vs 55 bytes for gold, https://arcprize.org/play?task=cf98881b:
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
# task 322: 49 vs 48 bytes for gold, https://arcprize.org/play?task=d037b0a7:
p=lambda a,b=[0]*9:[b:=[*map(max,b,r)]for r in a]
# task 325: 293 vs 184 bytes for gold, https://arcprize.org/play?task=d0f5fe59:
def p(m,R=range):
 z=0;M,N=len(m),len(m[0])
 for i in R(M*N):
  z+=(b:=m[r:=i//N][c:=i%N]>0)
  s=[];q=b*[(r,c)]
  while q:
   (y,x),*q=q;s+=(y,x),
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]*(m[y][x]>0):
    if M>i>-1<j<N:q+=(i,j),
   m[y][x]=0
 return[[8*(r==c)for c in R(z)]for r in R(z)]
# task 326: 30 bytes, gold, https://arcprize.org/play?task=d10ecb37:
p=lambda a:[a[0][:2],a[1][:2]]
# task 327: 90 vs 67 bytes for gold, https://arcprize.org/play?task=d13f3404:
p=lambda m,R=range(6):[[max(3>r-k>-1<c-k<3and m[r-k][c-k]for k in R)for c in R]for r in R]
# task 329: 54 bytes, gold, https://arcprize.org/play?task=d23f8c26:
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]
# task 330: 266 vs 137 bytes for gold, https://arcprize.org/play?task=d2abd087:
def p(m):
 for i in range(99):
  z,*s=0,;q=(m[r:=i//10][c:=i%10]==5)*[(r,c)]
  while q:
   m[r][c]=9;(y,x),*q=q;z+=1;s+=(y,x),
   for i,j in[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
    if-1<i<10>j>-1<5==m[i][j]:m[i][j]=9;q+=(i,j),
  for r,c in s:m[r][c]=1+(z==6)
 return m
# task 332: 61 vs 58 bytes for gold, https://arcprize.org/play?task=d406998b:
p=lambda m:[[len(r)*r.pop(0)%2*3or x for x in[*r]]for r in m]
# task 333: 93 bytes, gold, https://arcprize.org/play?task=d43fd935:
p=lambda a,n=-23:n*a or[(d:=0)or[d:=b.pop()|d*(3in b[:-1])for _ in a]for*b,in zip(*p(a,n+1))]
# task 334: 76 vs 66 bytes for gold, https://arcprize.org/play?task=d4469b4b:
p=lambda m:[[x:=[0,5,0],y:=[5]*3,x],[y,x,x],[z:=[0,0,5],z,y]][max(max(m))-1]
# task 335: 199 vs 126 bytes for gold, https://arcprize.org/play?task=d4a91cb9:
def p(m):
 I=sum(m,[]).index;N=len(m[0])
 for c in range(min(x:=I(2)%N,X:=I(8)%N),max(x,X)+1):m[y:=I(2)//N][c]=4
 for r in range(min(y,Y:=I(8)//N),max(y,Y)+1):m[r][X]=4
 m[y][x]=2;m[Y][X]=8
 return m
# task 336: 115 vs 103 bytes for gold, https://arcprize.org/play?task=d4f3cd78:
import re
p=lambda a,n=-7:n*a or eval(re.sub('0(?=([0, ]*8|(?<=[58], 0))[^)]*5)','8',str([*zip(*p(a,n+1))][::-1])))
# task 337: 46 bytes, gold, https://arcprize.org/play?task=d511f180:
p=lambda g:[[x^84%x%3*13for x in r]for r in g]
# task 338: 104 vs 70 bytes for gold, https://arcprize.org/play?task=d5d6de2d:
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]
# task 339: 37 bytes, gold, https://arcprize.org/play?task=d631b094:
p=lambda a:[[*filter(int,sum(a,[]))]]
# task 346: 111 vs 58 bytes for gold, https://arcprize.org/play?task=d9fac9be:
import re
p=lambda m:[[int(re.findall(r'([1-9], )\1\1.{%d}\1(.), \1.{%d}'%((len(m[0])*3-7,)*2),str(m))[0][1])]]
# task 347: 50 bytes, gold, https://arcprize.org/play?task=dae9d2b5:
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]
# task 348: 101 bytes, gold, https://arcprize.org/play?task=db3e9e38:
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,_ in a[1:]+a[-1:]],n+1)
# task 350: 162 vs 94 bytes for gold, https://arcprize.org/play?task=dbc1a6ce:
def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][1 in m[r][:c]!=1 in m[r][c:]or 1 in a[c::N][:r]!=1 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]
# task 351: 70 vs 68 bytes for gold, https://arcprize.org/play?task=dc0a314f:
p=lambda g:[R[::-1][r.index(3):][:5]for r,R in zip(g,g[::-1])if 3in r]
# task 352: 114 vs 84 bytes for gold, https://arcprize.org/play?task=dc1df850:
import re
p=lambda m,i=3:-i*m or p([*zip(*eval(re.sub(r"0(?=..2|.{%d}2)"%(len(m[0]*3)+4),'1',str(m)))[::-1])],i-1)
# task 353: 104 vs 102 bytes for gold, https://arcprize.org/play?task=dc433765:
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)
# task 354: 105 vs 101 bytes for gold, https://arcprize.org/play?task=ddf7fa4f:
p=lambda a:[*map(f:=lambda b,c=a[0]:b and(d:=[*b,0].index(0)or 1)*[b[0]and max(c[:d])]+f(b[d:],c[d:]),a)]
# task 355: 101 bytes, gold, https://arcprize.org/play?task=de1cd16c:
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]
# task 356: 162 vs 105 bytes for gold, https://arcprize.org/play?task=ded97339:
def p(m,E=enumerate):N=len(m[0]);a=sum(m,[]);return[[[v,v or 8][8 in m[r][:c]!=8 in m[r][c:]or 8 in a[c::N][:r]!=8 in a[c::N][r:]]for c,v in E(l)]for r,l in E(m)]
# task 357: 92 vs 86 bytes for gold, https://arcprize.org/play?task=e179c5f4:
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,x%(l:=len(m[0])-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]
# task 358: 105 vs 97 bytes for gold, https://arcprize.org/play?task=e21d9049:
p=lambda a:[*map(f:=lambda*b:1<(n:=len({*b})-1)and[max(b[i%n::n])for i in range(len(b))]or b,*map(f,*a))]
# task 359: 64 bytes, gold, https://arcprize.org/play?task=e26a3af2:
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]
# task 360: 45 bytes, gold, https://arcprize.org/play?task=e3497940:
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]
# task 362: 136 vs 69 bytes for gold, https://arcprize.org/play?task=e48d4e1a:
p=lambda m,R=range(10):[[(d:=min(set(a:=sum(m,[]))-{0,5}))*(r==a[::10].index(d)+(s:=a.count(5))or c==a.index(d)-s)for c in R]for r in R]
# task 364: 315 vs 166 bytes for gold, https://arcprize.org/play?task=e509e548:
def p(m):
 M,N,*v=len(m),len(m[0])
 for i in range(M*N):
  z,*s=0,;q=(m[r:=i//N][c:=i%N]>2)*[(r,c)]
  while q:(y,x),*q=q;s+=(y,x),;b=0;[(b:=b*2|(M>i>-1<j<N!=3==m[i][j]!=((i,j)in v or(q:=q+[(i,j)]))))for i,j in[(y,x+1),(y+1,x),(y,x-1),(y-1,x)]];v+=(y,x),;z+=696553536>>b*2&3
  for r,c in s:m[r][c]=46%(8+z)
 return m
# task 365: 181 vs 112 bytes for gold, https://arcprize.org/play?task=e50d258f:
def p(m,b=[0]*3):
 for k in range(99):
  R=r=k//10
  while R<10>0<m[R][c:=k%10]:R+=1
  b=max(b,[sum(a:=[l[c:[*m[r],0].index(0,c)]for l in m[r:R]],[]).count(2),-r,-c,a])
 return b[3]
# task 368: 197 vs 142 bytes for gold, https://arcprize.org/play?task=e76a88a6:
def p(m):s=sum(m,[]);a=[x%5>0for x in s];x=a.index(1);w=a[x:].index(i:=0);exec("for j in range((a[x:][::10]+a).index(0)*(m[r:=i//10][c:=i%10]==5)):m[r+j][c:c+w]=s[x+10*j:][:w]\ni+=1\n"*99);return m
# task 369: 118 vs 113 bytes for gold, https://arcprize.org/play?task=e8593010:
p=lambda m,i=91:-i*m or[*zip(*eval(str(p(m,i-1)[::-1]).replace("3220,,,,    331"[i%7%4::4],"2113,,,,211"[i%7%4::4])))]
# task 371: 115 bytes, gold, https://arcprize.org/play?task=e9614598:
def p(a):
	b=sum(a,[]).index;c=b(1);d=b(1,c+1)+c>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a
# task 372: 48 bytes, gold, https://arcprize.org/play?task=e98196ab:
p=lambda a:[b for*b,in map(map,[max]*5,a,a[6:])]
# task 373: 39 bytes, gold, https://arcprize.org/play?task=e9afcf9a:
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]
# task 374: 279 vs 130 bytes for gold, https://arcprize.org/play?task=ea32f347:
def p(m):
 a=[]
 for k in range(99):
  w=(r:=k//10,c:=k%10),
  if m[r][c]>4:
   for x,y in[(0,1),(1,0)]:
    j=r;i=c
    while-1<(j:=j+y)<10>(i:=i+x)>-1!=m[j][i]>4:w+=(j,i),;z=m[j][i]=0
   a+=[len(w),w],
 for _,e in sorted(a)[::-1]:
  for r,c in e:m[r][c]=4**z%7
  z+=1
 return m
# task 375: 53 bytes, gold, https://arcprize.org/play?task=ea786f4a:
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g
# task 376: 30 bytes, gold, https://arcprize.org/play?task=eb281b96:
p=lambda a:(a+a[1:-1])*2+a[:1]
# task 377: 57 vs 55 bytes for gold, https://arcprize.org/play?task=eb5a1d5d:
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]
# task 378: 281 vs 145 bytes for gold, https://arcprize.org/play?task=ec883f72:
def p(m):
 n=len(m);(x,*_,X),(y,*_,Y)=map(sorted,zip(*[(r,c)for i in range(n*n)if m[r:=i//n][c:=i%n]]));a=[(x,y,-1,-1),(x,Y,-1,1),(X,y,1,-1),(X,Y,1,1)]
 for r,c,i,j in a:
  while n>c+j>-1<r+i<n:r+=i;c+=j;m[r][c]=min(set(sum(m,[]))-{0,sorted([m[u][v]for u,v,*_ in a])[1]})
 return m
# task 379: 341 vs 142 bytes for gold, https://arcprize.org/play?task=ecdecbb3:
def p(m,R=range):
 f=lambda m:[*map(list,zip(*m))];a=sum(m:=[f(m),m][t:=8 in m[0]],[]);n=len(m[0])
 for i in R(n*len(m)):
  def g(*a):
   for e in R(*a):
    if m[r][e]>7:
     for j in R(min(c,e),max(c,e)+1):m[r][j]=2
     for i in b' @`!a"Bb':m[r+i//32-2][e+i%4-1]=8
     break
  r=i//n;a[i]==2!=g(c:=i%n,0,-1)!=g(c+1,n)
 return[f(m),m][t]
# task 380: 27 bytes, gold, https://arcprize.org/play?task=ed36ccf7:
p=lambda a:[*zip(*a)][::-1]
# task 382: 145 vs 134 bytes for gold, https://arcprize.org/play?task=f15e1fac:
f=lambda b,*a:[b:=(*b[d>0:-1],*{0,d})for*_,d in[b,*a]]
p=lambda a,n=-3:n*a or p([b:=(c:=[*zip(*a)])[::-1],max(f(*c)[::-1],f(*b))][2in a[-1]],n+1)
# task 384: 65 vs 64 bytes for gold, https://arcprize.org/play?task=f25fbde4:
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))for _ in'  'if 4in b]
# task 385: 25 bytes, gold, https://arcprize.org/play?task=f25ffba3:
p=lambda a:a[:4:-1]+a[5:]
# task 386: 52 bytes, gold, https://arcprize.org/play?task=f2829549:
p=lambda a:[[3>>e+r.pop(0)for e in r[4:]]for r in a]
# task 388: 62 vs 61 bytes for gold, https://arcprize.org/play?task=f5b8619d:
p=lambda a:2*[2*[d or any(c)*8for*c,d in zip(*a,b)]for b in a]
# task 389: 57 bytes, gold, https://arcprize.org/play?task=f76d97a5:
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]
# task 391: 63 bytes, gold, https://arcprize.org/play?task=f8b3ba0a:
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]
# task 392: 320 vs 161 bytes for gold, https://arcprize.org/play?task=f8c80d96:
R=range(10)
J=1j
def p(g):
 S={i*J+j:v for i in R for j in R if(v:=g[i][j])};a={(a*-~k-b*k,d)for d in[-J,1,J,-1]for a in S for b in S if{a+d,a+d*J,b+d,b+d*J}<{*S}for k in R}
 for i,n in a:
  for d in n,n*J:
   I=i
   for*_,k in[S]*12:S[I]=S[k];I=[I+d,i][I+d in[*zip(*a)][0]]
 return[[S.get(i*J+j,5)for j in R]for i in R]
# task 393: 63 bytes, gold, https://arcprize.org/play?task=f8ff0b80:
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# task 394: 249 vs 91 bytes for gold, https://arcprize.org/play?task=f9012d9b:
def p(m,p=0,R=range):
 while n:=len(m):
  t={};b=0;h=[];p+=1
  for i in R(n*n):
   x=m[r:=i%n][c:=i//n];k=r%p,c%p;h+=[(r,c)]*(x<1)
   if x:b|=t.get(k,x)!=x;t[k]=x
  if~-b:x,y=h[0];s=R(int(len(h)**.5));return[[t[(x+r)%p,(y+c)%p]for c in s]for r in s]
# task 395: 57 vs 53 bytes for gold, https://arcprize.org/play?task=fafffa47:
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(3)]for b in a]
# task 396: 268 vs 220 bytes for gold, https://arcprize.org/play?task=fcb5c309:
def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for i in range(N*M):
  Y=y=i%N;X=x=i//N
  while(m[y]*2)[X]==b<M>X:X+=1
  while Y<N!=(m[Y]*2)[x]==b:Y+=1;z=max(z,[sum(sum(a:=[[d*(e>0)for e in l[x:X]]for l in m[y:Y]],[]))//d,a])
 return z[1]
# task 397: 130 vs 121 bytes for gold, https://arcprize.org/play?task=fcc82909:
p=lambda m,k=0:exec('r=k//9;c=k%9;exec("m[r+2][c:c+2]=3,3;r+=1;"*len(a:={*m[r][c:c+2]+m[r+1][c:c+2]})*(not{0,3}&a));k+=1;'*81)or m
# task 398: 80 vs 77 bytes for gold, https://arcprize.org/play?task=feca6190:
def p(a):l=25-5*a[0].count(0);return[((~-l*[0]+a[0])*2)[i:i+l]for i in range(l)]
# task 399: 64 bytes, gold, https://arcprize.org/play?task=ff28f65a:
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]
# task 400: 70 vs 67 bytes for gold, https://arcprize.org/play?task=ff805c23:
p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]
