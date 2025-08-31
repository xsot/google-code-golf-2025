# ovs (127 vs 106 bytes for gold)
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)

### combined (tied, 127 bytes)
R=range(12)
p=lambda g,k=-39:g*k or p([[g[j][~i]or(str(g)[~i*3-~j*38::35][1:3]in map(str,b"X&! "))*3for j in R]for i in R],k+1)
