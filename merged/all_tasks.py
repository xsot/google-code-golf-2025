# task 1: 61 bytes, gold, https://arcprize.org/play?task=07bbfb7:
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]
# task 2: 98 vs 90 bytes for gold, https://arcprize.org/play?task=0d62c1b:
p=lambda a,n=-62:[*map(lambda*b,d=0:[(c%2|d//3)*(d:=c+(n>c)*4)for c in b][::-1],*n*a or p(a,n+1))]
# task 3: 60 vs 58 bytes for gold, https://arcprize.org/play?task=17c7c7b:
p=lambda g:[[v*2for v in l]for l in g+g[g[:2]!=g[4:]:][2:5]]
# task 6: 51 bytes, gold, https://arcprize.org/play?task=520fde7:
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
# task 7: 67 vs 65 bytes for gold, https://arcprize.org/play?task=5269061:
p=lambda a,*b:[[max(sum(a,b:=[*b,0,0])[2::3])for _ in a]for _ in a]
# task 8: 94 bytes, gold, https://arcprize.org/play?task=5f2a901:
p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]
# task 10: 72 vs 69 bytes for gold, https://arcprize.org/play?task=8ed6ac7:
p=lambda a:[[sum(c<e*s for*s,in zip(*a))for*c,e in zip(*a,r)]for r in a]
# task 16: 46 vs 43 bytes for gold, https://arcprize.org/play?task=d3d703e:
p=lambda m:[[b'AA	'[i]for i in m[0]]]*3
# task 17: 120 bytes, gold, https://arcprize.org/play?task=dfd9992:
p=lambda a,n=1:[*map(f:=lambda*b:[max(b[i%n::n])for i in range(21)],*map(f,*a))]*any(b[n:]==b[:-n]for b in a)or p(a,n+1)
# task 21: 64 vs 57 bytes for gold, https://arcprize.org/play?task=190e5a7:
p=eval('lambda a:[[a '+'for a in-~min(map(a.count,a))*a[:1]]'*2)
# task 22: 101 vs 91 bytes for gold, https://arcprize.org/play?task=37eaa0f:
R=-1,0,1
p=lambda g:[[max(f[I+i*11+j]for I in range(121)if(f:=sum(g,[]))[I]==5)for j in R]for i in R]
# task 23: 218 vs 205 bytes for gold, https://arcprize.org/play?task=50deff5:
def p(g,*S):
 w=len(g[0])
 for c in-6&len(S)+4,5:
  for I in S:g[I//w][I%w]=c
  try:f=sum(g,[])*2;i=f.index(5);[{5}-{c}=={f[I]for I in s}!=g==p(g,i,*s)>1for s in[[w+i,1+i,w-~i],[i+1,i+2],[i+w,i+w*2]]]
  except:return g
# task 24: 65 vs 62 bytes for gold, https://arcprize.org/play?task=78fcbfb:
p=lambda a:[[max({*r}-{2})or(2in c)*2for c in zip(*a)]for r in a]
# task 25: 153 bytes, gold, https://arcprize.org/play?task=a07d186:
E=enumerate
p=lambda g,k=-1:g*k or p([[max([k*(2>i*i<=k in[r,r[:j],r[j:]][i])for i,k in E(map(min,g),-j)if k]or[v])for j,v in E(r)]for r in zip(*g)],k+1)
# task 26: 52 bytes, gold, https://arcprize.org/play?task=b2d62fb:
p=lambda a:[[8>>i+b.pop(0)for i in b[4:]]for b in a]
# task 28: 70 vs 63 bytes for gold, https://arcprize.org/play?task=bfc4729:
p=lambda g:[((j%11*[max(g[j%8])]+[0]*8)*2)[:10]for j in b'b"b""ooWoW']
# task 29: 118 vs 115 bytes for gold, https://arcprize.org/play?task=c786137:
p=lambda a:min([d in sum(i:=[b[1:-1]for*b,in zip(*[b for*b,in zip(*a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]
# task 31: 47 vs 45 bytes for gold, https://arcprize.org/play?task=cf80156:
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)))]
# task 32: 39 bytes, gold, https://arcprize.org/play?task=e0a9b12:
p=lambda a:[*zip(*map(sorted,zip(*a)))]
# task 33: 77 bytes, gold, https://arcprize.org/play?task=e32b0e9:
p=lambda g:[[v+(v<V)*R[5]for v,V in zip(r,R[:6]*3)]for r,R in zip(g,g[:6]*3)]
# task 39: 65 vs 60 bytes for gold, https://arcprize.org/play?task=013d3e2:
p=lambda a:[b[:3]for*b,in zip(*filter(any,zip(*a)))if any(b)][:3]
# task 41: 49 bytes, gold, https://arcprize.org/play?task=2168020:
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]
# task 43: 57 bytes, gold, https://arcprize.org/play?task=281f1f4:
p=lambda a:[[c*b[-1]//9|b.pop(0)for c in a[0]]for*b,in a]
# task 49: 87 vs 81 bytes for gold, https://arcprize.org/play?task=3b5c85d:
p=lambda a:[b.count(e)*[e]for b in a if(e:=min(set(d:=sum(a,[]))-{0},key=d.count))in b]
# task 52: 41 vs 40 bytes for gold, https://arcprize.org/play?task=5d8a9c8:
p=lambda a:[3*[1//len({*b})*5]for b in a]
# task 53: 21 bytes, gold, https://arcprize.org/play?task=5ff71a9:
p=lambda a:(a+a)[2:5]
# task 56: 43 vs 40 bytes for gold, https://arcprize.org/play?task=7a28665:
p=lambda g:[[5^(g[0][0]>0)-3*~(g[0][2]>0)]]
# task 57: 49 bytes, gold, https://arcprize.org/play?task=8bf18c6:
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]
# task 60: 48 bytes, gold, https://arcprize.org/play?task=9c11459:
p=lambda g:[r[:1]*5+[5*(l>0)]+5*[l]for*r,l in g]
# task 67: 33 bytes, gold, https://arcprize.org/play?task=dee498d:
p=lambda a:[b[:len(a)]for b in a]
# task 72: 61 vs 54 bytes for gold, https://arcprize.org/play?task=428a4f5:
p=lambda a:[[3*(c!=b.pop(0))for c in a.pop(0)]for b in a[7:]]
# task 73: 46 bytes, gold, https://arcprize.org/play?task=618c87e:
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]
# task 82: 50 bytes, gold, https://arcprize.org/play?task=ac3eb23:
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3
# task 83: 40 bytes, gold, https://arcprize.org/play?task=af2c5a8:
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 87: 36 bytes, gold, https://arcprize.org/play?task=c9b0459:
p=lambda a:[b[::-1]for b in a[::-1]]
# task 100: 88 vs 54 bytes for gold, https://arcprize.org/play?task=445eab21:
p=lambda a:[[max(range(1,10),key=[sum({*b}&{*c})for c in zip(*a)for b in a].count)]*2]*2
# task 103: 29 bytes, gold, https://arcprize.org/play?task=44f52bb0:
p=lambda a:[[a==a[::-1]or 7]]
# task 105: 154 vs 148 bytes for gold, https://arcprize.org/play?task=4612dd53:
A=any
p=lambda g,k=-3:k*g or p([[v or A([r*(m:=[*map(A,g)])[j],sum(map(bool,r))//4*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1],k+1)
# task 108: 58 vs 56 bytes for gold, https://arcprize.org/play?task=46f33fce:
p=eval('lambda a:[[a '+"for a in a[1::2]for _ in' '*4]"*2)
# task 113: 25 bytes, gold, https://arcprize.org/play?task=496994bd:
p=lambda a:a[:5]+a[4::-1]
# task 115: 54 bytes, gold, https://arcprize.org/play?task=4be741c5:
s={}.fromkeys
p=lambda a:[*s(zip(*s(zip(*map(s,a)))))]
# task 116: 20 bytes, gold, https://arcprize.org/play?task=4c4377d9:
p=lambda a:a[::-1]+a
# task 126: 57 vs 54 bytes for gold, https://arcprize.org/play?task=54d82841:
p=lambda a:a[:-1]+[[4*(sum(c)<2*max(c))for c in zip(*a)]]
# task 129: 47 bytes, gold, https://arcprize.org/play?task=5582e5ca:
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3
# task 130: 65 bytes, gold, https://arcprize.org/play?task=5614dbcf:
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]
# task 135: 32 bytes, gold, https://arcprize.org/play?task=5bd6f4ac:
p=lambda a:[b[6:]for b in a[:3]]
# task 140: 36 bytes, gold, https://arcprize.org/play?task=6150a2bd:
p=lambda a:[b[::-1]for b in a[::-1]]
# task 142: 40 bytes, gold, https://arcprize.org/play?task=62c24649:
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# task 144: 59 vs 53 bytes for gold, https://arcprize.org/play?task=6430c8c4:
p=lambda a:[[3>>c+b.pop(0)for c in a.pop(0)]for b in a[5:]]
# task 146: 58 bytes, gold, https://arcprize.org/play?task=662c240a:
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
# task 150: 30 bytes, gold, https://arcprize.org/play?task=67a3c6ac:
p=lambda g:[r[::-1]for r in g]
# task 152: 40 bytes, gold, https://arcprize.org/play?task=67e8384a:
p=lambda a:[r+r[::-1]for r in a+a[::-1]]
# task 155: 18 bytes, gold, https://arcprize.org/play?task=68b16354:
p=lambda a:a[::-1]
# task 162: 132 vs 97 bytes for gold, https://arcprize.org/play?task=6cf79266:
r=range(324)
def p(a):
	for i in r:
		b=a[i%18:][:3];i//=18;z=any(max([*zip(*b)][i:i+3]))
		for k in r:b[k%5%3][i+k%3]**=z
	return a
# task 164: 32 bytes, gold, https://arcprize.org/play?task=6d0aefbc:
p=lambda a:[b+b[::-1]for b in a]
# task 166: 65 vs 61 bytes for gold, https://arcprize.org/play?task=6d75e8bb:
p=lambda a:[[d or any(b)*2*any(c)for*c,d in zip(*a,b)]for b in a]
# task 171: 54 bytes, gold, https://arcprize.org/play?task=6f8cd79b:
p=lambda a:[*map(f:=lambda*b:[8,*b[2:],8],*map(f,*a))]
# task 172: 20 bytes, gold, https://arcprize.org/play?task=6fa7a44f:
p=lambda a:a+a[::-1]
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
# task 197: 54 bytes, gold, https://arcprize.org/play?task=82819916:
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]
# task 198: 122 bytes, gold, https://arcprize.org/play?task=83302e8f:
p=lambda a,n=-23:n*a or p([*map(lambda*b,d=1:[[c,4-(sum(25>>e&d for e in b)>9)][9>>c&(d:=c!=4)]for c in b][::-1],*a)],n+1)
# task 202: 109 vs 107 bytes for gold, https://arcprize.org/play?task=855e0971:
p=lambda a:(len({*a[0]}-{0})<2)*[[*map(min,*[c for c in a if max(b)in c])]for b in a]or[*zip(*p([*zip(*a)]))]
# task 203: 69 vs 64 bytes for gold, https://arcprize.org/play?task=85c4e7cd:
p=lambda a:[[(d:=a[l:=len(a)//2])[l+d.index(c)]for c in b]for b in a]
# task 207: 81 bytes, gold, https://arcprize.org/play?task=88a62173:
p=eval('lambda a:[[min(b:=sum(a,()),key=b.count)'+'for*a,in map(zip,a,a[3:])]'*2)
# task 210: 20 bytes, gold, https://arcprize.org/play?task=8be77c9e:
p=lambda a:a+a[::-1]
# task 211: 48 bytes, gold, https://arcprize.org/play?task=8d5021e8:
p=lambda g:[l[::-1]+l for l in(g[::-1]+g)*2][:9]
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
# task 221: 103 vs 94 bytes for gold, https://arcprize.org/play?task=91413438:
def p(a):r=range(d:=str(a).count('0'));return[[c*(j<9+d*~i)for j in r for c in b]for i in r for b in a]
# task 223: 52 vs 51 bytes for gold, https://arcprize.org/play?task=9172f3a0:
p=lambda a:eval("[[a "+"for a in a for _ in%s]"%a*2)
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
# task 247: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a3325580:
p=lambda a:(m:=max(map(c:=(b:=sum(zip(*a),())).count,{*b}-{0})))*[[*{d:0for d in b if c(d)==m}]]
# task 249: 26 bytes, gold, https://arcprize.org/play?task=a416b8f3:
p=lambda a:[r*2for r in a]
# task 251: 94 vs 89 bytes for gold, https://arcprize.org/play?task=a5313dff:
p=lambda a,n=-42:[*map(lambda*b,d=0:[max(n,c*(d+(d:=c)>1))for c in b][::-1],*n*a or p(a,n+1))]
# task 252: 61 vs 57 bytes for gold, https://arcprize.org/play?task=a5f85a15:
p=lambda a:[(i:=1)*[[c,c and 4][i:=1-i]for c in b]for b in a]
# task 257: 81 bytes, gold, https://arcprize.org/play?task=a68b268e:
p=eval('lambda a:[[next(filter(int,sum(a,())),0)'+'for*a,in map(zip,a,a[5:])]'*2)
# task 258: 61 bytes, gold, https://arcprize.org/play?task=a699fb00:
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))
# task 259: 86 vs 85 bytes for gold, https://arcprize.org/play?task=a740d043:
p=lambda a,n=-23:n*a or p([[d*(d>1)for d in c]for c in zip(*a[a<[[0]*9]:])][::-1],n+1)
# task 261: 47 bytes, gold, https://arcprize.org/play?task=a79310a0:
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]
# task 262: 42 vs 39 bytes for gold, https://arcprize.org/play?task=a85d4709:
p=lambda a:[3*[-b.index(5)%3+2]for b in a]
# task 267: 57 vs 46 bytes for gold, https://arcprize.org/play?task=aabf363d:
p=lambda a:[[(d:=a[-1][0])*(0<c!=d)for c in b]for b in a]
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
# task 276: 38 bytes, gold, https://arcprize.org/play?task=b1948b0a:
p=lambda a:eval(str(a).replace(*'62'))
# task 278: 179 vs 118 bytes for gold, https://arcprize.org/play?task=b27ca6d3:
def p(g):E=enumerate;L=abs;S={(i,j)for i,r in E(g)for j,v in E(r)if v};return[[v or 3*any(L(a-I)+L(A-J)==1==L(i-I)|L(j-J)for a,A in S for I,J in S)for j,v in E(r)]for i,r in E(g)]
# task 282: 89 vs 86 bytes for gold, https://arcprize.org/play?task=b60334d2:
p=lambda a:[*map(f:=lambda*b:[c|e|d>>2for c,d,e in zip([0,*b],b,b[1:]+(0,))],*map(f,*a))]
# task 283: 94 vs 86 bytes for gold, https://arcprize.org/play?task=b6afb2da:
z=0,
p=lambda a:[*map(f:=lambda*b:[c[0]*sum(c,7)%32%6for c in zip(b,z+b,b[1:]+z)],*map(f,*a))]
# task 287: 63 vs 56 bytes for gold, https://arcprize.org/play?task=b8825c91:
p=lambda a:[[max({c,b.pop()}-{4})for c in a.pop()]for*b,in[*a]]
# task 289: 64 vs 63 bytes for gold, https://arcprize.org/play?task=b91ae062:
p=lambda a:eval('[[a '+"for a in a for _ in[*{*'%s'}][5:]]"%a*2)
# task 291: 69 vs 61 bytes for gold, https://arcprize.org/play?task=b9b7f026:
p=lambda a:max([[c]]for c in sum(a,a)if[*{b.count(c)for b in a}][2:])
# task 292: 58 vs 56 bytes for gold, https://arcprize.org/play?task=ba26e723:
p=lambda g:[[6-j%3&v%~5for j,v in enumerate(r)]for r in g]
# task 295: 54 bytes, gold, https://arcprize.org/play?task=bbc9ae5d:
p=lambda a:[b:=a[0]]+[b:=b[:1]+b[:-1]for _ in b[2::2]]
# task 296: 63 bytes, gold, https://arcprize.org/play?task=bc1d5164:
p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]
# task 297: 47 vs 43 bytes for gold, https://arcprize.org/play?task=bd4472b8:
p=lambda a:a[:2]+[[b]*len(a[0])for b in a[0]]*2
# task 300: 87 bytes, gold, https://arcprize.org/play?task=be94b721:
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))if max(range(1,10),key=sum(a,a).count)in b]
# task 301: 31 bytes, gold, https://arcprize.org/play?task=beb8660c:
p=lambda g,S=sorted:S(map(S,g))
# task 303: 64 vs 62 bytes for gold, https://arcprize.org/play?task=c1d99e64:
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]
# task 306: 82 vs 81 bytes for gold, https://arcprize.org/play?task=c444b776:
p=lambda a:[*map(f:=lambda*b:[max(b[i%10::10])for i in range(len(b))],*map(f,*a))]
# task 307: 52 vs 50 bytes for gold, https://arcprize.org/play?task=c59eb873:
p=eval('lambda a:[[a '+"for a in a for _ in'  ']"*2)
# task 309: 38 bytes, gold, https://arcprize.org/play?task=c8f0f002:
p=lambda a:eval(str(a).replace(*'75'))
# task 311: 32 bytes, gold, https://arcprize.org/play?task=c9e6f938:
p=lambda a:[r+r[::-1]for r in a]
# task 312: 45 vs 44 bytes for gold, https://arcprize.org/play?task=c9f8e694:
p=lambda a:[[e and r[0]for e in r]for r in a]
# task 315: 64 vs 63 bytes for gold, https://arcprize.org/play?task=cce03e0d:
p=lambda a:[[d//2*e for d in b for e in c]for b in a for c in a]
# task 318: 61 vs 54 bytes for gold, https://arcprize.org/play?task=ce4f8723:
p=lambda a:[[c|b.pop(0)and 3for c in a.pop(0)]for b in a[5:]]
# task 321: 57 vs 55 bytes for gold, https://arcprize.org/play?task=cf98881b:
p=lambda m:[[r.pop(0)or r[4]or r[9]for _ in m]for r in m]
# task 322: 49 vs 48 bytes for gold, https://arcprize.org/play?task=d037b0a7:
p=lambda a,b=[0]*9:[b:=[*map(max,b,r)]for r in a]
# task 326: 30 bytes, gold, https://arcprize.org/play?task=d10ecb37:
p=lambda a:[a[0][:2],a[1][:2]]
# task 329: 54 bytes, gold, https://arcprize.org/play?task=d23f8c26:
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]
# task 337: 46 bytes, gold, https://arcprize.org/play?task=d511f180:
p=lambda g:[[x^84%x%3*13for x in r]for r in g]
# task 339: 37 bytes, gold, https://arcprize.org/play?task=d631b094:
p=lambda a:[[*filter(int,sum(a,[]))]]
# task 346: 111 vs 58 bytes for gold, https://arcprize.org/play?task=d9fac9be:
import re
p=lambda m:[[int(re.findall(r'([1-9], )\1\1.{%d}\1(.), \1.{%d}'%((len(m[0])*3-7,)*2),str(m))[0][1])]]
# task 347: 50 bytes, gold, https://arcprize.org/play?task=dae9d2b5:
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]
# task 351: 70 vs 68 bytes for gold, https://arcprize.org/play?task=dc0a314f:
p=lambda g:[R[::-1][r.index(3):][:5]for r,R in zip(g,g[::-1])if 3in r]
# task 353: 104 vs 102 bytes for gold, https://arcprize.org/play?task=dc433765:
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)
# task 355: 101 bytes, gold, https://arcprize.org/play?task=de1cd16c:
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]
# task 360: 45 bytes, gold, https://arcprize.org/play?task=e3497940:
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]
# task 371: 115 bytes, gold, https://arcprize.org/play?task=e9614598:
def p(a):
	b=sum(a,[]).index;c=b(1);d=b(1,c+1)+c>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a
# task 372: 48 bytes, gold, https://arcprize.org/play?task=e98196ab:
p=lambda a:[b for*b,in map(map,[max]*5,a,a[6:])]
# task 373: 39 bytes, gold, https://arcprize.org/play?task=e9afcf9a:
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]
# task 375: 53 bytes, gold, https://arcprize.org/play?task=ea786f4a:
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g
# task 376: 30 bytes, gold, https://arcprize.org/play?task=eb281b96:
p=lambda a:(a+a[1:-1])*2+a[:1]
# task 377: 57 vs 55 bytes for gold, https://arcprize.org/play?task=eb5a1d5d:
p=lambda g,*a:[y for*y,in zip(*a or p(g,*g))if g!=(g:=y)]
# task 380: 27 bytes, gold, https://arcprize.org/play?task=ed36ccf7:
p=lambda a:[*zip(*a)][::-1]
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
# task 393: 63 bytes, gold, https://arcprize.org/play?task=f8ff0b80:
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# task 395: 57 vs 53 bytes for gold, https://arcprize.org/play?task=fafffa47:
p=lambda a:[[2>>c+c+b.pop(0)for c in a.pop(3)]for b in a]
# task 398: 80 vs 77 bytes for gold, https://arcprize.org/play?task=feca6190:
def p(a):l=25-5*a[0].count(0);return[((~-l*[0]+a[0])*2)[i:i+l]for i in range(l)]
# task 399: 64 bytes, gold, https://arcprize.org/play?task=ff28f65a:
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]
# task 400: 70 vs 67 bytes for gold, https://arcprize.org/play?task=ff805c23:
p=lambda g:[R[::-1][r.index(1):][:5]for r,R in zip(g,g[::-1])if 1in r]
