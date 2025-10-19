# compression_experiments (283 (377 unzipped) bytes, gold)
import re
def p(n):f={0:(a:=max(n:=re.sub(', ','',str(n+[*zip(*n)])),key=n.count),2)}|{(m:=len(re.findall(e+e+'([^]+)'+e+']+)'+e+'|$',n+n[::-1])[0]))-len(max(re.findall(e+'+',n)))*~(m>0)>>1:(e,m-1>>1)for e in{*n}-{a,*'([]+)'}};return[[int([a,*f[max(abs(e),abs(m))]][f[max(abs(e),abs(m))][1]<min(abs(e),abs(m))])for e in range(-max(f),max(f)+1)]for m in range(-max(f),max(f)+1)]

### joking (284 (377 unzipped) bytes)
# derived from regex solution by kenkridge
# 284
import re
def p(r):l={0:(i:=max(r:=re.sub(', ','',str(r+[*zip(*r)])),key=r.count),2)}|{(d:=len(re.findall(t+t+'([^]+)'+t+']+)'+t+'|$',r+r[::-1])[0]))-len(max(re.findall(t+'+',r)))*~(d>0)>>1:(t,d-1>>1)for t in{*r}-{i,*'([]+)'}};return[[int([i,*l[max(abs(t),abs(d))]][l[max(abs(t),abs(d))][1]<min(abs(t),abs(d))])for t in range(-max(l),max(l)+1)]for d in range(-max(l),max(l)+1)]

##
import re
def p(#[*'_irlt']##):l={0:(i:=max(r:=re.sub('#[', ','. ',',.']##','',str(#[prev_vals[0]]##+[*zip(*#[prev_vals[0]]##)])),key=r.count),#[*range(10)]##)}|{(d:=len(re.findall(t+t+'([^]+)'+t+']+)'+t+'|$',r+r[::-1])[0]))-len(max(re.findall(t+'+',r)))*~(#['d>0','0<d']##)>>1:(t,d-1>>1)for t in{*r}-{#["i,*'([]+)'","*i+'([]+)'","*'([]+)'+i"]##}};return[[int([i,*l[max(abs(t),abs(d))]][l[max(abs(t),abs(d))][1]<min(abs(t),abs(d))])for t in range(-max(l),max(l)+1)]for d in range(-max(l),max(l)+1)]

## non-regex
def p(g,*S):
 for C in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda d:d.count(C));I=0;D=max(d:=min(d:=[-I+(I:=d.index(C,I)+1)for v in d if v==C][1:],d[::-1])+[0]);S+=((2*d.index(D)or len(d)-1)+D|1,D,C),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W-1==max(abs(d+~v-v)for v in(i,v))>=min(abs(d+~v-v)for v in(i,v))>G-2],b][0]for v in R]for i in R]

### ovs (301 (378 unzipped) bytes)
def p(g,*S):
 for c in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda r:r.count(c));I=0;D=max(d:=min(d:=[-I+(I:=d.index(c,I)+1)for v in d if v==c][1:],d[::-1])+[0]);S+=((2*d.index(D)or~-len(d))+D|1,D-2,c),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W==1+max(abs(d+~v-v)for v in(i,v))>min(abs(d+~v-v)for v in(i,v))>G],b][0]for v in R]for i in R]

### garry_moss (309 (400 unzipped) bytes)
# Garry modified from kenkridge's notebook https://www.kaggle.com/code/kenkrige/chipping-skills-3-regex/comments
import re
def p(i):
 r=re.sub(', ','',str(i+[*zip(*i)]));r+=r[::-1];i=int(max(r,key=r.count));l={0:(0,i)}
 for t in range(10):
  if(t!=i)*(e:=re.findall(f'{t}+',r)):d=len((re.findall(f'{t}{t}([^]){t}]+){t}',r)or[''])[0]);o=len(max(e))*((d>0)+1);l[o+d>>1]=d+1>>1,t
 return[[i*((d:=l[r[1]])[0]>r[0])or d[1]for t in range(-max(l),max(l)+1)if(r:=sorted((abs(t),abs(e))))]for e in range(-max(l),max(l)+1)]

### mwi (320 (373 unzipped) bytes)
def	p(g,*S):
	for	c	in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i	for	i,v	in	enumerate(r)if	v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for	x	in	r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
	R=range(w:=max(S)[0]);return[[([C	for	W,G,C	in	S	if	G<(M:=sorted(abs(w//2-v)for	v	in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for	j	in	R]for	i	in	R]

### combined (321 (373 unzipped) bytes)
def p(g,*S):
 for c in{b:=max(f:=sum(g,[]),key=f.count)}^{*f}:r=max([[i for i,v in enumerate(r)if v==c]for*r,in[*g,*zip(*g)]],key=len);D=max(d:=min(d:=[x-r.pop(0)for x in r[1:]],d[::-1])+[0]);S+=((d.index(D)*2or~-len(d))+D|1,D-2,c),
 R=range(w:=max(S)[0]);return[[([C for W,G,C in S if G<(M:=sorted(abs(w//2-v)for v in(i,j)))[0]*2<M[1]*2+1==W]+[b])[0]for j in R]for i in R]
