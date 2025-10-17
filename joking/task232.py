p=lambda i,e=0:i*0!=0and[p(y)or[e:=y-e,5][e<0]for y in i]

##
p=lambda i:[(e:=0)or[max(e:=y-e,e>>9&5)for y in x]for x in i]
p=lambda i:[(e:=0)or[(e:=y-e)>>9&5or e for y in x]for x in i]