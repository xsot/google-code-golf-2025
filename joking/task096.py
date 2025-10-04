# zip fiddling
def p(g,*S):
 for C in{b:=max(d:=sum(g,[]),key=d.count)}^{*d}:d=max([*g,*zip(*g)],key=lambda d:d.count(C));I=0;D=max(d:=min(d:=[-I+(I:=d.index(C,I)+1)for v in d if v==C][1:],d[::-1])+[0]);S+=((2*d.index(D)or len(d)-1)+D|1,D,C),
 R=range(d:=max(S)[0]);return[[[*[C for W,G,C in S if W-1==max(abs(d+~v-v)for v in(i,v))>=min(abs(d+~v-v)for v in(i,v))>G-2],b][0]for v in R]for i in R]