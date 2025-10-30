# att (121 bytes, gold)
p=lambda a,*n,d=0:[e for*b,c in zip(*n or p(a,*a),a)if c[0]if(d:=d+any(e:=[*map(lambda x,y:y*(x==y!=c[0]),a,a:=b)]))][:3]

### ovs (138 bytes)
p=eval(('lambda i:'+'[[sum({r.pop()}&)r,r[1:])]*'*2+'[[r[0]r,*i)if]i if])])]').translate([0,"{*r}-{*i[0]}","zip(","for*r,in "]))

##
# 147
exec(f"def p(i):I=i;A=0;{'i=[[A*(A==(A:=B)!=c[0])for*c,B in zip(*I,a)if all(c)]for*a,in zip(*i)];'*2+'*i,=zip(*i[any(i[-1])-2::-1]);'*40}return i")

exec('def p(i):h={*i[0]};return'+'[[a*({a}=={b}-h)for a,b in zip(r,r[1:])]for*r,in zip(*'*2+'[[t[0]for t in zip(s,*i)if{*t}-h]for s in i if{*s}-h])])]')

### joking (147 bytes)
exec("p=lambda i,k=-1:[[sum({r[1]}&{r[0]}-{*i[0]})if k<1else r[1]"+"for*r,in %s)if{*r[1:]}-{*k*i[0]}]"*2%("zip(r[1:],r,*i","k*i or zip(*p(i,k+1)"))

## some rearrangements of the other solution
## slightly hampered by having no idea how the code works
p=lambda i,k=1:-k*[(r[0]for*r,in zip(r,*i)if{*r}-{*i[0]})for*r,in i if{*r}-{*i[0]}]or[[sum({r.pop()}&{*r}-{*i[0]})for*r,in zip(r,r[1:])]for*r,in zip(*p(i,k-1))]
p=lambda i,k=2:[[sum({r[1]}&{r[0]}-{*i[0]})if k else r[1]for*r,in zip(r[1:],r,*i)if k or{*r[1:]}-{*i[0]}]for*r,in(k<1)*i or zip(*p(i,k-1))if k or{*r}-{*i[0]}]
p=lambda i,k=-1:[[sum({r[1]}&{r[0]}-{*i[0]})if k<1else r[1]for*r,in zip(r[1:],r,*i)if{*r[1:]}-{*k*i[0]}]for*r,in k*i or zip(*p(i,k+1))if{*r}-{*k*i[0]}]
exec("p=lambda i,k=1:-k*[(r[0]\2zip(r,*i)if\1)\2i if\1]or[[sum({r.pop()}&\1)\2zip(r,r[1:])]\2zip(*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in "]))
exec("p=lambda i,k=1:-k*[(r[0]\2r,*i)if\1)\2*zip(*i))if\1]or[[sum({r.pop()}&\1)\2r,r[1:])]\2*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in zip("]))
exec("p=lambda i,k=1:-k*[(r[0]\2\3r,*i)if\1)\2i if\1]or[[sum({r.pop()}&\1)\2\3r,r[1:])]\2\3*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in ","zip("]))

### combined (162 bytes)
p=lambda i:[[1//len(q:={*sum([[t[0]for t in zip(s,*i)if{*t,0}>h][y:y+2]for s in i if{*s,0}>(h:={*i[0]})][x:x+2],[])})*max(q-h|{0})for y in[0,1,2]]for x in[0,1,2]]
