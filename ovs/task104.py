p=lambda g,h=2,w=3:h and[p(g,h-1,w&2-A//4)for A in range(9)][::1-g[h][-h]|1]or-w%3^w

##
p=lambda g,h=0,w=0:h<2and[p(g,h+1,w^A>>w//8)for A in range(9)][::g[h][1-h]-2|1]or(w<4)*3
p=eval('lambda g:[[3*(A^B<4>A-4)'+'for %s in range(9)[::g[%s][%s]-2|1]]'*2%(*'B10A01',))
