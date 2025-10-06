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