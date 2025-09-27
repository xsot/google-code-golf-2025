# ovs (130 bytes, gold)
p=lambda i,n=1,*w:any(w==(w:=[*map(len,s:=str(i).split(str(n)))][1:-1])for n in{max(i[:3])[0]:0,n:0})*eval('5'.join(s))or p(i,n+1)

### mwi (137 bytes)
p=lambda i,n=1,w=0:any(w==(w:=[*map(len,str(i).split(str(n))[1:-1])])for n in{n,max(i[:3])[0]})*eval(str(i).replace(*f"{n}5"))or p(i,n+1)

### combined (189 bytes)
p=lambda i,n=1:(s:=[[[y>0for*s,y in zip(*i,x)if n in s]for x in i if n in x]for n in range(10)]).count(s[n]or 1)>1<=n not in i[0][:3]+i[1][:3]and eval(str(i).replace(str(n),"5"))or p(i,n+1)
