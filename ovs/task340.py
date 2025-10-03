p=lambda i:[i:=[[sum({v,r[0]}&{r[-1],*i[1],*r[j**5:]})for j,v in enumerate(r)][::-1]for*r,in zip(*i)]for _ in i][3]
# enumerate + [::-1] looks a bit annoying
