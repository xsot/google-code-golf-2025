# att (46 bytes, gold)
p=lambda g:[[x^84%x%3*13for x in r]for r in g]

### att (48 bytes)
p=lambda a:eval(str(a).translate({53:56,56:53}))

### xsot (48 bytes)
p=lambda m:eval(str(m).translate({53:56,56:53}))

##
p=lambda m:eval(str(m).translate({53:56,56:53}))
p=lambda m:[[{i:i,5:8,8:5}[i]for i in r]for r in m]
