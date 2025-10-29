p=lambda i:[(t:=0)or[(i:=t**y==i)*3>>(t:=y)for y in x]for x in i]

##
p=lambda i,s=0:[(t:=1)*[(s:=t<y-s&6)*3>>(t:=y)for y in x]for x in i]