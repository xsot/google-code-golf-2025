# joking (121 bytes, gold)
p=lambda g:exec("q=[]\nfor r in zip(*g):q+=q[::-1]*({*r}^{2}=={3}<{*q[-1]})or[[v or 3for v in r]]\ng[:]=q[9::-1];"*8)or g


##
p=lambda i:{*i[s:=str(i).index(", 2")//31]+i[s+1]}-{2,3}and[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]or i[:s]+(i*2)[9+s::-1]
p=lambda i:({*(r:=sum(i,i[0]))[(s:=r.index(2)//10)*10:]}<={2,0})*eval(str(i[:s-1]+i[s-2::-1]+i[:1]*9).replace(*"03"))[:10]or[*zip(*p([*zip(*i[::-1])]))][::-1]
p=lambda i:{*i[s:=sum(i,i[0]).index(2)//10-1]+i[s+1]}<={2,3}and i[:s]+i[s-1::-1]+i[:1]*9or[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]
p=lambda g:exec("q=[]\nfor r in zip(*g):q+=q[::-1]*({*r}=={2,3}<{2,*q[-1]})or[[v or 3for v in r]]\ng[::-1]=q[:10];"*8)or g

### ovs (125 bytes)
def p(g):
 for*q,in[[]]*8:[q:=(q[::-1]*({*r}^{2}=={3}<{*q[0]})or[[v or 3for v in r]])+q for r in zip(*g)];g=q[-10:]
 return g

### combined (175 bytes)
p=lambda i,e=enumerate:{*(r:=sum(i,i[0][:0]))[(s:=r.index(2)//10)*10:]}<={2,0}and eval(str((i[:s]+i[s-1::-1]+i[:1]*9)[:10]).replace(*"03"))or[*zip(*p([*zip(*i[::-1])]))][::-1]
