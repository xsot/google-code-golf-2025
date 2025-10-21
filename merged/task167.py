# ovs (70 bytes, gold)
p=lambda i:[[5*(y==x%len({*str(i)})%3)for x in b'']for y in(0,1,2)]

### combined (85 bytes)
p=lambda i:[b:=[[0,0,5],[0,5,0],[5,0,0]],b[::-1],[[5]*3]+[[0]*3]*2][4-len({*str(i)})]
