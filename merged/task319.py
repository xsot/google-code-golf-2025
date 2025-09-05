# att (243 (293 unzipped) vs 194 bytes for gold)
def p(a):g=max(f:=sum(A:=a,[]),key=f.count);return[[[[g,d][d==e]for*b,d in zip(*a,b)if e in b]for b in a if e in b]for e in{*f}for i in range(2652)if[]<(b:=[a for a,A in zip(a,sum(zip(A,A),((),)*19)[i%51:])for a,A in zip(a,sum(zip(A,A),((),)*19)[i%52:])if a!=A==e!=g])==b[:1]*f.count(b[0])][0]

### ovs (267 bytes)
# see joking's solution for details
p=lambda i:[[[t[3],y][y==l]for*s,y in zip(*i,x)if l in s]for x in i if(l:=(t:=sorted({*(z:=sum(i,[]))},key=z.count))[1&b'1 Ds	`E$@  !%0a,)@\n   @%@@@'[(m:=hash((*z,))%3999%2529%1577%989%616)//7]>>m%7])in x]

## legit solve, zips to 275:

def p(g):f=sum(g,[]);*r,b=T={C:{i*1j+j for i,r in enumerate(g)for j,v in enumerate(r)if C==v}for C in sorted(f,key=f.count)};return[[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]for c in r for l in r for o in T[l]if T[c]in({i*2+q+a-o*2for i in T[l]for a in(0,1,1j,1+1j)}&set().union(*T.values())for q in T[c])][0]

### joking (280 bytes)
# this can probably be shortened a bit with a lot more bruteforcing, but i doubt it can reach sub 200
# maybe there's a better way to generate a binary number with a lot of zeroes?
q=0
for n in b'@@@%@   \n@),a0%!  @$E`	sD 1':q=q*128+n
p=lambda i:[[[t[-1],y][y==l]for*s,y in zip(*i,x)if l in s]for x in i if(l:=(t:=sorted({*(z:=sum(i,[]))},key=z.count))[1&q>>hash((*z,))%3999%2529%1577%989%616])in x]

## base 36 version
p=lambda i:[[[t[-1],y][y==l]for*s,y in zip(*i,x)if l in s]for x in i if(l:=(t:=sorted({*(z:=sum(i,[]))},key=z.count))[1&int("UVXTWA4FWP709TG8WKB7YZMZLETQU9Z2HCC4AMP7LV1AWF2II79QRUG7JTZG6QGHW1JWBWFZ8RWOPGMIAL8BE9UR1VNP1GV06DXVOSYKQIH60E87DVHFZT4",36)>>hash((*z,))%3999%2529%1577%989%616])in x]


## generation code:
examples=load_examples(319)
e = examples['train'] + examples['test'] + examples['arc-gen']
p = [set(),set()]
for l in e:
   t = sorted({*(z:=sum(l['input'],[]))},key=z.count)
   f={t.index(c)for c in {*sum(l['output'],[])}}
   p[min(f)]|={hash((*z,))}

print(len(p[0]),len(p[1]))
print(p[0]&p[1])

base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(number, base):
   result = ""
   while number:result += base_string[number % base];number //= base
   return result[::-1] or "0"

ratio = 0.7
def modchain(lis, level, mods = []):
 if level == 0:
  n=sorted(lis[1])
  if max(lis[1]) <= 615:
   print(max(lis[1]))
   print(lis)
   print("%".join(map(str,mods)))
   q=0
   for n in lis[1]:q|=2**n
   b36 = to_base(q, base=36)
   print(len(b36),b36)
   r=[]
   h=0
   while q:
    s=q%2**7
    if s==0:
     s=1
     while h+s in lis[0]:s+=1
     s=2**s
    r+=[s]
    q=q//2**7
    h+=7

   # if r[0]<10, we can use it as our initial value
   r="".join(map(chr,r[::-1])).replace("\0","\\0").replace("\n","\\n").replace("\r","\\r")
   print(len(r),"b'"+r+"'")
   die
 else:
  for a in range(2,int(min(10000,max(lis[0]|lis[1]))*ratio)):
   l=[{y%a for y in x}for x in lis]
   if l[0]&l[1]:continue
   modchain(l, level-1, mods + [a])

modchain(p, 5)

## ideas
# you could maybe bruteforce something like any((q:=q+x)<hash<(q:=q+y) for x,y in stuff)
# better bruteforcing: in the end, it's a split of 1s and 0s. maybe there's a straight up condition that can seperate them. we can mess with the hash generation quite a bit if we want

# theoretically, this format is 136 bytes pre-hash
# 267 cases with 1 bit of information divided by 7 bits gives us 38 ascii chars to work with, which seems doable?

# old method
## this one checks if the hash modulo is in a list, unfortunately this means the list basically has to be the size of the number of ones
p=lambda i:[[[t[-1],y][y==l]for*s,y in zip(*i,x)if l in s]for x in i if(l:=(t:=sorted({*(z:=sum(i,[]))},key=z.count))[(q:=0)+hash((*z,))%5009%2681in[q:=q+n for n in b' ">?,v%6&!!	B!Z%$7!0NK"?ND|Rt	']])in x]

### mwi (304 (396 unzipped) bytes)
def p(g):
 f=sum(g,[]);*r,b=sorted({*f},key=f.count);W,H=len(g[0]),len(g);T={C:{(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if C==v}for C in r}
 for c in r:
  for l in r:
   if T[c]in({(i*2+q+a,j*2+Q+A)for i,j in T[l]for a in(0,1)for A in(0,1)if H>i*2+q+a>-1<j*2+Q+A<W}for q in range(-H*2,H*2)for Q in range(-W*2,W*2)):return[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]

### combined (306 (392 unzipped) bytes)
E=enumerate
def p(g):
 f=sum(g,[]);*r,b=sorted({*f},key=f.count);W,H=len(g[0]),len(g);T={C:{(i,j)for i,r in E(g)for j,v in E(r)if C==v}for C in r}
 for c in r:
  for l in r:
   if T[c]in({(i*2+q+a,j*2+Q+A)for i,j in T[l]for a in(0,1)for A in(0,1)if H>i*2+q+a>-1<j*2+Q+A<W}for q in range(-H*2,H*2)for Q in range(-W*2,W*2)):return[[[b,l][v==l]for*c,v in zip(*g,r)if l in c]for r in g if l in r]
