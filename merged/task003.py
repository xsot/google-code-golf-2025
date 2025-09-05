# ovs (60 vs 2500 bytes for gold)
p=lambda g:[[v*2for v in l]for l in g+g[g[:2]!=g[4:]:][2:5]]

### combined (tied, 60 bytes)
p=lambda g:[[v*2for v in l]for l in g+g[g[:2]!=g[4:]:][2:5]]

### xsot (61 bytes)
p=lambda m:eval(str(m+m[2*(m[0]!=m[3]):][:3]).replace(*'12'))

###
p=lambda m:eval(str(m+m[2*(m[0]!=m[3]):][:3]).translate({49:50}))
p=lambda m:eval(str(m+m[2*(m[1]!=m[4]):][:3]).translate({49:50}))
