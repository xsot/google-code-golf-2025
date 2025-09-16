# ovs (128 vs 132 bytes for gold)
p=eval(f'lambda i:[[max([i{" for i in i[a-3:a]+i[a+3:a:-1]for a in[b]"*2}if i][:-3]+[i[a][b]])'+'for %c in range(6)]'*2%(98,97))

##

def p(g):
 o=eval(str(g));R={*range(6)}
 for i in R:
  for j in R:
   for S in b' *#-':
    for A in({i+(d:=S%5-1),j+(D:=S%3-1)}<R!=0<o[i+d][j+D])*b"*/&+":
     if{b:=A%5*d+i,B:=A%4*D+j}<R:g[b][B]=g[b][B]or o[i][j]
 return g

### joking (132 bytes)
p=lambda i,r=range(6):[[max([s for t in i[a-3:a]+i[a+3:a:-1]for s in t[b-3:b]+t[b+3:b:-1]if s][:-3]+[i[a][b]])for b in r]for a in r]

### combined (145 bytes)
p=lambda i,k=3,r=range(6):-k*i or[[p([*zip(*i[::-1])],k-1)[b][~a]+max([*[s for t in i[a%3:a]for s in t[b%3:b]if s][:-3],0])for b in r]for a in r]
