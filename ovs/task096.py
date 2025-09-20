def p(g,*S):
 for c in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda r:r.count(c));I=0;D=max(d:=min(d:=[-I+(I:=d.index(c,I)+1)for v in d if v==c][1:],d[::-1])+[0]);S+=((2*d.index(D)or~-len(d))+D|1,D-2,c),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W==1+max(abs(d+~v-v)for v in(i,v))>min(abs(d+~v-v)for v in(i,v))>G],b][0]for v in R]for i in R]
