import re
def p(r):l={0:(i:=max(r:=''.join(str(r+[*zip(*r)]).split(', ')),key=r.count),1)}|{(d:=len(D:=max(map(''.join,re.findall(f'({t}([{t}]+)\d+?{t}|{t}+)',r+r[::-1])),key=len)))>>1:(t,d-D.count(t))for t in{*r}-{i,*'([{t}]+)'}};return[[int([i,*l[max(abs(t),abs(d))]][l[max(abs(t),abs(d))][1]/2<=min(abs(t),abs(d))])for t in range(-max(l),max(l)+1)]for d in range(-max(l),max(l)+1)]

##
def p(g,*S):
 for c in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda r:r.count(c));I=0;D=max(d:=min(d:=[-I+(I:=d.index(c,I)+1)for v in d if v==c][1:],d[::-1])+[0]);S+=((2*d.index(D)or~-len(d))+D|1,D-2,c),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W==1+max(abs(d+~v-v)for v in(i,v))>min(abs(d+~v-v)for v in(i,v))>G],b][0]for v in R]for i in R]
