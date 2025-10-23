# ❌ task 1: 61 vs 58 bytes for gold, https://arcprize.org/play?task=007bbfb7
p=lambda a:[[d&e for d in b for e in c]for b in a for c in a]
# 💎 task 2: 88 bytes, gold, https://arcprize.org/play?task=00d62c1b
p=lambda a,n=11:-n*a or[*map(lambda*b,d=0:[d:=c^c-0**n>>d&4for c in b][::-1],*p(a,n-1))]
# 🥇 task 3: 58 bytes, gold, https://arcprize.org/play?task=017c7c7b
p=lambda g:[[v*2for v in l]for l in g+g[g[:3]*2==g:][2:5]]
# 💎 task 4: 73 bytes, gold, https://arcprize.org/play?task=025d127b
import re;p=lambda i:eval(re.sub(r"(.),(?=.*\1.*0, \1)",r"0,\1|",str(i)))
# 🥉 task 5: 209 (280 unzipped) vs 183 bytes for gold, https://arcprize.org/play?task=045e512c
def p(i):r=max([[(e,a)for e in range(21)[g:g+3]for a in range(21)[y:y+3]if i[e][a]]for g in range(21)for y in range(21)],key=len);return[[max(((y-o*f,g-o*n)in r)*i[e+f][a+n]for e,a in r for f in[-4,0,4]for n in[-4,0,4]for o in range(21)[1:4])for g in range(21)]for y in range(21)]
# 🥇 task 6: 51 bytes, gold, https://arcprize.org/play?task=0520fde7
p=lambda a:[[2*c*b.pop(0)for c in b[4:]]for b in a]
# 🥉 task 7: 63 vs 62 bytes for gold, https://arcprize.org/play?task=05269061
p=lambda a:[*zip(*[(max(sum(a,a)[x::3])for x in[7,8,9]*17)]*7)]
# 🥈 task 8: 90 vs 84 bytes for gold, https://arcprize.org/play?task=05f2a901
p=lambda g:exec('*G,f=0,\nfor r in g:M=max(r);f|=M;G[M-f&11-f:0]=r,\ng[:]=zip(*G);'*4)or g
# 🥇 task 9: 109 bytes, gold, https://arcprize.org/play?task=06df4c85
p=lambda g,E=enumerate:[[max({*r[:j+1]}&{*r[j::3]}|{*c[:i]}&{*c[i::3]})for j,c in E(zip(*g))]for i,r in E(g)]
# 💎 task 10: 67 bytes, gold, https://arcprize.org/play?task=08ed6ac7
p=lambda g:[g:=[V*-1*-1or v*sum(r)%6for V,v in zip(g,r)]for r in g]
# 💎 task 11: 114 bytes, gold, https://arcprize.org/play?task=09629e4f
p=eval("lambda a:max(a*(not'8'in'%s'%a)"+f"for*a,in[*map(zip,a,a,a{',[a[3]]*9,*[a[%d:]]*3'*2%(1,2)})][::4]"*2+')')
# 🥈 task 12: 132 vs 126 bytes for gold, https://arcprize.org/play?task=0962bcdd
import re;p=lambda i:[i:=eval(re.sub("(([^0]).{37}([^0]), )0(, 0.{31})0, 0,",r"\1\2\4\3,0,\2+",str([*zip(*i[::-1])])))for _ in i][7]
# 💎 task 13: 136 bytes, gold, https://arcprize.org/play?task=0a938d79
def p(i):*v,=map(max,*i);*_,f,r=sorted(map(v.index,v));N=len(v);return i[N:]and[*zip(*p([*zip(*i)]))]or[(v[:f]+v[f:2*r-f]*N)[:N]]*len(i)
# 🥈 task 14: 68 vs 67 bytes for gold, https://arcprize.org/play?task=0b148d64
p=lambda i,*I:[w for*w,r in zip(*I or p(zip(*i),*i),i)if[*{*r}][2:]]
# 💎 task 15: 92 bytes, gold, https://arcprize.org/play?task=0ca9ddb6
p=lambda i,k=-3:i*k or[i:=[r.pop()|4*(k==2)|7*((k:=K)==1)for K in i]for*r,in zip(*p(i,k+1))]
# 🥇 task 16: 43 bytes, gold, https://arcprize.org/play?task=0d3d703e
p=lambda m:[[109//i&12%i+7for i in m[0]]]*3
# 🥈 task 17: 102 vs 99 bytes for gold, https://arcprize.org/play?task=0dfd9992
p=lambda g:[g:=[*zip(*[max(a*all(len({*r,0})<3for r in zip(b,a))for a in g)for b in g])]for _ in g][1]
# 💎 task 18: 283 (409 unzipped) bytes, gold, https://arcprize.org/play?task=0e206a2e
def p(g):G={i*1j+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g};[(s:={j},[abs(x-a)<2==s.add(x)for x in[*G]*5for a in[*s]],[2for a in[*s][4:]for a in[1,3,10,11]for O in[*G]if all(G[x]in(max([G[x]for x in[*G]],key=[G[x]for x in[*G]].count),G.get((x-j-a//4*(x-j).real)*1j**a+O))for x in s)for x in s for i,g[int(i.imag)][int(i.real)]in(((x-j-a//4*(x-j).real)*1j**a+O,G[x]),(x,0))])for j in[*G]];return g
# 💎 task 19: 104 bytes, gold, https://arcprize.org/play?task=10fcaaa3
*z,p=[0]*9,eval('lambda a:[[a[1][1]or 8*any(sum(a,())[::2])'+'for*a,in map(zip,z+a+a,a+a,a[1:]+a+z)]'*2)
# 💎 task 20: 139 bytes, gold, https://arcprize.org/play?task=11852cab
S='+[*map(any,g:=[*zip(*g)])].index(1)'*2
p=eval(f"lambda g:[g:=[[g[J][I]|((g*2)[I-{S}]*2)[4{S}-J]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")
# 💎 task 21: 51 bytes, gold, https://arcprize.org/play?task=1190e5a7
p=lambda i:i*-1*-1or-~min(map(i.count,i))*[p(i[0])]
# 🥉 task 22: 95 vs 91 bytes for gold, https://arcprize.org/play?task=137eaa0f
p=lambda i:[[*map(max,*[s[t:t+3]for t in range(121)if(s:=sum(i,[]))[t-x]==5])]for x in b'mx\n']
# 🥉 task 23: 202 vs 195 bytes for gold, https://arcprize.org/play?task=150deff5
import re;p=lambda i,w=2:s!=(r:=re.sub(("5(, )?"*3,"5, 5(.%s)5, 5"%{k:=len(i[0])*3-2},"5(.%s)?"%{k+3}*3)[w],w%2*r"8,8\1 8,8"or r"2\1 2\2 2\3",s,1))and p(eval(r))or w and p(i,w-1)if"5"in(s:=str(i))else i
# 🥇 task 24: 62 bytes, gold, https://arcprize.org/play?task=178fcbfb
p=lambda i:[[3%-~sum(x)or(2in y)*2for y in zip(*i)]for x in i]
# 🥈 task 25: 134 vs 131 bytes for gold, https://arcprize.org/play?task=1a07d186
p=lambda g:[[sum({v}&{*r[:j]}|{*r[j:]}&{m[j],m[j:=j+1]})for v in m[2:]]for r in g if any(m:=[0,*min(g),j:=0])]or[*zip(*p([*zip(*g)]))]
# 🥇 task 26: 52 bytes, gold, https://arcprize.org/play?task=1b2d62fb
p=lambda a:[[8>>i+b.pop(0)for i in b[4:]]for b in a]
# 🥇 task 27: 103 bytes, gold, https://arcprize.org/play?task=1b60fb0c
p=lambda g,r=range(10):[[(g[i][j]^-g[C:=sum(map(max,*g,*zip(*g)))%2+~i][C+i-j])%3for j in r]for i in r]
# ❌ task 28: 66 vs 63 bytes for gold, https://arcprize.org/play?task=1bfc4729
p=lambda g:[(sorted(g[j%8])[j%11:]*j)[-10:]for j in b'*"*""oowow']
# 🥉 task 29: 117 vs 108 bytes for gold, https://arcprize.org/play?task=1c786137
exec("p=lambda a:min([d in sum(i:="+'[b[1:-1]for*b,in zip(*'*2+"a)if d in b])if{d}<{*b}],a),i]for d in sum(a,a))[1]")
# 🥇 task 30: 94 bytes, gold, https://arcprize.org/play?task=1caeab9d
def p(i):*h,=map(max,*i);H=h.index;j=H(1);return[[c*x[(j:=j%10+1)+~H(c)]for c in h]for x in i]
# 🥇 task 31: 45 bytes, gold, https://arcprize.org/play?task=1cf80156
p=lambda a,*n:[*filter(any,zip(*n or p(*a)))]
# 🥇 task 32: 39 bytes, gold, https://arcprize.org/play?task=1e0a9b12
p=lambda a:[*zip(*map(sorted,zip(*a)))]
# 🥇 task 33: 73 bytes, gold, https://arcprize.org/play?task=1e32b0e9
p=lambda g,t=[],s=0:g*0!=0and[*map(p,g,(t+g)[:6]*3,[g[5]]*17)]or(t>g)*s|g
# 🥉 task 34: 128 vs 125 bytes for gold, https://arcprize.org/play?task=1f0c79e5
import re;p=lambda i,k=7:-k*i or[*zip(*eval(re.sub("(?=(.{32})*(., |.{29})?2, [^0].{25}([^02]))\d","\\3",str(p(i,k-1)))))][::-1]
# 🥇 task 35: 83 bytes, gold, https://arcprize.org/play?task=1f642eb9
p=lambda i,k=3:-k*i or[[k:=i[y!=8+k*2]or y for y in i]for i[::-1]in zip(*p(i,k-1))]
# ❌ task 36: 86 vs 75 bytes for gold, https://arcprize.org/play?task=1f85a75f
p=lambda a,c=1,*n:(len(d:=[b for*b,in zip(*n or p(a,c,*a))if c in b])<6)*d or p(a,c+1)
# 💎 task 37: 104 bytes, gold, https://arcprize.org/play?task=1f876c06
import re;p=lambda g,k=9:-k*g or p(eval(re.sub(r"(?<=(.).{28})(?=(.{29})+\1)0",r"\1",str(g)))[::-1],k-1)
# 🥇 task 38: 51 bytes, gold, https://arcprize.org/play?task=1fad071e
p=lambda g:[(str(g).count('1, 1')*[1]+[0]*9)[:9:2]]
# 🥇 task 39: 60 bytes, gold, https://arcprize.org/play?task=2013d3e2
p=lambda a,n=7:-n*a[:3]or p([*zip(*a[1-any(a[0]):3+n])],n-1)
# 🥇 task 40: 69 bytes, gold, https://arcprize.org/play?task=2204b7a8
p=lambda i,c=50:[[y%~y&i[(c:=c-1)>>9][~c//5%-2]for y in x]for x in i]
# 🥇 task 41: 49 bytes, gold, https://arcprize.org/play?task=22168020
p=lambda a,b=0:[[e|(b:=b^e)for e in r]for r in a]
# 💎 task 42: 134 bytes, gold, https://arcprize.org/play?task=22233c11
p=lambda g,Q=range(10):[g:=[[g[j][~i]|g[j-C-C][~i+C]*g[j-C][~i+C+C]%~(i>C<j)%9for j in Q]for i in Q]for C in[sum(b'%r'%g)//38%4]*4][3]
# 🥇 task 43: 56 bytes, gold, https://arcprize.org/play?task=2281f1f4
p=lambda a:[[c+b[-1]&2|b.pop(0)for c in a[0]]for*b,in a]
# 🥈 task 44: 213 (272 unzipped) vs 195 bytes for gold, https://arcprize.org/play?task=228f6490
p=lambda n:[n:=[[i^r*(1&(m:=m>>1)>>99or i==r)for i in i]for r in{*sum(n,[])}if bin(sum((sum(n,[])[i]==r)<<i+9for i in range(100)))in bin(m:=sum((sum(n,[])[i]<5in{*sum(n,[])[i//10*10:i]}&{*sum(n,[])[i:i//10*10+10]})<<i+100for i in range(50)))for i in n][::-1]for i in n][1]
# 🥇 task 45: 45 bytes, gold, https://arcprize.org/play?task=22eb0ac0
p=lambda g:[10*r[:r[0]==r[9]]or r for r in g]
# 🥇 task 46: 168 bytes, gold, https://arcprize.org/play?task=234bbc79
p=lambda i,n=3,Z=zip:[*Z(*[[y%~y&max({*p,*x,*q}-{5})for y in x*3][n:n+3]for*x,p,q in Z(*i,[[],*Z(*i)],[*Z(*i),[5]][1:])if any(x)or(n:=n-[*p,5].index(5)+q.index(5))*0])]
# 🥇 task 47: 55 bytes, gold, https://arcprize.org/play?task=23581191
p=lambda g:[[sum({*r+c})%13for*c,in zip(*g)]for r in g]
# 🥉 task 48: 118 vs 92 bytes for gold, https://arcprize.org/play?task=239be575
p=lambda m,i=99,s="":-i*[[8-8*("2"in'%s'%m)]]or p([*zip(*eval(str(m).replace("282"[i%3]+s,"1"+s,2)))][::-1],i-1,", 1")
# 🥇 task 49: 81 bytes, gold, https://arcprize.org/play?task=23b5c85d
p=lambda a:[c*[e]for b in a if(c:=b.count(e:=min(d:=sum(a,[0]*99),key=d.count)))]
# 💎 task 50: 84 bytes, gold, https://arcprize.org/play?task=253bf280
p=lambda a,*b,s=0:[c|(s&(s:=s^c)&~sum(b)>7)*3for c in b]or[*map(p,a,*map(p,a*9,*a))]
# 💎 task 51: 111 bytes, gold, https://arcprize.org/play?task=25d487eb
p=lambda i:[*eval("map(lambda*x,l=0,b=1,a=1:[[l:=l|(b!=y>a<1)*(a:=b),b:=y][y>0]for y in x][::-1],*"*4+"i))))")]
# 🥇 task 52: 40 bytes, gold, https://arcprize.org/play?task=25d8a9c8
p=lambda a:[3*[len({*b})%2*5]for b in a]
# 🥇 task 53: 21 bytes, gold, https://arcprize.org/play?task=25ff71a9
p=lambda a:(a+a)[2:5]
# 💎 task 54: 270 (372 unzipped) bytes, gold, https://arcprize.org/play?task=264363fd
def	p(s):
	*e,i,i=sorted({*sum(s,[])},key=sum(s,[]).count);e={u*1j+t:s	for	u,s	in	enumerate(s)for	t,s	in	enumerate(s)if	s	in	e};n={u	for	u	in	e	for	t	in	e	if	abs(u-t)==1}
	for	u	in{*e}-n:
		for	t	in	n:
			k=t-sum(n)/len(n);l=t;s[int(t.imag)][int(t.real)],r,t=i,2,k+u
			while	s[int(t.imag)][int(t.real)]*r^i*r:s[int(t.imag)][int(t.real)],r,t=e[l],abs(k)>=2,k/2+t
	return	s
# 💎 task 55: 77 bytes, gold, https://arcprize.org/play?task=272f95fa
p=lambda i,z=0:i*0!=0and[p(y,3*(z:=z+([y]>i)))for y in i]or i or 2222096>>z&7
# 🥇 task 56: 40 bytes, gold, https://arcprize.org/play?task=27a28665
p=lambda i:[[0**i[0][0]+0**i[0][2]*3^2]]
# 🥉 task 57: 49 vs 48 bytes for gold, https://arcprize.org/play?task=28bf18c6
p=lambda a,*n:[*filter(any,zip(*n or p(a,*a)*2))]
# 💎 task 58: 94 bytes, gold, https://arcprize.org/play?task=28e73c20
p=lambda a:a and[len(b:=a[0])*[3],[*b[:~(c:=3*[b]>a)]]+[3]*-~c,*zip(*p([*zip(*a[2:])])[::-1])]
# 💎 task 59: 153 bytes, gold, https://arcprize.org/play?task=29623171
p=lambda g,w=37,R=range(11),h=0:[[(g[r][c]==5)*5or(w<sum(t:=sum([*zip(*g[r&12:][:3])][c&12:][:3],()))>=(h:=1))*max(t)for c in R]for r in R]*h or p(g,w-1)
# 🥇 task 60: 47 bytes, gold, https://arcprize.org/play?task=29c11459
p=lambda g:[r[:1]*5+[l%~l%6]+5*[l]for*r,l in g]
# 🥇 task 61: 63 bytes, gold, https://arcprize.org/play?task=29ec7d0e
p=lambda i,r=range(18):[[y*x%max(i[~0])+1for y in r]for x in r]
# 💎 task 62: 121 bytes, gold, https://arcprize.org/play?task=2bcee788
p=lambda g:exec("q=[]\nfor r in zip(*g):q+=q[::-1]*({*r}^{2}=={3}<{*q[-1]})or[[v or 3for v in r]]\ng[:]=q[9::-1];"*8)or g
# 🥈 task 63: 75 vs 74 bytes for gold, https://arcprize.org/play?task=2bee17df
p=lambda g:[[v+3-3*(c>[-v]*99<r[1:-1])for _,*c,_,v in zip(*g,r)]for r in g]
# 🥇 task 64: 152 bytes, gold, https://arcprize.org/play?task=2c608aff
p=lambda a,n=-3:n*a or[[d:=[e:=b.pop(),d][g[2]!=d>0<e!=g[1]in b]for _ in[*b]]for*b,in zip(*p(a,n+1))if[d:=0,g:=sorted(set(c:=sum(a,a[5])),key=c.count)]]
# 💎 task 65: 84 bytes, gold, https://arcprize.org/play?task=2dc579da
p=lambda a:[p(b)for*b,in map(zip,a,a[len(a)//2+1:])]or min(b:=sum(a,()),key=b.count)
# 💎 task 66: 245 (341 unzipped) bytes, gold, https://arcprize.org/play?task=2dd70a9a
def	p(t):
	f={r+d*1j:t[d][r]for	d	in	range(len(t))for	r	in	range(len(t))}
	n,e=[d	for	d	in	f	if	f[d]==3]
	i=[(n,e-n,1),(n,n-e,1)]
	for*o,d,n,e	in	i:
		if(d	in	f)*e%8:
			if	f[d]==2:return[[(r+d*1jin	o)*3|t[d][r]for	r	in	range(len(t))]for	d	in	range(len(t))]
			i+=[o+[d-f[d]//8*n,d-f[d]//8*n+r,r,~f[d]//8*e]for	r	in	f[d]//8*[n/1j,n*1j]or[n]]
# 🥇 task 67: 33 bytes, gold, https://arcprize.org/play?task=2dee498d
p=lambda a:[b[:len(a)]for b in a]
# 🥈 task 68: 115 vs 112 bytes for gold, https://arcprize.org/play?task=31aa019c
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]\nfor*a,in map(zip,a[:1]+a,a,a,a[1:]+a)]#'*2)
# 🥇 task 69: 150 bytes, gold, https://arcprize.org/play?task=321b1fc6
def p(g):E=range(10);f={*enumerate(sum(zip(*g*2),()))};return[[sum(V*(f>{(i+j*20-I+J,8)for J,V in f if V%8})for I,V in f if 8^V)for j in E]for i in E]
# 🥉 task 70: 82 vs 78 bytes for gold, https://arcprize.org/play?task=32597951
p=lambda i:[[(c[0]+7in{*x}&{*c,hash(c)%1070})*2+c[0]for c in zip(x,*i)]for x in i]
# 💎 task 71: 104 bytes, gold, https://arcprize.org/play?task=3345333e
p=lambda i:min([[sum({*t}&{*max(i,key=any)})for t in zip(x,(x*2)[~n::-1])]for x in i]for n in range(16))
# 🥇 task 72: 54 bytes, gold, https://arcprize.org/play?task=3428a4f5
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[7:]+n)]or(a!=n)*3
# 🥇 task 73: 46 bytes, gold, https://arcprize.org/play?task=3618c87e
p=lambda a:a[:2]+a[::3]+[[5-b*4for b in a[2]]]
# 🥇 task 74: 77 bytes, gold, https://arcprize.org/play?task=3631a71a
p=lambda i,*c:[*map(min,i,[9,9]+i[::-1],c)]or[i:=[*map(p,i,*i)]for _ in i][2]
# 🥇 task 75: 86 bytes, gold, https://arcprize.org/play?task=363442ee
p=lambda i,r=range(9):[i[a][:4]+[i[a-a%3+1][b-b%3+5]*i[a%3][b%3]for b in r]for a in r]
# 💎 task 76: 270 (384 unzipped) bytes, gold, https://arcprize.org/play?task=36d67576
def	p(t):
	r={min(n:={g*1j+s:f	for	g,f	in	enumerate(t)for	s,f	in	enumerate(f)if	f},key=n.get)};e=n;[abs(s-g)<2!=r.add(g)for	g	in[*e]*6for	s	in[*r]]
	for	g,f	in	enumerate(t):
		for	s	in	e:o=min(n:={(s-g//4*s.real*2)*1j**g:e[s]^2for	s	in[*r]},key=n.get)-s;t=min(e.get(s-o,3)==13%-~n[s]^2for	s	in[*n])*[[n.get(g*1j+s+o,f^2)^2for	s,f	in	enumerate(f)]for	g,f	in	enumerate(t)]or	t
	return	t
# 💎 task 77: 110 bytes, gold, https://arcprize.org/play?task=36fdfd69
p=lambda i,k=7,*w:k and p([*map(p,i,[k>1]*99,[i*2]+i,i[1:]+[i*2],*w)],k-1)or((c:=w.count)(2)+c(4)>=2!=i)*4or i
# 💎 task 78: 59 bytes, gold, https://arcprize.org/play?task=3906de3d
p=lambda i,*n:sorted(n,key=0 .__eq__)or[*zip(*map(p,i,*i))]
# 💎 task 79: 105 bytes, gold, https://arcprize.org/play?task=39a8645d
p=eval(f"lambda a:max(b:=[a {'for*a,in map(zip,a,a[1:],a[2:])'*2}if any(min(*a,*zip(*a)))],key=b.count)")
# 💎 task 80: 231 (301 unzipped) bytes, gold, https://arcprize.org/play?task=39e1d7f9
def p(f):n=f.index(min(f,key=set))+1;e={u*1j+o:f for u,f in enumerate(f[::n])for o,f in enumerate(f[::n])};return[[[f or[e[t:=u//n*1j+o//n],*[e[a+t-r]for r in e if(e[r]==e[a])*2>abs(t-r)]][-1]for o,f in enumerate(f)]for u,f in enumerate(f)]for a in e if all(e.get(a+1j**u)for u,f in enumerate(f))][-1]
# 💎 task 81: 83 bytes, gold, https://arcprize.org/play?task=3aa6fb7a
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or i or(8in w[:2])*(8in w[2:])
# 🥇 task 82: 50 bytes, gold, https://arcprize.org/play?task=3ac3eb23
p=lambda g:[f:=g[0],[*map(max,[0]+f,f[1:]+[0])]]*3
# 🥇 task 83: 40 bytes, gold, https://arcprize.org/play?task=3af2c5a8
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# 🥇 task 84: 62 bytes, gold, https://arcprize.org/play?task=3bd67248
def p(i,x=1):i[-1][x]=4;i[~x][x]=2;i[:~x]and p(i,x+1);return i
# 🥈 task 85: 56 vs 50 bytes for gold, https://arcprize.org/play?task=3bdb4ada
p=lambda i:[i:=[f:=y*(x!=i or f<y)for y in x]for x in i]
# 💎 task 86: 151 bytes, gold, https://arcprize.org/play?task=3befdf3e
p=lambda i,k=7,s=0:-k*i or[[[-((s:=[abs(s)or 1,s&s//4][y>0]-1)>1)|y,*[x for x in sum(i,x)if 0<x!=y!=0],0][k>6]for y in x]for*x,in zip(*p(i,k-1)[::-1])]
# 🥇 task 87: 36 bytes, gold, https://arcprize.org/play?task=3c9b0459
p=lambda a:[b[::-1]for b in a[::-1]]
# 💎 task 88: 100 bytes, gold, https://arcprize.org/play?task=3de23699
p=lambda a,n=44:a*(-3-n)or p([[d%~d&max(max(a))for d in c]for c in zip(*a[any(n*a[-1])-2::-1])],n-1)
# 💎 task 89: 232 (279 unzipped) bytes, gold, https://arcprize.org/play?task=3e980e27
def	p(i):
	for	n	in(e:={n*1j+a:i	for	n,i	in	enumerate(i)for	a,i	in	enumerate(i)if	i}):
		for	r	in	e:
			t={r}
			for	a	in[*e]*3:
				if	e[n]==e[r]!=any(0<abs(n-r)<2for	r	in	e)<any(0<abs(a-r)<2for	r	in	t):t|={a};i[int((a-r+n).imag)][int((-(-1)**e[r]*(a-r)+n).real)]=e[a]
	return	i
# 💎 task 90: 153 bytes, gold, https://arcprize.org/play?task=3eda0437
s='for %s,b in enumerate(%s)'
exec(f"p=lambda a:max([j>i,-(C:=sum(g:=[[b|6*(i<=m<=j)*(k<=n<=l){s}]{s}],a).count)(7),C(6),g]{s*4})[3]"%(*'nbmaiakbjalb',))
# 🥇 task 91: 63 bytes, gold, https://arcprize.org/play?task=3f7978a0
p=lambda a,n=46:a*~n or p([*zip(*a[(5in a[n%2-2])-2::-1])],n-1)
# 🥇 task 92: 86 bytes, gold, https://arcprize.org/play?task=40853293
p=lambda a:[*map(f:=lambda*b,i=0:[v|(i:=i^b.count(v)*v-v)>>v*9for v in b],*map(f,*a))]
# 🥉 task 93: 100 vs 98 bytes for gold, https://arcprize.org/play?task=4093f84a
import re
p=lambda g:[g:=eval(re.sub("[^50],([^(]+5)",r"\1,5",str([*zip(*g[::-1])])))for _ in g][11]
# 💎 task 94: 97 bytes, gold, https://arcprize.org/play?task=41e4d17e
p=lambda i,*h:[h:=[y+6%-y*(1<x.count(1)==h.count(h>[7])%5)for y in x]for x in zip(*h or p(i,*i))]
# 🥈 task 95: 74 vs 73 bytes for gold, https://arcprize.org/play?task=4258a5f9
p=lambda a,n=6:~n*a or[[n%2|(n:=m)for m in a]for a[::-1]in zip(*p(a,n-2))]
# 💎 task 96: 283 (377 unzipped) bytes, gold, https://arcprize.org/play?task=4290ef0e
import re
def p(n):f={0:(a:=max(n:=re.sub(', ','',str(n+[*zip(*n)])),key=n.count),2)}|{(m:=len(re.findall(e+e+'([^]+)'+e+']+)'+e+'|$',n+n[::-1])[0]))-len(max(re.findall(e+'+',n)))*~(m>0)>>1:(e,m-1>>1)for e in{*n}-{a,*'([]+)'}};return[[int([a,*f[max(abs(e),abs(m))]][f[max(abs(e),abs(m))][1]<min(abs(e),abs(m))])for e in range(-max(f),max(f)+1)]for m in range(-max(f),max(f)+1)]
# 💎 task 97: 93 bytes, gold, https://arcprize.org/play?task=42a50994
p=lambda i,*w:i*0!=0and[*map(p,*sum([[x,x[1:]+[i*4],[i*4]+x]for x in[i,*w]],[]))]or(i in w)*i
# 💎 task 98: 64 bytes, gold, https://arcprize.org/play?task=4347f46a
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i,*w)]or i^min(w)
# 🥇 task 99: 112 bytes, gold, https://arcprize.org/play?task=444801d8
p=lambda g,R=[]:g and p(g[:-1],w:=[g[-1][x]or(1in{*R[:x+1]}&{*R[x:]})*max(sum(g[-2:],R))for x in range(10)])+[w]
# 🥈 task 100: 88 vs 85 bytes for gold, https://arcprize.org/play?task=445eab21
p=lambda a:[[max(range(1,10),key=[sum({*b}&{*c})for c in zip(*a)for b in a].count)]*2]*2
# 💎 task 101: 261 (444 unzipped) bytes, gold, https://arcprize.org/play?task=447fd412
def p(f):
 o,n,d,e,a=[{r+m*20for m in range(len(f))for r in range(len(f[m]))if f[m][r]==b}for b in range(5)]
 for b in d:e|={b for b in d for m in n|e if abs(b-m)in[1,20]}
 for b in d:i={b}-a and{b-min(len({b+m*(g-2)for g in range(5)}&d)for m in[1,20])*(min(e)-max(e))}&d;a|=i;f=[[f[m][r]or r+m*20in(i and{b-min(len({b+m*(g-2)for g in range(5)}&d)for m in[1,20])*(min(e)-m)for m in n})for r in range(len(f[m]))]for m in range(len(f))]
 return f
# 💎 task 102: 135 bytes, gold, https://arcprize.org/play?task=44d8ac46
exec("p=lambda i,n=12:[[i[a][b]or 2*any([n,*[2]*(n-2),n]==[sum(i[(a-k+s)%12][b-j:][:n])/5"+"for %s in range(n)%s"*6%(*'s]n j k)b]a]',))
# 🥇 task 103: 29 bytes, gold, https://arcprize.org/play?task=44f52bb0
p=lambda a:[[a==a[::-1]or 7]]
# 🥉 task 104: 86 vs 84 bytes for gold, https://arcprize.org/play?task=4522001f
p=lambda g,h=2,w=0:h and[p(g,h-1,w^A>>w//8)for A in range(9)][::1-g[h][-h]|1]or(w<4)*3
# 🥈 task 105: 146 vs 145 bytes for gold, https://arcprize.org/play?task=4612dd53
p=lambda g:[g:=[[v or A([r*(m:=[*map(A,g)])[j],sorted(r)[-4]*m[j:]][A(m[:j])])*2for j,v in enumerate(r)]for r in zip(*g)][::-1]for A in[any]*4][3]
# 💎 task 106: 55 bytes, gold, https://arcprize.org/play?task=46442a0e
p=lambda i,s=[],k=3:-k*i or p([*zip(*i+s)],i[::-1],k-1)
# 🥉 task 107: 163 vs 161 bytes for gold, https://arcprize.org/play?task=469497ad
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]'+'or g[(y%sx)//z%%%s::%s].count(g[6])>>(x-%sy)%%z&2'*2+'for %s in range(5*z)]'*2)%(*'-66++54~yx',))
# 💎 task 108: 46 bytes, gold, https://arcprize.org/play?task=46f33fce
p=lambda a:a>a*0!=0and[p(a[1])]*4+p(a[2:])or a
# 💎 task 109: 77 bytes, gold, https://arcprize.org/play?task=47c1f68c
p=lambda a,s=0:a*0!=0and(b:=[*map(p,a,[a[l:=len(a)//2]]*l)])+b[::-1]or a%~a&s
# 🥈 task 110: 89 vs 85 bytes for gold, https://arcprize.org/play?task=484b58aa
p=lambda g:[max([[0in{x,y,x^y}and(x|y)for x,y in zip(b,a)]for a in g],key=all)for b in g]
# 🥇 task 111: 60 bytes, gold, https://arcprize.org/play?task=48d8fb45
p=lambda g:[(f:=sum(g,g))[f.index(5)+d:][:3]for d in b'	']
# 🥇 task 112: 106 bytes, gold, https://arcprize.org/play?task=4938f0c2
p=lambda i,k=1:-k*i or p([*map(lambda*x,b=2+[*map(max,i)].index(3)*2:[y|(x*2)[b:=b-1]for y in x],*i)],k-1)
# 🥇 task 113: 25 bytes, gold, https://arcprize.org/play?task=496994bd
p=lambda a:a[:5]+a[4::-1]
# 🥇 task 114: 64 bytes, gold, https://arcprize.org/play?task=49d1d64f
*R,p=0,lambda g:[R+g[0]+R,*[r[:1]+r+r[-1:]for r in g],R+g[-1]+R]
# 🥇 task 115: 52 bytes, gold, https://arcprize.org/play?task=4be741c5
p=lambda a,*n:[*zip(*map({}.fromkeys,n or p(a,*a)))]
# 🥇 task 116: 20 bytes, gold, https://arcprize.org/play?task=4c4377d9
p=lambda a:a[::-1]+a
# 💎 task 117: 130 bytes, gold, https://arcprize.org/play?task=4c5c2cf0
p=lambda i:[i:=[*zip(*map(max,i,(i*2)[j*2::-1]+i[::-1]))]for j in b'	'*2if[x.count(max(i[j]))for x in i[j-1:j+2]]==[2,1,2]][1]
# 💎 task 118: 226 (300 unzipped) bytes, gold, https://arcprize.org/play?task=50846271
def	p(r):
	for	f	in(2,3):
		t,e,i,*n=[{s-o*1jfor	o,r	in	enumerate(r)for	s,r	in	enumerate(r)if	r>=f}for	f	in(2,0,5,6)]
		for	o	in	e:j={s	for	s	in	e	if	abs(s-o)in(2,0,1,f)};n+=[f|j	for	f	in	n	if	t-f>j]
		for	f	in	n:
			if	t-i<f:return[[r+3*(s-o*1jin	f&i)for	s,r	in	enumerate(r)]for	o,r	in	enumerate(r)]
# 🥇 task 119: 106 bytes, gold, https://arcprize.org/play?task=508bd3b6
import re;p=lambda i,k=39:-k*i or[*zip(*eval(re.sub("0(?=.{34}[38].{34}[382])","3",str(p(i,k-1))))[::-1])]
# 💎 task 120: 78 bytes, gold, https://arcprize.org/play?task=50cb2852
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or[8,i]["0"in str(w)]
# 🥉 task 121: 90 vs 89 bytes for gold, https://arcprize.org/play?task=5117e062
p=lambda g:exec("g[:]=*map(list,zip(*g[(8in g[-2])-2::-1])),;"*40+"g[1][1]=max(g[0])")or g
# 🥉 task 122: 79 vs 75 bytes for gold, https://arcprize.org/play?task=5168d44c
p=lambda a:7in map(sum,a)and a[-2-len(a)%2:][:2]+a[:-2]or[*zip(*p([*zip(*a)]))]
# 🥈 task 123: 75 vs 72 bytes for gold, https://arcprize.org/play?task=539a4f51
R=range(10)
p=lambda g:[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]
# 💎 task 124: 95 bytes, gold, https://arcprize.org/play?task=53b68214
p=lambda i:i[9:]and i or p(i+[((w:=i[4]!=i[1])*[0for k in(1,2)if[0]*k+i[0]>i[2]]+i[w-3])[:10]])
# 🥈 task 125: 122 vs 119 bytes for gold, https://arcprize.org/play?task=543a7ed5
import re;p=lambda i,k=15:-k*i or p(eval(re.sub('[83](?='+k*k%3*', 4|, 6'+'.{43}6)','k*k%3+3',str([*zip(*i[::-1])]))),k-1)
# 🥇 task 126: 54 bytes, gold, https://arcprize.org/play?task=54d82841
p=lambda a:a[:-1]+[[4*(0<sum(c)in c)for c in zip(*a)]]
# 💎 task 127: 63 bytes, gold, https://arcprize.org/play?task=54d9e175
p=lambda a,q=3:a*-1and 5+a%5or a[1:]and[p(a[1])]*q+p(a[2:],4-q)
# 🥇 task 128: 59 bytes, gold, https://arcprize.org/play?task=5521c0d9
p=lambda i,*n:n[-n.count(0):]+n or[*zip(*map(p,i,*i))][:15]
# 🥇 task 129: 47 bytes, gold, https://arcprize.org/play?task=5582e5ca
p=lambda a:[[max(b:=sum(a,a),key=b.count)]*3]*3
# 🥇 task 130: 65 bytes, gold, https://arcprize.org/play?task=5614dbcf
p=lambda a:[[sum({*b[c:c+3]}-{5})for c in(0,3,6)]for b in a[::3]]
# 💎 task 131: 125 bytes, gold, https://arcprize.org/play?task=56dc2b01
p=lambda a:[a:=[[*b[:[*b,1].index(~b[l:=len(a)]%5%3)],*b[l:],8,*[0]*l][l-1::-1]for*b,in zip(*a,*filter(any,a))]for _ in a][3]
# 🥇 task 132: 86 bytes, gold, https://arcprize.org/play?task=56ff96f3
p=lambda i,v=0:[i:=[[v|(v:=v^sum({*A}&{*y}))for A in i]for y in zip(*i)]for _ in i][1]
# 💎 task 133: 276 (439 unzipped) bytes, gold, https://arcprize.org/play?task=57aa92db
def	p(e):
	*f,n={o*66+l:(e)for	o,e	in	enumerate(e)for	l,e	in	enumerate(e)if	e},
	for	o	in	n:
		u={o}
		for	t	in*f,:
			if{o-66,o-1}&t:f.remove(t);u|=t
		f+=u,
	for	t	in*f,:
		for	o	in	t:
			for	u	in	t:
				i=t
				for	i	in	1//len([r	for	r	in	i	if	n[o]==n[r]])*f:
					for	a	in	t-{u}:
						for	r	in([r	for	r	in	i	if	n[o]==n[r]==n[u]]):r+=(len([r	for	r	in	i	if	n[o]==n[r]==n[u]])^6)%6*(a-u);e[r//66][r%66],={n[r]for	r	in	i}-{n[o]}
	return	e
# 💎 task 134: 123 bytes, gold, https://arcprize.org/play?task=5ad4f10b
p=lambda g,D=10:[[D*(D!=v>0)for v in r]for r in('0, %g, 0'%D in'%s'%g)*g]or(h:=[*filter(any,zip(*p(g,D-.5)))])[::len(h)//3]
# 🥇 task 135: 32 bytes, gold, https://arcprize.org/play?task=5bd6f4ac
p=lambda a:[b[6:]for b in a[:3]]
# 💎 task 136: 104 bytes, gold, https://arcprize.org/play?task=5c0a986e
import re;p=lambda m,i=30:i and p(re.sub(r:="(?<=(%d.{34}){2})0"%(i%4),r[5],str(m))[::-1],i-1)or eval(m)
# 🥈 task 137: 141 vs 137 bytes for gold, https://arcprize.org/play?task=5c2c9af4
def p(a):r=range(len(a));*_,B,C=sorted(map(a.index,a));W=max(a[B]);return[[W>>max(i-B,B-i,abs(a[B].index(W)-j))%(C-B)*9for j in r]for i in r]
# 🥇 task 138: 104 bytes, gold, https://arcprize.org/play?task=5daaa586
p=lambda a,n=35:-n*a or p([*map(lambda*b,d=0:[d:=c|d*(d==b[0]>n-3)for c in b[::-1]],*a[0in a[0]:])],n-1)
# 💎 task 139: 88 bytes, gold, https://arcprize.org/play?task=60b61512
p=lambda i,k=4,*w:k and p([*map(p,i,[k>1]*9,i[:1]+i,i[1:]+i,*w)],k-1)or i or(sum(w)>7)*7
# 🥇 task 140: 36 bytes, gold, https://arcprize.org/play?task=6150a2bd
p=lambda a:[b[::-1]for b in a[::-1]]
# 💎 task 141: 93 bytes, gold, https://arcprize.org/play?task=623ea044
p=eval("lambda a:[[max((x-i in(y-j,j-y))*b[y]"+"for %s,b in enumerate(a)%s"*4%(*'y x)j]i]',))
# 🥇 task 142: 40 bytes, gold, https://arcprize.org/play?task=62c24649
p=lambda a:[b+b[::-1]for b in a+a[::-1]]
# 💎 task 143: 130 bytes, gold, https://arcprize.org/play?task=63613498
p=lambda i,n=1,*w:any(w==(w:=[*map(len,s:=str(i).split(str(n)))][1:-1])for n in{max(i[:3])[0]:0,n:0})*eval('5'.join(s))or p(i,n+1)
# 🥇 task 144: 53 bytes, gold, https://arcprize.org/play?task=6430c8c4
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[5:]+n)]or 3>>a+n
# 💎 task 145: 170 bytes, gold, https://arcprize.org/play?task=6455b5f5
p=lambda x,k=7,v=2:-k*x or p([[a:=2*(b==2)or(k>1)*(a|(b or(v:=v*2)))or[b//max(f:=sum(x,[]))+min({*f}-{2})//b*8,f.count(b)+2][k]for b in[2]+r][:0:-1]for*r,in zip(*x)],k-1)
# 🥇 task 146: 58 bytes, gold, https://arcprize.org/play?task=662c240a
p=lambda g:(x:=g[:3])*([*map(list,zip(*x))]!=x)or p(g[3:])
# 💎 task 147: 72 bytes, gold, https://arcprize.org/play?task=67385a82
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or(3in w)+7&i*9
# 💎 task 148: 124 bytes, gold, https://arcprize.org/play?task=673ef223
p=lambda g,*w:[[-v%12&6|(c:=c^(8in r*v))*8>>v for v in r]for r in g if[c:=any(r)and(w:=[r,*w])[0][0]!=g[4][0]!=8in w.pop()]]
# 🥇 task 149: 75 bytes, gold, https://arcprize.org/play?task=6773b310
p=lambda a:a[3:]and[p([*zip(*a[t:t+3])])for t in[0,4,8]]or 9<sum(sum(a,()))
# 🥇 task 150: 30 bytes, gold, https://arcprize.org/play?task=67a3c6ac
p=lambda g:[r[::-1]for r in g]
# 💎 task 151: 103 bytes, gold, https://arcprize.org/play?task=67a423a3
def p(g):
 y,x,*_=[z.index(max(z))for z in[g]+g]
 for N in b"":g[y+N//3-6][x+N%3-1]=4
 return g
# 🥇 task 152: 40 bytes, gold, https://arcprize.org/play?task=67e8384a
p=lambda a:[r+r[::-1]for r in a+a[::-1]]
# 💎 task 153: 131 bytes, gold, https://arcprize.org/play?task=681b3aeb
r=3,2,1;p=lambda g:max(({*str(w:=[[max(g[A%10-y][A%11-x]for A in(a,a%119))for x in r]for y in r])}^{'0'},w)for a in range(6666))[1]
# 🥉 task 154: 100 vs 98 bytes for gold, https://arcprize.org/play?task=6855a6e4
import re
p=lambda g,*G:eval(re.sub("([^2(]{9}2[^2]{9})",r"*[\1][::-1]","%s"%[*zip(*G or p(g,*g))]))
# 🥇 task 155: 18 bytes, gold, https://arcprize.org/play?task=68b16354
p=lambda a:a[::-1]
# 💎 task 156: 128 bytes, gold, https://arcprize.org/play?task=694f12f3
p=lambda i,a=9,S=sum:[[v-(S(g:=S(i,[]))//S(g[:i.index(min(i),1)*10]*2)+2^a//60)*(S(g[a-18:(a:=a+1):9])>11)for v in r]for r in i]
# 💎 task 157: 242 (256 unzipped) bytes, gold, https://arcprize.org/play?task=6a1e5592
def	p(g):
	r=[*map(max,*g[6:]),0,5,0].index;w=r(0,t:=r(5))
	for	l	in	range(t%15+16-w):
		for	s	in	1,0:
			u=*map(list,g),
			for	x	in	g[6:]:
				s+=any(x[t:w])
				for	b	in	range(t,w):g[s][b-t+l]+=x[b]>4;x[b]=0
			g=p(g)or	u
	if{*g[1]+g[2]}=={1,2}:return	g
# 💎 task 158: 260 (488 unzipped) bytes, gold, https://arcprize.org/play?task=6aa20dc0
def	p(r):
	f,l=max((len({*str(e:=[f[o:o+3]for	f	in	r[f:f+3]])}),e)for	f	in	range(len(r))for	o	in	range(len(r[-1])))
	for	e	in	range(len(r[-1])):
		for	f	in	range(len(r)-e*3):
			for	o	in	range(len(r[-1])-e*3):
				for	a	in	range(len(r[-1])):
					for	a	in	range(e*3*all(r[f+a][o+n]==l[a//e][n//e]or	r[f+a][o+n]==r[-1][-1]!=l[a//e][n//e]==max({*l[1]}-{r[-1][-1]})for	a	in	range(e*3)for	n	in	range(e*3))):
						for	n	in	range(e*3):r[f+a][o+n]=l[a//e][n//e]
					l=*zip(*l[::-1]),
	return	r
# 💎 task 159: 105 bytes, gold, https://arcprize.org/play?task=6b9890af
p=lambda g,*G:sum([[[2,*r,2]]*[str(g).count('2')//12,all(r)][{*r}<={0,2}]for*r,in zip(*G or p(g,*g))],[])
# 💎 task 160: 100 bytes, gold, https://arcprize.org/play?task=6c434453
import re;p=lambda i,*n:eval(re.sub("1.{5}1(.{25})??"*3,r"0,2,0\1 2,2,2\2 0,2,0",str(n or p(i,*i))))
# 💎 task 161: 79 bytes, gold, https://arcprize.org/play?task=6cdd2623
p=lambda m:[[4//(C:=sum(m,m).count)(x)*x|4//C(i)*i for i in m[0]]for x,*_ in m]
# 🥈 task 162: 97 vs 96 bytes for gold, https://arcprize.org/play?task=6cf79266
import re;p=lambda i,*I:eval(re.sub("0, 0, 0(.{55})?"*3," 1,1,1\%d"*3%(1,2,3),str(I or p(i,*i))))
# 🥈 task 163: 136 vs 131 bytes for gold, https://arcprize.org/play?task=6d0160f0
R=0,4,8
e=range(11)
p=lambda a:[[5*(a[i][j]==5)or sum((4==a[k+i//4][l+j//4])*a[k+i%4][l+j%4]for k in R for l in R)for j in e]for i in e]
# 🥇 task 164: 32 bytes, gold, https://arcprize.org/play?task=6d0aefbc
p=lambda a:[b+b[::-1]for b in a]
# 💎 task 165: 130 bytes, gold, https://arcprize.org/play?task=6d58a25d
def p(i):_,b,s={}.fromkeys(sum(i[::-1],[0]));return[[t[a]or(b in t[[*t[:a]+i,s].index(s):])*b for*t,in zip(*i)]for a in range(20)]
# 🥉 task 166: 63 vs 61 bytes for gold, https://arcprize.org/play?task=6d75e8bb
p=lambda a:[[~v*c*any(b)%10for v,c in zip(b,max(a))]for b in a]
# 💎 task 167: 70 bytes, gold, https://arcprize.org/play?task=6e02f1e3
p=lambda i:[[5*(y==x%len({*str(i)})%3)for x in b'']for y in(0,1,2)]
# 🥉 task 168: 115 vs 110 bytes for gold, https://arcprize.org/play?task=6e19193c
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(r"0(?=(.{35})+,( [^0]).{27}\2,\2)",r"\2",str(p(i,k-1))))[::-1])]
# 💎 task 169: 113 bytes, gold, https://arcprize.org/play?task=6e82a1ae
p=lambda i,k=11,t=1:-k*i or[(e:=1)*[e:=y%2*[y|(t:=t*16),-y%5,e|y][k//-10]for y in i]for i[::-1]in zip(*p(i,k-1))]
# 🥈 task 170: 194 (236 unzipped) vs 180 bytes for gold, https://arcprize.org/play?task=6ecd11f4
def p(r):[(o:=i,f:=e)for i,r in enumerate(r)for e,r in enumerate(r)if r];n=0**r[o-3][f]-4;e=*filter(max,zip(*filter(max,zip(*r[:o-3])))),;return[[e and(r)for e,r in zip(e[::~len(e)//n],r[n-~f:])]for e,r in zip(e[::~len(e)//n],r[n-~o:])]
# 🥇 task 171: 51 bytes, gold, https://arcprize.org/play?task=6f8cd79b
p=lambda a:a*all(a[0])or p([*zip(*a[:0:-1],[8]*9)])
# 🥇 task 172: 20 bytes, gold, https://arcprize.org/play?task=6fa7a44f
p=lambda a:a+a[::-1]
# 💎 task 173: 204 (299 unzipped) bytes, gold, https://arcprize.org/play?task=72322fa7
p=lambda n:[1for l,s in enumerate(n)for d,s in enumerate(s)for y,s in enumerate(n)for t,s in enumerate(s)if((r:=[n[y-f//3][t-f%3]for f,s in enumerate(n[:9])])==r[::-1])*sum(r[4]*r[:4])*(r[4]==n[l-1][d-1]or sum(s==n[l-f//3][d-f%3]for f,s in enumerate(r))>7)for f,n[l-f//3][d-f%3]in enumerate(r)]and n
# 🥈 task 174: 97 vs 89 bytes for gold, https://arcprize.org/play?task=72ca375d
p=lambda g,c=1:((f:=lambda g:[r for r in zip(*g)if c in r])(k:=f(g))==f(k[::-1]))*f(k)or p(g,c+1)
# 🥇 task 175: 75 bytes, gold, https://arcprize.org/play?task=73251a56
r=range(21);p=lambda g:[[g[A][B]|g[B][A]or g[0][B!=A]for B in r]for A in r]
# 💎 task 176: 61 bytes, gold, https://arcprize.org/play?task=7447852a
p=lambda g,r=5:[[x|~r*(r:=r-x)%6for x in s]*(r:=1)for s in g]
# 🥇 task 177: 51 bytes, gold, https://arcprize.org/play?task=7468f01a
p=lambda a,*n:[*filter(any,zip(*n or p(*a)[::-1]))]
# 🥇 task 178: 47 bytes, gold, https://arcprize.org/play?task=746b3537
p=lambda a:a*-1*-1or[p(a:=b)for b in a if a!=b]
# 🥇 task 179: 21 bytes, gold, https://arcprize.org/play?task=74dd1130
p=lambda a:[*zip(*a)]
# 💎 task 180: 74 bytes, gold, https://arcprize.org/play?task=75b8110e
p=lambda a:[p(b)for*b,in map(zip,a,a[4:])]or max(sum(a+a,())[1:],key=bool)
# 🥇 task 181: 67 bytes, gold, https://arcprize.org/play?task=760b3cac
def p(a):
	for b in a[:3]:c=6>>a[3][3];b[c:c+3]=b[5:2:-1]
	return a
# 🥉 task 182: 186 vs 169 bytes for gold, https://arcprize.org/play?task=776ffc46
def p(g):
 R=F=sum(g,[])
 while C:=max(F):
  o=F.index(C)-2;N={d for d in range(65)if d%20<6!=F[d+o:]>=[C]}
  for i in N:i+=o;F[i]=0;g[i//20][i%20]+=N==R and~-W
  if~-C:R,W=N,C
 return g
# 🥈 task 183: 94 vs 93 bytes for gold, https://arcprize.org/play?task=77fdfe62
def p(g):A=len(g);B=range(2,A-2);return[[g[g[C][B]%5-3-C*2//A][0-B*2//A]for B in B]for C in B]
# ❌ task 184: 101 vs 91 bytes for gold, https://arcprize.org/play?task=780d0b14
p=lambda i,k=0,s=[0]*99:[s+0*(s:=[*x])for x in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
# 🥈 task 185: 133 vs 120 bytes for gold, https://arcprize.org/play?task=7837ac64
p=eval(f"lambda i:{'[[sum({r.pop()}&r,r[1:])]*'*2}((r[0]r,*i)ifi if)])]".translate([0,"{*r}-{*i[0]})","zip(","for*r,in "]))
# ❌ task 186: 61 vs 60 bytes for gold, https://arcprize.org/play?task=794b24be
p=lambda m:[(c:=sum(sum(m,z:=[0]*3))*[2]+z)[:3],[0,c[3],0],z]
# 💎 task 187: 88 bytes, gold, https://arcprize.org/play?task=7b6016b9
p=lambda i,k=7:-k*i or[*map(lambda*x,z=3:[z:=y|(y*z==6)or 2for y in x],*p(i,k-1)[::-1])]
# 🥈 task 188: 63 vs 61 bytes for gold, https://arcprize.org/play?task=7b7f7511
p=lambda a,s=4:a[:s]*(a[:s]*2==a)or[*zip(*p([*zip(*a)],~-s%5))]
# 🥇 task 189: 111 bytes, gold, https://arcprize.org/play?task=7c008303
p=lambda i,r=range(6):[[i[a-6+(s:=i[6][0]%3)*3][b-6+(t:=i[0][6]%3)*3]/3*i[a//3-s][b//3-t]for b in r]for a in r]
# 🥈 task 190: 106 vs 105 bytes for gold, https://arcprize.org/play?task=7ddcd7ec
import re;p=lambda i,k=19:-k*i or[*zip(*eval(re.sub('.{31}0, ([^0])'*2,r"|\1\g<0>",str(p(i,k-1))))[::-1])]
# 💎 task 191: 228 (384 unzipped) bytes, gold, https://arcprize.org/play?task=7df24a62
def	p(n):
	e=[[*l]for	l	in	zip(*n)if	1in	l]
	e=[[*l]for	l	in	zip(*e)if	1in	l]
	for	l	in	0,1,0,1,0,1,0,1:n=l*n[::-1]or[[*l]for	l	in	zip(*n)];[1for	r,l	in	enumerate(n)for	z,l	in	enumerate(n)for	i,l	in	enumerate(all(n[r+i-1][z+f-1]==l&-2if	0<z+f<24>r+i>0else	l<4for	i,l	in	enumerate(e)for	f,l	in	enumerate(l))*e)for	f,l	in	enumerate(l)if	0<z+f<24>r+i>0for	n[r+i-1][z+f-1]in[l]]
	return	n
# 🥈 task 192: 114 vs 110 bytes for gold, https://arcprize.org/play?task=7e0986d6
b=c='for*d,c,b,a in zip(b,c,z+a,a[1:]+z,a)]'
*z,p=b,lambda a:eval('[[[sum({*d}&{b,c}),a][f"{a}, "*2in"%s"]'%a+b*2)
# 💎 task 193: 71 bytes, gold, https://arcprize.org/play?task=7f4411dc
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or(w.count(i)>1)*i
# 💎 task 194: 55 bytes, gold, https://arcprize.org/play?task=7fe24cdd
p=lambda i,s=[],k=3:-k*i or p([*zip(*i+s)],i[::-1],k-1)
# 💎 task 195: 96 bytes, gold, https://arcprize.org/play?task=80af3007
p=lambda a,n=1:[[y&a[(n:=n+3)//9%9][n%9]for y in x]for x in-n*a]or p([*filter(any,zip(*a))],n-1)
# 💎 task 196: 107 bytes, gold, https://arcprize.org/play?task=810b9b61
p=lambda i,k=19:-k*i or[*map(lambda*r,a=8:[a:=[b or 8&a,b|2*(a%3<b),b%5][k//8]for b in r],*p(i,k-1)[::-1])]
# 🥇 task 197: 54 bytes, gold, https://arcprize.org/play?task=82819916
p=lambda a:[[b[a[1].index(c)]for c in a[1]]for b in a]
# 💎 task 198: 118 bytes, gold, https://arcprize.org/play?task=83302e8f
p=lambda a,*b,n=-23:n*a or[[c,4-(sum(25>>e&n for e in b)>9)][9>>c&(n:=c!=4)]for c in b][::-1]or[*map(p,a,*p(a,n=n+1))]
# 🥇 task 199: 84 bytes, gold, https://arcprize.org/play?task=834ec97d
p=lambda g:-~(i:=g.index(m:=max(g)))*[([4,0]*15)[m.index(max(m)):][:len(g)]]+g[i:-1]
# 🥇 task 200: 84 bytes, gold, https://arcprize.org/play?task=8403a5d5
p=lambda g,r=5:[([0]*g[9].index(c:=max(g[9]))+[c,r,c,r:=any(x)*5]*3)[:10]for x in g]
# 🥈 task 201: 203 vs 199 bytes for gold, https://arcprize.org/play?task=846bdb03
def p(g):j=D=0;P=[];exec("for r in g:F=r[j]==4;P+=r[j:]*D;D^=F;r[j]*=D|F<1\nj+=1\n"*13+"g[:]=filter(any,zip(*g));"*3);A,*_,B=map(max,g);E=4,*[0]*len(g),4;return E,*zip(*([A]*9,*g,[B]*9)[::A==P[0]or-1]),E
# 🥉 task 202: 104 vs 102 bytes for gold, https://arcprize.org/play?task=855e0971
p=lambda a:[[*map(min,*[c for c in a if{*c}<=r])]for b in a if len(r:={*b,0})<3]or[*zip(*p([*zip(*a)]))]
# 🥉 task 203: 67 vs 64 bytes for gold, https://arcprize.org/play?task=85c4e7cd
p=lambda i:[[i[g:=len(i)//2][g+i[g].index(y)]for y in x]for x in i]
# 🥇 task 204: 93 bytes, gold, https://arcprize.org/play?task=868de0fa
import re;p=lambda i:eval(re.sub("(?<!1, )1,(.+?)1",r"1,*[(s:=len([\1]))%2*5+2]*s,1",str(i)))
# 💎 task 205: 139 bytes, gold, https://arcprize.org/play?task=8731374e
p=lambda a,n=87,i=0:[[min(b+c,key=b.count)for c in zip(*a)]for b in-n*a]or p([*zip(*a[(6in(i:=1+i*(a==(a:=b))for b in a[-1]))-2::-1])],n-1)
# 💎 task 206: 140 bytes, gold, https://arcprize.org/play?task=88a10436
def p(g):
 W=len(g[0]);s=sum(G:=g,[]).index(5)+~W
 for g[s//W][s%W:s%W+3]in[G:=[r for*r,in zip(*G)if{*r}-{0,5}]for _ in g][1]:s+=W
 return g
# 💎 task 207: 74 bytes, gold, https://arcprize.org/play?task=88a62173
p=lambda a:[p(b)for*b,in map(zip,a,a[3:])]or min(b:=sum(a,()),key=b.count)
# 🥈 task 208: 211 (270 unzipped) vs 199 bytes for gold, https://arcprize.org/play?task=890034e9
def	p(z):
	t=min(sum(r:=z,[]),key=sum(r:=z,[]).count);o=len(r:=[r	for	r	in	zip(*r)if	t	in	r])
	f=len(r:=[r	for	r	in	zip(*r)if	t	in	r])
	for	n	in	range(22-o):
		for	m	in	range(22-f):
			for	z[m][n:n+o]in	r*0**sum(sum(r[n:n+o][1:-1])for	r	in	z[m:m+f][1:-1]):m+=1
	return	z
# 💎 task 209: 247 (387 unzipped) bytes, gold, https://arcprize.org/play?task=8a004b2b
def	p(g):
	G=g
	for	s	in	G*4:G=[[*s]for	s	in	zip(*G[~4:])if{*s}-{0,4}];g=[[*s]for	s	in	zip(*g[(4in	g[-1])-2::-1])]
	for	s,r	in	enumerate(g):
		if[0for	y,r	in	enumerate(g)for	x,r	in	enumerate(s*r)for	Y,r	in	enumerate(s*all(g	in[0,((G+20*[[]])[(Y-y)//s]+20*[4])[(X-x)//s]]for	Y,g	in	enumerate(g)for	X,g	in	enumerate(g))*G)for	X,r	in	enumerate(s*r)for	g[Y+y][X+x]in[G[Y//s][X//s]]]:return	g
# 🥇 task 210: 20 bytes, gold, https://arcprize.org/play?task=8be77c9e
p=lambda a:a+a[::-1]
# 🥇 task 211: 48 bytes, gold, https://arcprize.org/play?task=8d5021e8
p=lambda g:[l[::-1]+l for l in(g[::-1]+g)*2][:9]
# 💎 task 212: 93 bytes, gold, https://arcprize.org/play?task=8d510a79
p=lambda i,k=18:~k*i or[[x.pop()or[0,*x][k%-2]%5&6-(5in x)for _ in i]for*x,in zip(*p(i,k-1))]
# ❌ task 213: 94 vs 88 bytes for gold, https://arcprize.org/play?task=8e1813be
p=lambda i:[*zip(*[u:=[*filter(int,w:=[sum({*r}-{5})for r in i])]]*len(u)*(u>w)or p(zip(*i)))]
# 🥇 task 214: 62 bytes, gold, https://arcprize.org/play?task=8e5a5113
p=lambda a:[b[:4]+(a.pop()[:4]+c)[::-1]for*c,b in[*zip(*a,a)]]
# 🥉 task 215: 45 vs 42 bytes for gold, https://arcprize.org/play?task=8eb1be9a
p=lambda g:([max(g[::3]),*g[4:6]]*9)[:len(g)]
# 💎 task 216: 113 bytes, gold, https://arcprize.org/play?task=8efcae92
p=lambda a:max([-(c:=sum(b:=[b[x%17:x%21]for b in a[x%19:x%22]],a).count)(0),c(2),c(1),b]for x in range(8**6))[3]
# 🥇 task 217: 95 bytes, gold, https://arcprize.org/play?task=8f2ea7aa
p=lambda a,*n:[*filter(any,zip(*[[d&e for d in b for e in c]for b in n for c in a]or p(a,*a)))]
# 🥇 task 218: 56 bytes, gold, https://arcprize.org/play?task=90c28cc7
p=lambda a,*n:[*{b:0for b in zip(*n or p(*a))if any(b)}]
# 💎 task 219: 243 (261 unzipped) bytes, gold, https://arcprize.org/play?task=90f3ed37
def p(i):
 t=r=f=0
 while i[f:]:
  if i[f]>i[0]:t=t or f;r=r or i[f:].index(i[0]);i[f-1:f+r]=[n for o in(0,-1,1,2)for d in(t-1,t)if 7not in sum(n:=[[i%7-2%~e for e,i in zip(e,i[:o%4%3]+i[o<0:]+[0])]for e,i in zip(i[f-1:f+r],i[d:])],[])][0];f+=r
  f+=1
 return i
# 🥉 task 220: 90 vs 87 bytes for gold, https://arcprize.org/play?task=913fb3ed
p=lambda i:[i:=[[x.pop()or-(s*2^s-7)%7for s in[0]+x[:0:-1]]for*x,in zip(*i)]for _ in i][3]
# 💎 task 221: 86 bytes, gold, https://arcprize.org/play?task=91413438
def p(i):j=sum(i,i).count(a:=0);return[(q*(9+(a:=a-1)//3*j)+[0]*21)[:j*3]for q in i*j]
# 💎 task 222: 102 bytes, gold, https://arcprize.org/play?task=91714a58
p=lambda g:[g:=[[c*(sum(g,g).count(c)>8!=2*f"{c}, "in"%s"%r)for c in r]for*r,in zip(*g)]for _ in g][5]
# 💎 task 223: 46 bytes, gold, https://arcprize.org/play?task=9172f3a0
p=lambda a:a>a*0!=0and[p(a[0])]*3+p(a[1:])or a
# 💎 task 224: 165 bytes, gold, https://arcprize.org/play?task=928ad970
p=lambda i,k=3,s=0,S=sum:-k*i or p([[y|(s==5in{*(h:=[*map(S,i)])[b+1:]}&{*h[:b]})*S({*S(i,[-5])})for b,y in enumerate(x)]+0*[s:=s*2+S(x)]for x in zip(*i)][::-1],k-1)
# 🥈 task 225: 128 vs 127 bytes for gold, https://arcprize.org/play?task=93b581b8
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if(c:=b)*i+i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))
# 💎 task 226: 119 bytes, gold, https://arcprize.org/play?task=941d9a10
p=lambda i,y=0:[[v|-~int(a:=y*2/sum(c))*(a==(s:=s+v)*2/sum(r)>=v==a%1)for*c,v in zip(*i,r)]for r in i if[y:=y+r[s:=0]]]
# 🥇 task 227: 52 bytes, gold, https://arcprize.org/play?task=94f9d214
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[4:]+n)]or~a+n&2
# 🥈 task 228: 119 vs 116 bytes for gold, https://arcprize.org/play?task=952a094c
import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'([^0])((, (?!\1|0).).*0\3.{28})0',r'0\2\1',str(p(a,n+1)[::-1]))))]
# 🥇 task 229: 73 bytes, gold, https://arcprize.org/play?task=9565186b
p=lambda a:[[[5,c][c==max(d:=sum(a,a),key=d.count)]for c in b]for b in a]
# 🥈 task 230: 113 vs 111 bytes for gold, https://arcprize.org/play?task=95990924
import re
p=lambda m,i=3:-i*m or[*zip(*eval(re.sub("0(?=, 0.%s.5, 5)"%{len(m)*3},"3**i%5",str(p(m,i-1))))[::-1])]
# 🥇 task 231: 43 bytes, gold, https://arcprize.org/play?task=963e52fc
p=lambda a:[(r[:6]*4)[:len(r)*2]for r in a]
# 💎 task 232: 57 bytes, gold, https://arcprize.org/play?task=97999447
p=lambda i,e=0:i*0!=0and[p(y)or[e:=y-e,5][e<0]for y in i]
# 💎 task 233: 281 (462 unzipped) bytes, gold, https://arcprize.org/play?task=97a05b5b
def p(e):
 for r in 92*[e]:e=[[*r]for r in zip(*e[all(r==r[:12]for r in str(e[0]).split('0')):][::-1])]
 for r in 92*[[r[i:3+i]for r in r[f:3+f]]for f,p in enumerate(r[2:])for i,p in enumerate(p[2:])][::-1]:
  for f,p in enumerate(e*({*sum(r,[])}^{0}>{2,0})):
   for i,p in enumerate(p):
    for o,p in enumerate(r*all((2*(2*e)[o+f])[n+i]==2*(2!=p)for o,p in enumerate(r)for n,p in enumerate(p))):e[o+f][i:3+i],*r=p,
  r[:]=[[*r]for r in zip(*r[::-1])]
 return e
# 💎 task 234: 107 bytes, gold, https://arcprize.org/play?task=98cf29f8
p=lambda i:[i:=[*zip(*[x for x in i[:1]*11+i if{sum(x),0}^{*x+max(i,key=any)}][:~len(i):-1])]for _ in i][3]
# 🥇 task 235: 61 bytes, gold, https://arcprize.org/play?task=995c5fa3
p=lambda g:[[g[1][x]*sum(g[2][x:x+3])%13^8]*3for x in b'']
# 🥇 task 236: 54 bytes, gold, https://arcprize.org/play?task=99b1bc43
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[5:]+n)]or-n%5^3*a
# 💎 task 237: 67 bytes, gold, https://arcprize.org/play?task=99fa7670
p=lambda a,c=0:[(b:=0)or[c:=(b:=b or d)for d in r+[c]]for*r,_ in a]
# 💎 task 238: 201 (313 unzipped) bytes, gold, https://arcprize.org/play?task=9aec4887
def p(i):r=[e for e in zip(*[e for e in zip(*i)if{*e}-{0}-{8}])if{*e}-{0}-{8}];return[[[*[f:=[e for e in zip(*[e for e in zip(*i)if{*e}-{0}&{8}])if{*e}-{0}&{8}],*f,f][n],*r[n]][e-1]and(r[1-(len(r)-e-1>n<e)|-(len(r)-e-1<n>e)][1-(len(r)-e-1>n>e)|-(len(r)-e-1<n<e)]or 8)for e in range(len(r))]for n in range(len(r))]
# 💎 task 239: 99 bytes, gold, https://arcprize.org/play?task=9af7a82c
p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted([c:=-b.count(e),e]*-c+[0]*22for e in{*b})))][2::2]
# 🥈 task 240: 104 vs 99 bytes for gold, https://arcprize.org/play?task=9d9215db
p=lambda i:[i:=[[(z:=i[b])[~a]|z[a]|z[a%2*(b<a<18-b)*b+2]for b in r]for a in r]for r in[range(19)]*5][4]
# 🥇 task 241: 21 bytes, gold, https://arcprize.org/play?task=9dfd6313
p=lambda a:[*zip(*a)]
# 🥇 task 242: 54 bytes, gold, https://arcprize.org/play?task=9ecd008a
p=lambda g:[r[~r.index(0)::-1][:3]for r in g if 0in r]
# 🥇 task 243: 79 bytes, gold, https://arcprize.org/play?task=9edfc990
p=lambda a,n=-79:a*n or[*zip(*eval(str(p(a,n+1)[::-1]).replace('1, 0','1,1')))]
# 🥇 task 244: 63 bytes, gold, https://arcprize.org/play?task=9f236235
p=lambda a:[b[::(n:=~a.index(min(a,key=set)))]for b in a][::-n]
# 🥈 task 245: 101 vs 100 bytes for gold, https://arcprize.org/play?task=a1570a43
p=lambda i,k=7:-k*i or p([*map(lambda*r,w=0:[[v,w%3][(w:=v)<=2in max(i,key=any)]for v in r],*i)],k-1)
# 🥇 task 246: 105 bytes, gold, https://arcprize.org/play?task=a2fd1cf0
p=lambda a,n=3,d=0:-n*a or p([[b.pop()|4*(n|2in b)*(d:=d^sum(c)&2)for c in a[::-1]]for*b,in zip(*a)],n-1)
# 💎 task 247: 92 bytes, gold, https://arcprize.org/play?task=a3325580
p=lambda a,m=9:[*zip(*{(d,)*m:0for d in sum(zip(*a),())if sum(a,a).count(d)==m})]or p(a,m-1)
# 🥉 task 248: 74 vs 72 bytes for gold, https://arcprize.org/play?task=a3df8b1e
def p(m,c=0,d=1):
 for r in m[::-1]:r[c]=1;c+=d;r[1:-c]or(d:=-d)
 return m
# 🥇 task 249: 26 bytes, gold, https://arcprize.org/play?task=a416b8f3
p=lambda a:[r*2for r in a]
# ❌ task 250: 121 vs 114 bytes for gold, https://arcprize.org/play?task=a48eeaf7
import re
p=lambda i:[i:=eval(re.sub("5((.{35})+(?=.{66}2)|[0, ]+(?=, 2))",r"0\1+5",str([*zip(*i[::-1])])))for _ in i][7]
# 🥉 task 251: 89 vs 88 bytes for gold, https://arcprize.org/play?task=a5313dff
p=lambda a,n=43:-n*a or[[14>>d&b.pop()or n<1for d in[0]+b[:0:-1]]for*b,in zip(*p(a,n-1))]
# 💎 task 252: 53 bytes, gold, https://arcprize.org/play?task=a5f85a15
p=lambda g,v=0:g*0!=0and[*map(p,g,[-1,4]*9)]or-g//v&v
# 💎 task 253: 114 bytes, gold, https://arcprize.org/play?task=a61ba2ce
p=lambda g:[[(i:=a&b)*0+max(v*(sum(g,g)[i-1:(i:=i+1)]==[v,v])for v in sum(g,[]))for a in b'[Z']for b in b'A[']
# 🥉 task 254: 93 vs 84 bytes for gold, https://arcprize.org/play?task=a61f2674
def p(i):k=*zip(*i),;return[[x.pop(0)>>(s<max(k))+2*(s>sorted({*k})[1])for s in k]for x in i]
# 💎 task 255: 227 (290 unzipped) bytes, gold, https://arcprize.org/play?task=a64e4611
def p(g):
 for y in range(32):g=[[g[y][~x]+13*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%13|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g
# 🥈 task 256: 96 vs 95 bytes for gold, https://arcprize.org/play?task=a65b410d
def p(g):s=sum(m:=max(g))//2;i=s-~g.index(m);return[[2-((i:=i+i%~i)<s)+(i>s)]*i+r[i:]for r in g]
# 💎 task 257: 68 bytes, gold, https://arcprize.org/play?task=a68b268e
p=lambda a:[p(b)for*b,in map(zip,a,a[5:])]or max(sum(a,()),key=bool)
# 🥇 task 258: 61 bytes, gold, https://arcprize.org/play?task=a699fb00
import re
p=lambda a:eval(re.sub('1, 0(?=, 1)','1,2',str(a)))
# 🥈 task 259: 85 vs 84 bytes for gold, https://arcprize.org/play?task=a740d043
p=lambda i,k=39:-k*i or p([*zip(*eval(str(i).replace(*"10"))[any(i[-1])-2::-1])],k-1)
# 💎 task 260: 130 bytes, gold, https://arcprize.org/play?task=a78176bb
exec("p=lambda a:[[max({*max(a)}-{5})*any(a[i][j]%5or 2==sum(m-n-i+j+k%5==2<a[m][n]"+'for %s in range(10)%s'*6%(*'m n k)_)j]i]',))
# 🥇 task 261: 47 bytes, gold, https://arcprize.org/play?task=a79310a0
p=lambda a:[[e%3for e in r]for r in[a.pop()]+a]
# 🥇 task 262: 39 bytes, gold, https://arcprize.org/play?task=a85d4709
p=lambda i:[[~b//~a^2]*3for a,b,_ in i]
# 💎 task 263: 117 bytes, gold, https://arcprize.org/play?task=a87f7484
p=lambda g:g[(T:=[*zip(*[map(bool,sum(g,g*0))]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p((*zip(*g),)))]
# 🥈 task 264: 193 (241 unzipped) vs 189 bytes for gold, https://arcprize.org/play?task=a8c38be5
p=lambda g:[[sorted([g[+y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]for y in range(len(g)-2)for x in range(len(g[0])-2)],key=lambda g:[0==y for y in g]+[5==y for y in g])[b'mloeb( ra'[y//3*3+x//3]%9][y%3*3+x%3]for x in range(9)]for y in range(9)]
# 🥉 task 265: 118 vs 104 bytes for gold, https://arcprize.org/play?task=a8d7556c
import re;p=lambda g:[g:=[*zip(*eval(re.sub("[^5]{4}(.{52})0, 0(?![^0]{14}0, 0)","2,2\\1 2,2",str(g))))]for _ in g][7]
# 💎 task 266: 99 bytes, gold, https://arcprize.org/play?task=a9f96cdd
p=lambda g:[([0,0,0,r%9,0,r%8]*2)[4-max(g).index(2):][:5]for r in b'HfHGH'[2-g.index(max(g)):][:3]]
# 🥇 task 267: 46 bytes, gold, https://arcprize.org/play?task=aabf363d
p=lambda i:[[i[6][[y]<x]for y in x]for x in i]
# 🥈 task 268: 222 (278 unzipped) vs 218 bytes for gold, https://arcprize.org/play?task=aba27056
def p(i):l,f=[(e:=r,o:=n)for r in range(len(i))for n in range(len(i))if i[r][n]][0];return i[e][o-2]and[*zip(*p([[*r]for r in zip(*i[::-1])]))][::-1]or[i for r in range(l+1,len(i))for n in({*range(f+2,o-1),e-r+f+2,o-2+r-e}&{*range(len(i))},range(f+1,o))[r<e]for i[r][n]in[4]][0]
# 🥇 task 269: 63 bytes, gold, https://arcprize.org/play?task=ac0a08a4
p=lambda a:eval("[[a\nfor a in a for _ in[*{*'%s'}][5:]]#"%a*2)
# 🥈 task 270: 117 vs 116 bytes for gold, https://arcprize.org/play?task=ae3edfdc
import re;p=lambda i,k=7:-k*i or eval(re.sub(f"({k|3})([^)]*)0(, {2-k//4})",r"0\2\1\3",str([*zip(*p(i,k-1)[::-1])])))
# 💎 task 271: 86 bytes, gold, https://arcprize.org/play?task=ae4f1146
p=eval(f"lambda a:max([str(a).count('1'),a]{'for*a,in map(zip,a,a[1:],a[2:])'*2})[1]")
# 💎 task 272: 71 bytes, gold, https://arcprize.org/play?task=aedd82e4
p=lambda i,*w:i*0!=0and[*map(p,i,[i*2]+i,i[1:]+[i*2],*w)]or~(2in w)*i%3
# 🥉 task 273: 114 vs 108 bytes for gold, https://arcprize.org/play?task=af902bf9
p=lambda g,R={*range(10)}:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in R^{i}for J in{j}^R})//5*2for j in R]for i in R]
# 🥇 task 274: 71 bytes, gold, https://arcprize.org/play?task=b0c4d837
p=lambda i:[(h:=[8for x in i if sum(x)==10]+[0]*5)[:3],h[5:2:-1],[0]*3]
# 💎 task 275: 130 bytes, gold, https://arcprize.org/play?task=b190f7f5
p=lambda i:('8'in str(j:=i[(u:=len(i[0])):]))*[[t*y/8for t in s for y in x]for s in i[:u]for x in j]or[*zip(*p([*zip(*j+i[:u])]))]
# 🥇 task 276: 38 bytes, gold, https://arcprize.org/play?task=b1948b0a
p=lambda a:eval(str(a).replace(*'62'))
# 💎 task 277: 155 bytes, gold, https://arcprize.org/play?task=b230c067
z=[0];p=lambda g,k=38,h=2,q=z*9:~k*g or p([q:=[v and[v%63,P|p|v,h:=h*64,v//sum(g,z).count(v)][k>>4]for P,p,v in zip(z+q,z+r,r)]for*r,in zip(*g[::-1])],k-1)
# 💎 task 278: 116 bytes, gold, https://arcprize.org/play?task=b27ca6d3
import re;p=lambda i:[i:=eval(re.sub("0(?=(.%s.{,9}|..)2, 2)"%{len(i)*3-5},"3",str([*zip(*i[::-1])])))for _ in i][3]
# 🥉 task 279: 109 vs 107 bytes for gold, https://arcprize.org/play?task=b2862040
p=lambda g,f=18:~f*g or p([*map(lambda*r,a=0:[a:=9&b%[9|3-a,a+9,10][f//9]or(f<0)*9for b in r],*g[::-1])],f-1)
# 💎 task 280: 168 bytes, gold, https://arcprize.org/play?task=b527c5c6
def p(a,n=3,i=0):
 for b in a:
  B=bytes(b+[0]).find;d=B(0,c:=B(b'\0')+1)+~c;i+=1
  for e in a[i+~d:i+d]:e[:c]=[e[c]]*c
 return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
# 💎 task 281: 103 bytes, gold, https://arcprize.org/play?task=b548a754
p=lambda a,n=47,*P:-n*a or p([*zip(*[max(P*({0,8}in map(set,a)),P:=a.pop(),key=set)for _ in a*1])],n-1)
# 💎 task 282: 76 bytes, gold, https://arcprize.org/play?task=b60334d2
p=lambda i,*x,c=0:[c|(c:=i)>>2|(i:=y)for y in x+x[7:]]or[*map(p,*map(p,*i))]
# 💎 task 283: 72 bytes, gold, https://arcprize.org/play?task=b6afb2da
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or-i%8*w.count(5)%5
# 🥈 task 284: 204 vs 201 bytes for gold, https://arcprize.org/play?task=b7249182
p=lambda i:[i:=[*zip(*len(l:=[n for n,y in E(m)if y])%2*i)]or[[(23//(X:=sum(l)-b-b)**2*9+(l[0]<=b<=l[1])>>a*a&1)*m[l[X<0]]for a,_ in E(i,-i.index(m))]for b,_ in E(m)]for E in[enumerate]*2if[m:=max(i)]][1]
# 💎 task 285: 274 (431 unzipped) bytes, gold, https://arcprize.org/play?task=b775ac94
def	p(o):
	for*i,in[[]]*8:
		o=[i[::-1]for*i,in	zip(*o)]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				if	m:
					n={(r,e)}
					for	t	in*i,:
						if{(r-1,e),(r,e-1),(r-1,e+1),(r-1,e-1)}&t:i.remove(t);n|=t
					i+=[n]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				for	t	in*i,:
					for	n,f	in	t:
						if{(n-e,f-~r),(n-~e,f-r)}&t:o[n-e][f-r]|=len({*str([i[f:f+2]for*i,in	o[n:n+2]])})//8*o[n][f]
	return	o
# 💎 task 286: 105 bytes, gold, https://arcprize.org/play?task=b782dc8a
p=lambda i,k=39:-k*i or[[t:=y or sum({*sum(t%8*i,[])}-{t,8})for y in[8]+x][:0:-1]for*x,in zip(*p(i,k-1))]
# 💎 task 287: 55 bytes, gold, https://arcprize.org/play?task=b8825c91
p=lambda*a:sum({*a[3:]}-{4})or[*map(p,*a+a,a[0][::-1])]
# ❌ task 288: 91 vs 88 bytes for gold, https://arcprize.org/play?task=b8cdaf2b
def p(i,n=0):
 l=len(i)//2;*w,S,L=i
 for x in w[l-0**S[-l]:]:x[n]=x[~n]=L[l];n+=1
 return i
# 🥇 task 289: 63 bytes, gold, https://arcprize.org/play?task=b91ae062
p=lambda a:eval("[[a\nfor a in a for _ in[*{*'%s'}][5:]]#"%a*2)
# 🥉 task 290: 68 vs 67 bytes for gold, https://arcprize.org/play?task=b94a9452
p=lambda i,r=[]:r*-1*-1or[p(x,sum({*r}or i,x*-1))for x in i if[x]>i]
# 🥈 task 291: 62 vs 61 bytes for gold, https://arcprize.org/play?task=b9b7f026
p=lambda i,n=1:len({x.count(n)for x in i})//3*[[n]]or p(i,n+1)
# 💎 task 292: 53 bytes, gold, https://arcprize.org/play?task=ba26e723
p=lambda g,v=0:g*0!=0and[*map(p,g,b''*7)]or g*v//4
# 🥈 task 293: 60 vs 59 bytes for gold, https://arcprize.org/play?task=ba97ae07
p=lambda a:[[d^c^b[0]or d for*_,c,d in zip(*a,b)]for b in a]
# 🥇 task 294: 70 bytes, gold, https://arcprize.org/play?task=bb43febb
import re;p=lambda m:eval(re.sub('(?<=5.{34})5(?=.{34}5)','2',str(m)))
# 🥇 task 295: 54 bytes, gold, https://arcprize.org/play?task=bbc9ae5d
p=lambda a:[b:=a[0]]+[b:=b[:1]+b[:-1]for _ in b[2::2]]
# 🥇 task 296: 63 bytes, gold, https://arcprize.org/play?task=bc1d5164
p=lambda g:[[*map(max,a,b,a[4:],b[4:])]for a,b in zip(g,g[2:])]
# 🥇 task 297: 43 bytes, gold, https://arcprize.org/play?task=bd4472b8
p=lambda i:i[:2]+[*zip(*i[:1]*len(i[0]))]*2
# 🥇 task 298: 55 bytes, gold, https://arcprize.org/play?task=bda2d7a6
p=lambda i:[[i[3][~-x.index(y)%3]for y in x]for x in i]
# 🥇 task 299: 54 bytes, gold, https://arcprize.org/play?task=bdad9b1f
p=lambda i:[[3%~t+2&8-(2in x)for t in i[0]]for x in i]
# 🥇 task 300: 87 bytes, gold, https://arcprize.org/play?task=be94b721
p=lambda a,*n:[b for*b,in zip(*n or p(a,*a))if max(range(1,10),key=sum(a,a).count)in b]
# 🥇 task 301: 31 bytes, gold, https://arcprize.org/play?task=beb8660c
p=lambda g,S=sorted:S(map(S,g))
# 🥉 task 302: 91 vs 89 bytes for gold, https://arcprize.org/play?task=c0f76784
import re;p=lambda i:eval(re.sub("5,([ 0,]*)5(?!, 5)",r"5,*[5+(r:=len([\1]))]*r,5",str(i)))
# ❌ task 303: 64 vs 62 bytes for gold, https://arcprize.org/play?task=c1d99e64
p=lambda a:[[d^2^2*any(b)*any(c)for*c,d in zip(*a,b)]for b in a]
# 🥇 task 304: 92 bytes, gold, https://arcprize.org/play?task=c3e719e8
p=lambda i:[[t*(y==max(z:=sum(i,i),key=z.count))for y in x for t in s]for x in i for s in i]
# 🥇 task 305: 57 bytes, gold, https://arcprize.org/play?task=c3f564a4
p=lambda g:[([*{*g[0]}-{0}]*9)[y:y+16]for y in range(16)]
# 🥇 task 306: 63 bytes, gold, https://arcprize.org/play?task=c444b776
p=lambda i:[i:=[*zip(*map(max,i,i[:10]+i))][::-1]for _ in i][7]
# 💎 task 307: 46 bytes, gold, https://arcprize.org/play?task=c59eb873
p=lambda a:a>a*0!=0and[p(a[0])]*2+p(a[1:])or a
# 💎 task 308: 205 bytes, gold, https://arcprize.org/play?task=c8cbb738
e=enumerate
def p(g):q=range(m:=min(A:={J-sum(C)//4:N for N in sum(g,g)if len(C:=[C+A*8for(A,B)in e(g)for(C,E)in e(B)if E==N])<5or(M:=N)*0for J in C})+3>>3,1-m);return[[A.get(y*8+x,M)for x in q]for y in q]
# 🥇 task 309: 38 bytes, gold, https://arcprize.org/play?task=c8f0f002
p=lambda a:eval(str(a).replace(*'75'))
# 💎 task 310: 70 bytes, gold, https://arcprize.org/play?task=c909285e
p=lambda a,*n:[b for b in zip(*n or p(a,*a))if{*b}-({*a[1]}&{*a[12]})]
# 🥇 task 311: 32 bytes, gold, https://arcprize.org/play?task=c9e6f938
p=lambda a:[r+r[::-1]for r in a]
# 🥇 task 312: 44 bytes, gold, https://arcprize.org/play?task=c9f8e694
p=lambda a:[[e%~e&r[0]for e in r]for r in a]
# 💎 task 313: 62 bytes, gold, https://arcprize.org/play?task=caa06a1f
p=lambda g,s=[0]:s*-1*-1or[*map(p,g,(s+g)[1:3+len(s)//12]*10)]
# 💎 task 314: 82 bytes, gold, https://arcprize.org/play?task=cbded52d
p=lambda i,*w:i*0!=0and[*map(p,i,i[:3]+i,i[3:]+i,*w)]or max(w[0]&w[1],w[2]&w[3],i)
# 🥇 task 315: 63 bytes, gold, https://arcprize.org/play?task=cce03e0d
p=lambda i:[[t&-y%5for y in x for t in s]for x in i for s in i]
# 🥇 task 316: 71 bytes, gold, https://arcprize.org/play?task=cdecee7f
p=lambda i:[(q:=[*filter(abs,map(max,*i))]+[0]*9)[:3],q[5:2:-1],q[6:9]]
# 💎 task 317: 43 bytes, gold, https://arcprize.org/play?task=ce22a75a
p=lambda a:a==5or a and[p(a[1])]*3+p(a[3:])
# 🥇 task 318: 54 bytes, gold, https://arcprize.org/play?task=ce4f8723
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[5:]+n)]or(-a<n)*3
# 🥉 task 319: 236 (303 unzipped) vs 194 bytes for gold, https://arcprize.org/play?task=ce602527
def p(a):g=max(f:=sum(A:=a,[]),key=f.count);return[[[[g,A][A==e]for*b,A in zip(*a,b)if e in b]for b in a if e in b]for e in{*f}for i in range(52)for j in range(52)if[]<(b:=[a for a,A in zip(a,sum(zip(A,A),((),)*19)[i:])for a,A in zip(a,sum(zip(A,A),((),)*19)[j:])if a!=A==e!=g])==b[:1]*f.count(b[0])][0]
# 💎 task 320: 66 bytes, gold, https://arcprize.org/play?task=ce9e57f2
p=lambda a:[*zip(*[c[:-(w:=sum(c)//4)]+w*[8]+c for*c,in zip(*a)])]
# 🥇 task 321: 55 bytes, gold, https://arcprize.org/play?task=cf98881b
p=lambda m:[[r.pop(0)or r[4]|r[9]for _ in m]for r in m]
# 🥇 task 322: 48 bytes, gold, https://arcprize.org/play?task=d037b0a7
p=lambda a:[[*map(max,*a[:n]*2)]for n in(1,2,3)]
# 🥉 task 323: 107 vs 102 bytes for gold, https://arcprize.org/play?task=d06dbe63
p=lambda a,B=3:[[v|5*((b:=abs((B:=B-3)+str(a).find('8')))>~b%76in b'KHE"')for v in r]for r in a if[B:=B-2]]
# 💎 task 324: 228 (261 unzipped) bytes, gold, https://arcprize.org/play?task=d07ae81c
def p(g):k,K,b,B=T=sorted({*sum(g,[])},key=sum(g,[]).count);return[[([T[k!=C!=T[~all({k,B}!={*r}!={K,b}for r in[*zip(*g)]+g)]]for y,r in enumerate(g)for x,c in enumerate(r)if c in(k,K)!=abs(x-X)==abs(y-Y)]+[C])[0]for X,C in enumerate(r)]for Y,r in enumerate(g)]
# 💎 task 325: 140 bytes, gold, https://arcprize.org/play?task=d0f5fe59
p=lambda i,z=8,*w:i[22:]and[[8*(a==b)for b in w]for a in w]or p([[s:=h and(z:=z*2)|s|h for h in[0]+x]for*x,in zip(*i[::-1])],*{*sum(i,[0])})
# 🥇 task 326: 30 bytes, gold, https://arcprize.org/play?task=d10ecb37
p=lambda a:[a[0][:2],a[1][:2]]
# 🥇 task 327: 67 bytes, gold, https://arcprize.org/play?task=d13f3404
p=lambda i,l=[0]*3:[l:=[*map(max,x+[0]*3,[0]+l*2)]for x in i+[l]*3]
# 💎 task 328: 158 bytes, gold, https://arcprize.org/play?task=d22278a0
exec("p=lambda g:[[(D:=sorted((sum(T:=[abs(x-r),abs(y-c)]),~max(T)%2*f[y])"+'for %s,f in enumerate(g)%s'*4%(*'y x','if f[y]))[0][1]*(D[0]<D[1][:1])',*'c]r]'))
# 🥇 task 329: 54 bytes, gold, https://arcprize.org/play?task=d23f8c26
p=lambda a:[[0]*(l:=len(r)//2)+[r[l]]+l*[0]for r in a]
# 💎 task 330: 110 bytes, gold, https://arcprize.org/play?task=d2abd087
p=lambda i,k=-19,z=1:k*i or p([[e:=y and[1+y%7//6,z:=z*8,e|y][k>>4]for y in[0]+i][:0:-1]for*i,in zip(*i)],k+1)
# 🥇 task 331: 83 bytes, gold, https://arcprize.org/play?task=d364b489
p=lambda i,k=2:k//9*i or p(eval(str([*zip(*i[::-1])]).replace("1,","1,k|")),k*9%11)
# 🥇 task 332: 58 bytes, gold, https://arcprize.org/play?task=d406998b
p=lambda m:[[x-len(r)*r.pop(0)%2*2for x in[*r]]for r in m]
# 🥇 task 333: 89 bytes, gold, https://arcprize.org/play?task=d43fd935
p=lambda a,n=-3:n*a or[(d:=0)or[d:=b.pop()or d*(3in b)for _ in a]for*b,in zip(*p(a,n+1))]
# 🥉 task 334: 69 vs 66 bytes for gold, https://arcprize.org/play?task=d4469b4b
p=lambda i:[[(y>>max(max(i)))%2*5for y in[x,x|6,x|8]]for x in[4,2,8]]
# 🥉 task 335: 110 vs 107 bytes for gold, https://arcprize.org/play?task=d4a91cb9
p=lambda a,n=10,d=0:~n*a or p([[b.pop()|(n%6*2in b)*(d:=d^4%(sum(c)|4))for c in a[::-1]]for*b,in zip(*a)],n-3)
# 💎 task 336: 90 bytes, gold, https://arcprize.org/play?task=d4f3cd78
p=lambda i,k=3:-k*i or[[x.pop()or(sum(x)%8|1in x[:5])*8for _ in i]for*x,in zip(*p(i,k-1))]
# 💎 task 337: 43 bytes, gold, https://arcprize.org/play?task=d511f180
p=lambda x:x*-1and x^84%x%3*13or[*map(p,x)]
# 🥉 task 338: 68 vs 64 bytes for gold, https://arcprize.org/play?task=d5d6de2d
p=lambda i,s=0:[(t:=1)*[(s:=t<y-s&6)*3>>(t:=y)for y in x]for x in i]
# 🥇 task 339: 37 bytes, gold, https://arcprize.org/play?task=d631b094
p=lambda a:[[*filter(int,sum(a,[]))]]
# 💎 task 340: 112 bytes, gold, https://arcprize.org/play?task=d687bc17
p=lambda i:[i:=[[sum({v,r[0]}&{*i[1],*r[~(j:=j%5%-3):]})for v in r][::-1]for*r,in zip(*i)if[j:=2]]for _ in i][3]
# 💎 task 341: 115 bytes, gold, https://arcprize.org/play?task=d6ad076f
p=lambda i:[i:=[[b[a]or(v:=2+({*s}>{*s[a:]}>{0}and v))&8for b,s in zip(i,i[1:]+i)]for a in range(10)]for r in i][1]
# 🥈 task 342: 111 vs 110 bytes for gold, https://arcprize.org/play?task=d89b689b
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub("([1-9])((.{32})+?[0, ]+)8",r"0\2\1",str(p(i,k-1)))))][::-1]
# 💎 task 343: 64 bytes, gold, https://arcprize.org/play?task=d8c310e9
p=lambda i:[(h[:8-2*(h[8:12]!=h[:4]!=h[4:8])]*3)[:15]for h in i]
# 💎 task 344: 74 bytes, gold, https://arcprize.org/play?task=d90796e8
p=lambda i,*w:i*0!=0and[*map(p,i,[i*4]+i,i[1:]+[i*4],*w)]or(i^1in w)+7&i*9
# 💎 task 345: 89 bytes, gold, https://arcprize.org/play?task=d9f24cd1
p=lambda i,a=0,*h:i[1:]and[[c[1]|2&6%~sum(h)+max((h:=c)[1:])for c in zip(*i)]]+p(i[a:],1)
# 💎 task 346: 52 bytes, gold, https://arcprize.org/play?task=d9fac9be
p=lambda a:[[min(b:=sum(a[1:-1],a[3]),key=b.count)]]
# 🥇 task 347: 50 bytes, gold, https://arcprize.org/play?task=dae9d2b5
p=lambda a:[[6^6>>e+r.pop(3)for e in r]for r in a]
# 💎 task 348: 94 bytes, gold, https://arcprize.org/play?task=db3e9e38
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,in a[1:]]+a,n+1)
# 🥈 task 349: 204 (277 unzipped) vs 194 bytes for gold, https://arcprize.org/play?task=db93a21d
p=lambda	i:[i:=[[max(i[e][m],(e-r+a	in	range(a*4))*(m-n+a	in	range(a*4))*3,9in(e[m]for	e	in	i[:e]))for	m	in	range(len(i))]for	e	in	range(len(i))]for	a	in	range(len(i))for	r	in	range(-a*2,len(i))for	n	in	range(len(i)-a*2+1)if{min(e[n:a*2+n])for	e	in	i[max(r,0):a*2+r]}=={9}][-1]
# 💎 task 350: 89 bytes, gold, https://arcprize.org/play?task=dbc1a6ce
p=lambda i:[*map(f:=lambda*x,s=0:[y|(x.count(1)>(s:=s+y%8)>y<1)*8for y in x],*map(f,*i))]
# 💎 task 351: 66 bytes, gold, https://arcprize.org/play?task=dc0a314f
p=lambda i:[r[:5]for x in[*i]if(r:=i.pop()[~[*x,3].index(3)::-1])]
# 💎 task 352: 82 bytes, gold, https://arcprize.org/play?task=dc1df850
p=lambda i:[i:=[[x.pop()or[0]<x[-1:]<[3]for _ in i]for*x,in zip(*i)]for _ in i][3]
# 💎 task 353: 85 bytes, gold, https://arcprize.org/play?task=dc433765
p=lambda a,n=-3:n*a or p([*zip(*[a.pop(-~sum(r)in sum(a,r))for r in a*1][::-1])],n+1)
# 🥇 task 354: 96 bytes, gold, https://arcprize.org/play?task=ddf7fa4f
p=lambda i:[i:=[[(y==5)*c[c[1]>0]or y for*c,y in zip([0]+x,*i,x)][::-1]for x in i]for x in i][9]
# 🥉 task 355: 101 vs 98 bytes for gold, https://arcprize.org/play?task=de1cd16c
p=lambda a:[sorted(range(10),key=lambda c:sum(e!=c in{*b}&{*d}for b in a for*d,e in zip(*a,b)))[8:9]]
# 💎 task 356: 100 bytes, gold, https://arcprize.org/play?task=ded97339
p=lambda i,*I:[[W[b]|sum({*w[b:]}&{*w[:b]})for b in range(10)]for*W,w in zip(*I or p(zip(*i),*i),i)]
# 🥇 task 357: 86 bytes, gold, https://arcprize.org/play?task=e179c5f4
p=lambda m,x=1,d=1:m and p(m,x:=x-d*2+1,1>>x*(l:=len(m.pop())+~x)^d)+[[8]*x+[1]+[8]*l]
# 💎 task 358: 91 bytes, gold, https://arcprize.org/play?task=e21d9049
p=lambda i,k=23:-k*i or[[*map(max,x,84//len({*x,0})%6*[0]+x)]for*x,in zip(*p(i,k-1)[::-1])]
# 🥇 task 359: 64 bytes, gold, https://arcprize.org/play?task=e26a3af2
p=lambda g:[[max(w:=c+r,key=w.count)for*c,in zip(*g)]for r in g]
# 🥇 task 360: 45 bytes, gold, https://arcprize.org/play?task=e3497940
p=lambda a:[[*map(max,b,b[:4:-1])]for b in a]
# 💎 task 361: 185 (241 unzipped) bytes, gold, https://arcprize.org/play?task=e40b9e2f
def p(a):I=[a+a for a in a+a];return[[[I[x][y]|I[a-b+y][a+b+n+~x]|I[a+a+n+~x][b+b+n+~y]|I[a+b+n+~y][b-a+x]for y in range(10)]for x in range(10)]for n in range(10)for b in range(10)for a in range(10)if all(all(a[b:b+n])for a in I[a:a+n])][-1]
# 🥇 task 362: 69 bytes, gold, https://arcprize.org/play?task=e48d4e1a
p=lambda g:[r[(n:=g.count(g[0])):9]+r[:1]+r[:n]for r in g*2][10-n:-n]
# 💎 task 363: 204 bytes, gold, https://arcprize.org/play?task=e5062a87
def p(g):
 f=lambda C:{x+x//10*80for x in range(100)if C==g[x//10][x%10]};v=f(2)
 for y in f(0)|f(5):
  for Y in(m:=[Y+y-min(v)for Y in v])*(hash((*g[0],))%263+y!=99!={*m}<f(0)):g[Y//90][Y%90]=2
 return g
# 💎 task 364: 134 bytes, gold, https://arcprize.org/play?task=e509e548
p=lambda i,k=11,s=[0]*22:-k*i or p([s:=[[y%7*9%13%9,u*t%2<<k%4*3+6|y|u][k>0<y]for y,t,u in zip(x,[0]+x,s)]for*x,in zip(*i)][::-1],k-1)
# 🥇 task 365: 111 bytes, gold, https://arcprize.org/play?task=e50d258f
p=lambda a:max([-(c:=sum(b:=[b[x%8:x%11]for b in a[x%9:x%13]],a).count)(0),c(2),c(1),b]for x in range(5**6))[3]
# 💎 task 366: 302 (495 unzipped) bytes, gold, https://arcprize.org/play?task=e6721834
def p(g):
 *s,m,b,B=sorted({*sum(g,[])},key=sum(g,[]).count)
 *s,=g,
 for r in s*6:
  for r in s+(s:=[]):
   s+=[],
   for r in zip(*r):s+=s.pop()+[r]if{b,B}-{*r}>{b}or{*r}>{b}else[],
 [6for y,s in sorted((-sum(m^s for s in s for s in s),s)for s in s)for y,r in enumerate(g)for x,r in enumerate(r)for h,r in zip(g[y:]+g,s*all((a==r)!=(m==r)==(a==B)for h,r in zip(g[y:]+g,s)for a,r in zip(h[x:x+len(r)]+g,r)))for h[x:x+len(r)]in[r]];return[r for r in zip(*[r for r in zip(*g)if B in r])if B in r]
# 💎 task 367: 126 bytes, gold, https://arcprize.org/play?task=e73095fd
import re
p=lambda g,k=-19:k*g or p(eval(re.sub(f"0(?=, 4|.{ {N:=len(g)*3+4}}5, 0.{ {N-6}}0)","4",str([*zip(*g)][::-1]))),k+1)
# 💎 task 368: 132 bytes, gold, https://arcprize.org/play?task=e76a88a6
import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m:re.findall("([^50](, [1-9])+)",s*2)[-s[m.end()-1::32].count('5')][0],s:=str(i)))
# 🥇 task 369: 109 bytes, gold, https://arcprize.org/play?task=e8593010
p=lambda g,k=-11,z=1:k*g or[[P:=v&7or[z:=z*8,4-v%7,P&~5|v][k>>3]for v in[5]+r][:0:-1]for*r,in zip(*p(g,k+1))]
# 💎 task 370: 228 (357 unzipped) bytes, gold, https://arcprize.org/play?task=e8dc4411
def	p(a):
	for	f	in	range(4):m=[*map(min,a)].index(0);i=[*map(min,a)].count(0);a=[*map(list,zip(*a))][::-1];u=[*map(min,a)].index(0);[0for	f	in	range(4)for	d	in	range(i)for	n	in	range(i)for	a[u-1+a[u][m]//-9*~f-i*f-d][m-1+a[u][m]//-9*~f-i*f-n]in	a[u-1+a[u][m]//8][m-1+a[u][m]%8:][:1>a[u+d][m+n]<=u-1+a[u][m]//-9*~f-i*f-d|m-1+a[u][m]//-9*~f-i*f-n]]
	return	a
# 💎 task 371: 109 bytes, gold, https://arcprize.org/play?task=e9614598
def p(a):
 for i in[l:=len(a[0]),-l,1,0,-1]:b=sum(a,[]).index;i+=b(1,b(1)+1)+b(1)>>1;a[i//l][i%l]=3
 return a
# 🥇 task 372: 48 bytes, gold, https://arcprize.org/play?task=e98196ab
p=lambda a:[b for*b,in map(map,[max]*5,a,a[6:])]
# 🥉 task 373: 39 vs 38 bytes for gold, https://arcprize.org/play?task=e9afcf9a
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]
# 💎 task 374: 107 bytes, gold, https://arcprize.org/play?task=ea32f347
p=lambda g,l=128:-l*g or p([*zip(*(a:=eval(str(g).replace(l//12*"5, ",l//12*"4>>l%3,"))))][::-1],l-3+(g>a))
# 🥇 task 375: 53 bytes, gold, https://arcprize.org/play?task=ea786f4a
def p(g,i=0):
 for r in g:r[i]=r[~i]=0;i+=1
 return g
# 🥇 task 376: 30 bytes, gold, https://arcprize.org/play?task=eb281b96
p=lambda a:(a+a[1:-1])*2+a[:1]
# 🥇 task 377: 55 bytes, gold, https://arcprize.org/play?task=eb5a1d5d
p=lambda g,*a:[g:=y for*y,in zip(*a or p(g,*g))if g!=y]
# 💎 task 378: 141 bytes, gold, https://arcprize.org/play?task=ec883f72
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub("0(?=(%s 0)*%s ., [^0]%s?%s (.))"%(('.%s.0,'%{3*len(i)},)*4),"\\2",str(p(i,k-1)))))][::-1]
# 🥇 task 379: 141 bytes, gold, https://arcprize.org/play?task=ecdecbb3
import re
p=lambda i,k=7,r=re.sub:-k*i or[*zip(*eval(r(", 4, ","|8,8,8|",r("0, 8, ((0, )+)2","4,2,4,*[2]*len([\\1])",str(p(i,k-1)[::-1])))))]
# 🥇 task 380: 27 bytes, gold, https://arcprize.org/play?task=ed36ccf7
p=lambda a:[*zip(*a)][::-1]
# 🥇 task 381: 79 bytes, gold, https://arcprize.org/play?task=ef135b50
p=lambda i,s=9:[[y|(sum(x)>(s:=s+y)>(x!=i[9])>y)*9for y in x]*(s:=1)for x in i]
# 💎 task 382: 124 bytes, gold, https://arcprize.org/play?task=f15e1fac
p=lambda i,k=-3:k*i or p([*zip(w:=i.pop(),*[[*map(max,r,w:=r*('8'in'%s'%i)+[0,*w,0][r[-1]or[1]>r:])]for*r,in i[::-1]])],k+1)
# 🥇 task 383: 121 bytes, gold, https://arcprize.org/play?task=f1cefba8
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]
# 🥇 task 384: 62 bytes, gold, https://arcprize.org/play?task=f25fbde4
p=lambda a,*n:[b for b in zip(*n or p(*a))for _ in"00"*any(b)]
# 🥇 task 385: 25 bytes, gold, https://arcprize.org/play?task=f25ffba3
p=lambda a:a[:4:-1]+a[5:]
# 🥇 task 386: 52 bytes, gold, https://arcprize.org/play?task=f2829549
p=lambda a:[[3>>e+r.pop(0)for e in r[4:]]for r in a]
# 🥈 task 387: 205 vs 202 bytes for gold, https://arcprize.org/play?task=f35d900a
p=lambda i,k=6,e=enumerate,S=sum:~k*i or p([[y or([(S(x[b:])*S(x[:b])%5>S(r:=S([(),*zip(*i[b+b%~b:b+2])][a:a+3],()))<x[b-2]+x[b+2])*5,*{*S(i,[])}-{*r,5}]*3)[3>>k]for b,y in e(x)]for a,x in e(zip(*i))],k-2)
# ❌ task 388: 62 vs 61 bytes for gold, https://arcprize.org/play?task=f5b8619d
p=lambda a:2*[2*[d or any(c)*8for*c,d in zip(*a,b)]for b in a]
# 🥇 task 389: 57 bytes, gold, https://arcprize.org/play?task=f76d97a5
p=lambda a:[[sum({*sum(a,r)}-{e,5})for e in r]for r in a]
# 🥉 task 390: 100 vs 98 bytes for gold, https://arcprize.org/play?task=f8a8fe49
import re
p=lambda g,*G:eval(re.sub("([^2(]{9}2[^2]{9})",r"*[\1][::-1]","%s"%[*zip(*G or p(g,*g))]))
# 🥇 task 391: 63 bytes, gold, https://arcprize.org/play?task=f8b3ba0a
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]
# 🥉 task 392: 152 vs 149 bytes for gold, https://arcprize.org/play?task=f8c80d96
exec("p=lambda n:[[(a:=max(max(n)),5,5)[min(max(f-b,b-f,m-s,s-m)"+'for %s in range(10)%s'*4%(*'b s',"if n[b][s])%(3-(f', {a}, 0'*2in'%s'%n))]",*'m]f]'))
# 🥇 task 393: 63 bytes, gold, https://arcprize.org/play?task=f8ff0b80
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# 💎 task 394: 85 bytes, gold, https://arcprize.org/play?task=f9012d9b
p=lambda i:[[v for y,v in zip(x,x[n:n*2]+x)if 1>y]for x in i if(n:=122%len(i))>0in x]
# 🥇 task 395: 53 bytes, gold, https://arcprize.org/play?task=fafffa47
p=lambda a,n=[]:a*0!=0and[*map(p,a,a[3:]+n)]or~a+~n&2
# 💎 task 396: 139 bytes, gold, https://arcprize.org/play?task=fcb5c309
p=lambda m,n=266,f=0:[[sum({*e*sum(m,[-f])})for e in s]for r in m if(f:=((X:=n>>5)*[a:=(r*3)[x:=n%32]]in(s:=r[x:x+X],[f]*X))*a)]or p(m,n-1)
# 💎 task 397: 113 bytes, gold, https://arcprize.org/play?task=fcc82909
p=lambda m,k=71:exec('r=k//9;exec("%s=3,3;"*len(a:={*%s+%s})*all(a));k-=1;'%(('m[r:=r+1][k%9:k%9+2]',)*3)*81)or m
# 💎 task 398: 73 bytes, gold, https://arcprize.org/play?task=feca6190
p=lambda a,b=45:[*zip(*[2*((b:=b-1)*[0]+a[0])for c in 5*a[0]if c])][b:45]
# 🥇 task 399: 64 bytes, gold, https://arcprize.org/play?task=ff28f65a
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]
# 💎 task 400: 66 bytes, gold, https://arcprize.org/play?task=ff805c23
p=lambda g:[h[:5]for r in[*g]if(h:=g.pop()[~[*r,1].index(1)::-1])]
