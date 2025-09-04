# mwi (187 vs 140 bytes for gold)
p=lambda i,n=1:(s:=[[[y>0for*s,y in zip(*i,x)if n in s]for x in i if n in x]for n in range(10)]).count(s[n]or 1)>1<=n not in i[0][:3]+i[1][:3]and eval(str(i).replace(*f"{n}5"))or p(i,n+1)

### combined (189 bytes)
p=lambda i,n=1:(s:=[[[y>0for*s,y in zip(*i,x)if n in s]for x in i if n in x]for n in range(10)]).count(s[n]or 1)>1<=n not in i[0][:3]+i[1][:3]and eval(str(i).replace(str(n),"5"))or p(i,n+1)
