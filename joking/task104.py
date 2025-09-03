p=lambda g,R=range(9):[[3*((7%~g[2][1]^A)%9//4==(7%~g[1][2]^B)%9//4<2)for B in R]for A in R]

##
p=lambda g,R=range(9):[[3*((g[2][1]%-2^A)%9&12==(g[1][2]%-2^B)%9&12<7)for B in R]for A in R]
p=lambda g,R=range(9):[[3*((7%~g[2][1]^A)%9&12==(7%~g[1][2]^B)%9&12<7)for B in R]for A in R]
p=lambda g,R=[1]*4+[2]*4+[0]:[[A%~B*3%6for B in R][::~-g[1][0]//2]for A in R][::~-g[0][1]//2]
p=lambda g,R=range(9):[[3*(B//4==A//4<2)for B in R][::~-g[1][0]//2]for A in R][::~-g[0][1]//2]