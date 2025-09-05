# joking (143 vs 2500 bytes for gold)
p=lambda i:{*i[s:=str(i).index(", 2")//31]+i[s+1]}-{2,3}and[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]or i[:s]+(i*2)[9+s::-1]

##
p=lambda i:({*(r:=sum(i,i[0]))[(s:=r.index(2)//10)*10:]}<={2,0})*eval(str(i[:s-1]+i[s-2::-1]+i[:1]*9).replace(*"03"))[:10]or[*zip(*p([*zip(*i[::-1])]))][::-1]
p=lambda i:{*i[s:=sum(i,i[0]).index(2)//10-1]+i[s+1]}<={2,3}and i[:s]+i[s-1::-1]+i[:1]*9or[*zip(*p(eval(str([*zip(*i)][::-1]).replace(*"03")))[9::-1])]

### combined (175 bytes)
p=lambda i,e=enumerate:{*(r:=sum(i,i[0][:0]))[(s:=r.index(2)//10)*10:]}<={2,0}and eval(str((i[:s]+i[s-1::-1]+i[:1]*9)[:10]).replace(*"03"))or[*zip(*p([*zip(*i[::-1])]))][::-1]
