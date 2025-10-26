# att (126 bytes, gold)
p=eval(f'lambda i:[[([i[a][b]]*4+[i{" for i in i[a-3:a]+i[a+3:a:-1]for a in[b]"*2}if i])[-4]'+'for %c in range(6)]'*2%(98,97))

##
import re;p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'0(?=(, 0)?(.{20}){1,2}, ([^0]).{22}(?!\3|0)(.), 0)',r'\4',str(p(a,n+1)))))][::-1]

### joking (128 bytes)
# alt. i think there might be some way to rearrange this to save a byte or two
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if(c:=b)*i+i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))

##
p=eval(f'lambda i:[[max([i{" for i in i[%s-3:%s]+i[%s+3:%s:-1]"*2}if i][:-3]+[i[a][b]]){"for %s in range(6)]"*2}'%(*'aaaabbbbba',))
p=eval("lambda i:[[max([i\nfor i in i[a-3:a]+i[a+3:a:-1]for a in[b]#"*2+'\nif i][:-3]+[i[a][b]])'+'for %c in range(6)]'*2%(98,97))
p=eval(f'lambda i:[[max([i[a][b]]+[i{" for i in i[%s-3:%s]+i[:%s:-1][-3:]"*2}if i][:-3]){"for %s in range(6)]"*2}'%(*'aaabbbba',))
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if[c:=b]and i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if-~(c:=b)*i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))

p=lambda i,r=range(6):[[max([s for t in i[a-3:a]+i[a+3:a:-1]for s in t[b-3:b]+t[b+3:b:-1]if s][:-3]+[i[a][b]])for b in r]for a in r]

### ovs (128 bytes)
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

### combined (145 bytes)
p=lambda i,k=3,r=range(6):-k*i or[[p([*zip(*i[::-1])],k-1)[b][~a]+max([*[s for t in i[a%3:a]for s in t[b%3:b]if s][:-3],0])for b in r]for a in r]
