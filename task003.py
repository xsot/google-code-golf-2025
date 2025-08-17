p=lambda m:eval(str(m+m[2*(m[0]!=m[3]):][:3]).replace(*'12'))

###
p=lambda m:eval(str(m+m[2*(m[0]!=m[3]):][:3]).translate({49:50}))
p=lambda m:eval(str(m+m[2*(m[1]!=m[4]):][:3]).translate({49:50}))