# att (113 bytes, gold)
p=lambda g,f=126:~f*g or p([*map(lambda*r,a=0:[[b+7*(a>1==b),b%(9+a),(a:=b)or 9][f>>6]for b in r],*g[::-1])],f-1)

### ovs (118 bytes)
p=lambda g,f=126:~f*g or p([[[b+7*(a>7>1==b),b%(9+a),b or 9][f>>6]for a,b in zip([0]+r,r)]for*r,in zip(*g[::-1])],f-1)
