# joking+mwi (72 vs 71 bytes for gold)
p=lambda i:[(q:=sorted(map(max,*i),key=0 .__eq__))[:3],q[5:2:-1],q[6:9]]
