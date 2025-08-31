# combined (46 vs 43 bytes for gold)
p=lambda g:[[b" 	"[c]for c in g[0]]]*3

### xsot (tied, 46 bytes)
# note: edit in vim, not vscode 
p=lambda m:[[b'AA	'[i]for i in m[0]]]*3
##
p=lambda m:[[b'AA	'[i]for i in m[0]]]*3
p=lambda m:[[b'	'[-~i%9]for i in m[0]]]*3
p=lambda m:[[b'(-.,+)*/10'[i]-40for i in m[0]]]*3
p=lambda m:[[590324385360>>i*4&15for i in r]for r in m]
p=lambda m:[[[9,8,5,6,4,3,1,2][-~i%9]for i in r]for r in m]
p=lambda m:[[[-1,5,6,4,3,1,2,-1,9,8][i]for i in r]for r in m]

### ovs (51 bytes)
p=lambda g:[[(v^792>>v&53)%10for v in l]for l in g]
