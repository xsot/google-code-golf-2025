p=lambda r:[[sorted([[0==n for n in r[n][o:3+o]+r[1+n][o:3+o]+r[1+1+n][o:3+o]],[5==n for n in r[n][o:3+o]+r[1+n][o:3+o]+r[1+1+n][o:3+o]],r[n][o:3+o]+r[1+n][o:3+o]+r[1+1+n][o:3+o]]for n in range(len(r)-2)for o in range(len(r[0])-2))[b'dlfnb( ra'[n//3*3+o//3]%9][2][n%3*3+o%3]for o in range(9)]for n in range(9)]


##
p=lambda g:[[sorted([[0==y for y in g[y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]],[5==y for y in g[y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]],g[y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]]for y in range(len(g)-2)for x in range(len(g[0])-2))[b'mloeb( ra'[y//3*3+x//3]%9][2][y%3*3+x%3]for x in range(9)]for y in range(9)]
p=lambda g:[[sorted([[0==y for y in g[y][x:3+x]+g[y+1][x:3+x]+g[y+1+1][x:3+x]],[5==y for y in g[y][x:3+x]+g[y+1][x:3+x]+g[y+1+1][x:3+x]],g[y][x:3+x]+g[y+1][x:3+x]+g[y+1+1][x:3+x]]for y in range(len(g)-2)for x in range(len(g[y])-2))[b'#[*'md']##l#[*'of']###[*'en']###[*'bt']###[*'p(']## ra'[y//3*3+x//3]%9][2][y%3*3+x%3]for x in range(9)]for y in range(9)]

##
p=lambda g:[[sorted([g[+y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]for y in range(len(g)-2)for x in range(len(g[0])-2)],key=lambda g:[0==y for y in g]+[5==y for y in g])[b'mloeb( ra'[y//3*3+x//3]%9][y%3*3+x%3]for x in range(9)]for y in range(9)]
p=lambda g:[[sorted([g[+y][x:3+x]+g[1+y][x:3+x]+g[1+1+y][x:3+x]for y in range(len(g)-2)for x in range(len(g[0])-2)],key=lambda g:[0==x for x in g]+[5==x for x in g])[b'#[*'md']###[*'lu']###[*'of']###[*'en']###[*'bt']###[*'p(']## ra'[y//3*3+x//3]%9][y%3*3+x%3]for x in range(9)]for y in range(9)]