# ovs (225 (235 unzipped) vs 189 bytes for gold)
p=lambda g:max([[min(w:=r+c,key=w.count)for*c,in zip(*S)]for r in S]for A in range(len(g.pop(0))-6)if(s:=lambda w:len({*sum([r[A:A+6]for r in g[:6]],w[:6])})<=2)for S in[[[v for v,*c in zip(r,*g)if s(c)]for r in g if s(r[A:])]])or p(g)

### joking+mwi (231 bytes)
p=lambda i,x=0:(k:=[z for a in range(225)if len(z:=[t[x%30:][:a%15]for t in i[x//30:][:a//15]])>5<len(z[0])>2==len({*sum(z,[])})])and[[max(s-{*k[-1][0]})if len(s:={*y,*x})>1else y[0]for y in zip(x,*k[-1])]for x in k[-1]]or p(i,x+1)
