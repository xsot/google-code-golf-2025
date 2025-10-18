# ovs (91 vs 90 bytes for gold)
p=lambda i,*h:[[c[1]|2&6%~sum(h)+max((h:=c)[1:])for c in zip(*i[a:])]for a in[0,*range(9)]]

### joking (93 bytes)
# maybe there's some way to get rid of the range(10)?
p=lambda i,*h:[[c[1]|2&6%~sum(h)+max((h:=c)[1:])for c in zip(*i[a+a%~a:])]for a in range(10)]

### combined (109 bytes)
p=lambda i,r=range(10):[[i[a][b]|2&6%~sum((t:=[*zip(*i)])[b-1][a-(a>0):])+max(t[b][a:])for b in r]for a in r]
