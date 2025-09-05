# ovs (121 vs 2500 bytes for gold)
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]

### combined (tied, 121 bytes)
p=lambda g,*G:[[r,[(o:=[*{}.fromkeys(r)]*3)[1+0**v]for v in r]][str(o)[1:8]in f'{r+r[::-1]}']for r in zip(*G or p(g,*g))]
