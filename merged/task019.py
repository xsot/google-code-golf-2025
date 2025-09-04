# ovs (126 vs 118 bytes for gold)
E=enumerate
p=lambda g:[[v or 8*any([*[*g*2,[0]*9][y+d%5-1]*2,0][x+d%3-1]for d in b'-/29')for x,v in E(l*2)]for y,l in E(g*2)]

### combined (tied, 126 bytes)
E=enumerate
p=lambda g:[[v or 8*any([*[*g*2,[0]*9][y+d%5-1]*2,0][x+d%3-1]for d in b'-/29')for x,v in E(l*2)]for y,l in E(g*2)]
