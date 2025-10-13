# joking (86 vs 84 bytes for gold)
p=lambda g,h=2,w=0:h and[p(g,h-1,w^A>>w//8)for A in range(9)][::1-g[h][-h]|1]or(w<4)*3

##
p=lambda g,h=2,w=0:[p(g,h-1,w^A>>w//8)for A in range(h%~h&9)][::1-g[h][-h]|1]or(w<4)*3
p=lambda g,h=-2,w=0:[p(g,h+1,w^A>>w//8)for A in range(h%9-h)][::1-g[-h][h]|1]or(w<4)*3

##
p=lambda g,R=range(9):[[3*((7%~g[2][1]^A)%9//4==(7%~g[1][2]^B)%9//4<2)for B in R]for A in R]
p=lambda g,R=range(9):[[3*((g[2][1]%-2^A)%9&12==(g[1][2]%-2^B)%9&12<7)for B in R]for A in R]
p=lambda g,R=range(9):[[3*((7%~g[2][1]^A)%9&12==(7%~g[1][2]^B)%9&12<7)for B in R]for A in R]
p=lambda g,R=[1]*4+[2]*4+[0]:[[A%~B*3%6for B in R][::~-g[1][0]//2]for A in R][::~-g[0][1]//2]
p=lambda g,R=range(9):[[3*(B//4==A//4<2)for B in R][::~-g[1][0]//2]for A in R][::~-g[0][1]//2]

### ovs (88 bytes)
p=lambda g,h=0,w=0:h<2and[p(g,h+1,w^A>>w//8)for A in range(9)][::g[h][1-h]-2|1]or(w<4)*3

##

p=eval('lambda g:[[3*(A^B<4>A-4)'+'for %s in range(9)[::g[%s][%s]-2|1]]'*2%(*'B10A01',))

### combined (94 bytes)
p=lambda g,R=range(9):[[3*(B//4==A//4<2)for B in R][::~-g[1][0]//2]for A in R][::~-g[0][1]//2]
