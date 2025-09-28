# ovs (144 vs 133 bytes for gold)
r=-1,0,1
p=lambda g:[w for a in range(5000)if len({*str(w:=[[max(g[(y+A)%10][(x+A//10)%10]for A in(a,a%99))for x in r]for y in r])}^{'0'})>6][0]

### att (153 bytes)
s=' in[a '+'for*a,in map(zip,a[9:]+a,a,a[1:]+a)'*2
p=eval(f'lambda a:max(all(sum(d:=[[*map(int.__xor__,*e)]for*e,in zip(b,c)],a))*d for b{s}]for c{s}])')

### mwi (173 bytes)
def p(g):u=[[(r*2)[x//10:][:3]for r in(g*2)[x%10:][:3]]for x in range(99)];return max(all(sum(t:=[[x^y for y,x in zip(A,B)]for A,B in zip(a,b)],[]))*t for a in u for b in u)

### combined (181 (184 unzipped) bytes)
def p(g,R=range):u=[[(r*2)[x:x+3]for r in(g*2)[y:y+3]]for x in R(10)for y in R(10)];return[t for a in u for b in u if"0"not in str(t:=[[a[y][x]^b[y][x]for x in R(3)]for y in R(3)])][0]
