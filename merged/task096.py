# joking (298 (380 unzipped) bytes, gold)
# zip fiddling
def p(g,*S):
 for C in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda d:d.count(C));I=0;D=max(d:=min(d:=[-I+(I:=d.index(C,I)+1)for v in d if v==C][1:],d[::-1])+[0]);S+=((2*d.index(D)or len(d)-1)+D|1,D,C),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W-1==max(abs(d+~v-v)for v in(i,v))>=min(abs(d+~v-v)for v in(i,v))>G-2],b][0]for v in R]for i in R]

### ovs (301 (378 unzipped) bytes)
def p(g,*S):
 for c in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda r:r.count(c));I=0;D=max(d:=min(d:=[-I+(I:=d.index(c,I)+1)for v in d if v==c][1:],d[::-1])+[0]);S+=((2*d.index(D)or~-len(d))+D|1,D-2,c),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W==1+max(abs(d+~v-v)for v in(i,v))>min(abs(d+~v-v)for v in(i,v))>G],b][0]for v in R]for i in R]

### mwi (320 (373 unzipped) bytes)
def	p(g,*S):
	for	c	in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i	for	i,v	in	enumerate(r)if	v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for	x	in	r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
	R=range(w:=max(S)[0]);return[[([C	for	W,G,C	in	S	if	G<(M:=sorted(abs(w//2-v)for	v	in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for	j	in	R]for	i	in	R]

### combined (321 (373 unzipped) bytes)
def p(g,*S):
 for c in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i for i,v in enumerate(r)if v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for x in r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
 R=range(w:=max(S)[0]);return[[([C for W,G,C in S if G<(M:=sorted(abs(w//2-v)for v in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for j in R]for i in R]
