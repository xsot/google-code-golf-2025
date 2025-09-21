# ovs (71 bytes, gold)
p=lambda i:[(q:=[*filter(abs,map(max,*i))]+[0]*9)[:3],q[5:2:-1],q[6:9]]

### combined (72 bytes)
p=lambda i:[(q:=sorted(map(max,*i),key=0 .__eq__))[:3],q[5:2:-1],q[6:9]]
