# joking+mwi (85 vs 72 bytes for gold)
p=lambda i:[b:=[[0,0,5],[0,5,0],[5,0,0]],b[::-1],[[5]*3]+[[0]*3]*2][4-len({*str(i)})]
