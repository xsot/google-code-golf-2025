p=lambda i:[[[t[-1],y][y==l]for*s,y in zip(*i,x)if l in s]for x in i if(l:=(t:=sorted({*(z:=sum(i,[]))},key=z.count))[(q:=0)+hash((*z,))%5009%2681in[q:=q+n for n in b' ">?,v%6&!!	B!Z%$7!0NK"?ND|Rt	']])in x]

## generation code:
examples=load_examples(319)
e = examples['train'] + examples['test'] + examples['arc-gen']
p = [set(),set()]
for l in e:
    t = sorted({*(z:=sum(l['input'],[]))},key=z.count)
    f={t.index(c)for c in {*sum(l['output'],[])}}
    p[min(f)]|={hash((*z,))}

# there are 156 zeroes vs 111 ones, focus on identifying the ones
print(len(p[0]),len(p[1]))
print(p[0]&p[1])

t=[]

# get some viable modulos
for a in range(2,10000):
 l=[{y%a for y in x}for x in p]
 if l[0]&l[1]:continue
 t.append(([a],l))
 if len(t)>200:break

# loop over the next mod chain and print viable
for s in t:
 p=s[-1]
 for b in range(2,max(p[0]|p[1])):
  l = [{y%b for y in x}for x in p]
  if l[0]&l[1]:continue
  n=sorted(l[1])
  d = [a-b for a,b in zip(n,[0]+n)]
  if max(d) < 128 and len({13,10,0}&{*d}) == 0:
   print(len(d),d)
   print("".join(map(chr,d)))
   print(s[0]+[b])

# next steps:
# get a better setup lol?
# or else:
#  encode the resulting data better
#  increase collisions in the ones set