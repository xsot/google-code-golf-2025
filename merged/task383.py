# joking+mwi (121 bytes, gold)
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]

### ovs (tied, 121 bytes)
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]

## alternative with four rotations:
p=lambda g,k=-3:g*k or p([[*[[P[v>0]for v in r]for*P,in zip([0,0]+r,[0]+r,r)if len({*P})==3>0==P[2]],r][0]for*r,in zip(*g[::-1])],k+1)
