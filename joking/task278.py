import re;p=lambda i:[i:=eval(re.sub("0(?=(.%s.{,9}|..)2, 2)"%{len(i)*3-5},"3",str([*zip(*i[::-1])])))for _ in i][3]

##
p=lambda i,e=enumerate:[i:=[[y or("2, 2"in"%s"%[h[a:a+3]for h in i[b+b%~b:b+2]])*3for b,y in e(x)]for a,x in e(zip(*i))][::-1]for _ in i][3]
import re;p=lambda i:exec('i[:]=zip(*eval(re.sub("0(?=(.%s.{,9}|..)2, 2)"%{len(i[0])*3-5},"3",str(i[::-1]))));'*4)or i