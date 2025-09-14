# ovs (68 vs 61 bytes for gold)
p=lambda a:[*zip(*(c:=(A:=[*zip(*a)])[:len(A)//2])*(A==c*2)or p(A))]

### att (75 bytes)
p=lambda a:[a[:len(a)//2],c:=[b[:len(b)//2]for b in a]][a==[b*2for b in c]]

### combined (75 bytes)
p=lambda a:[a[:len(a)//2],c:=[b[:len(b)//2]for b in a]][a==[b*2for b in c]]
