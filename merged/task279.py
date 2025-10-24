# joking (109 vs 106 bytes for gold)
p=lambda g,f=18:~f*g or p([*map(lambda*r,a=0:[a:=9&b%[9|3-a,a+9,10][f//9]or(f<0)*9for b in r],*g[::-1])],f-1)

##
p=lambda g,f=26:~f*g or p([*map(lambda*r,a=0:[a:=9&b%[9|3-a,a+9,10][f>>4]or(f<0)*9for b in r],*g[::-1])],f-1)

### ovs (110 bytes)
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=9:[9&b%[9|12-a,a,a:=9+b][f>>6]or(f<0)*9for b in r],*g[::-1])],f-1)

### att (113 bytes)
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=0:[[b+7*(a>1==b),b%(9+a),(a:=b)or 9][f>>6]for b in r],*g[::-1])],f-1)

### combined (113 bytes)
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=0:[[b+7*(a>1==b),b%(9+a),(a:=b)or 9][f>>6]for b in r],*g[::-1])],f-1)
