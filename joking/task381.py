p=lambda i,E=enumerate:[[y or(a%9>0<2in{*x[b:]}&{*x[:b]})*9for b,y in E(x)]for a,x in E(i)]

##
p=lambda i,r=range(10):[[(x:=i[a])[b]or(a%9>0<2in{*x[b:]}&{*x[:b]})*9for b in r]for a in r]
p=lambda i:i[:1]+[[x[b]or(2in{*x[b:]}&{*x[:b]})*9for b in range(10)]for x in i[1:-1]]+i[-1:]
p=lambda i:i[:1]+[(b:=0)or[y|((b:=b|x.pop(0))>y<2in x)*9for y in[*x]]for x in i[1:-1]]+i[-1:]